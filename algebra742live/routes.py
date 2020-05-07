from flask import current_app as app
from flask_restful import reqparse, abort, Api, Resource
from functools import wraps
from flask import render_template, request, redirect, url_for, send_file, make_response, session
from flask import jsonify
from flask_socketio import emit
from pylti.flask import lti
#import models
#from .models import db, ma, RequestDenied
from .models.Question import Question, question_scores, get_question_from_digraph_node, get_snow_qm_task, get_question
from .models.Game import GameClasses
from .models.Board import Board
#from .models import get_or_create
from . import db, ma
from . import socketio, ROOMS
from werkzeug.datastructures import MultiDict, ImmutableMultiDict, FileStorage
from werkzeug.utils import secure_filename
from sqlalchemy.sql import select, and_, desc

from flask_wtf import Form
from wtforms import TextField, IntegerField, BooleanField, FieldList, StringField, RadioField, IntegerField, FormField, TextAreaField
import json
import os
import sys
if sys.version_info[0] < 3:
    import pathlib2 as pathlib
else:
    import pathlib
import tempfile
from .models.util import params_hash_lookup, graphics_path
#def lti(app=None, request='any', error=None, role='any',
#        *lti_args, **lti_kwargs):
#    """
#    LTI decorator
#    :param: app - Flask App object (optional).
#        :py:attr:`flask.current_app` is used if no object is passed in.
#    :param: error - Callback if LTI throws exception (optional).
#        :py:attr:`pylti.flask.default_error` is the default.
#    :param: request - Request type from
#        :py:attr:`pylti.common.LTI_REQUEST_TYPE`. (default: any)
#    :param: roles - LTI Role (default: any)
#    :return: wrapper
#    """
#
#    def _lti(function):
#        """
#        Inner LTI decorator
#        :param: function:
#        :return:
#        """
#
#        @wraps(function)
#        def wrapper(*args, **kwargs):
#            kwargs['lti'] = None 
#            return function(*args, **kwargs)
#
#        return wrapper
#
#    lti_kwargs['request'] = request
#    lti_kwargs['error'] = error
#    lti_kwargs['role'] = role
#
#    if (not app) or isinstance(app, Flask):
#        lti_kwargs['app'] = app
#        return _lti
#    else:
#        # We are wrapping without arguments
#        lti_kwargs['app'] = None
#        return _lti(app)

def error(exception=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    print(exception)
    return render_template('error.html')

class UserInfoForm(Form):
    """ Add data from Form

    :param Form:
    """
    username = StringField('username')
    firstname = StringField('firstname')
    lastname = StringField('lastname')

#@app.route('/reveal/', methods=['GET', 'POST'])
#def reveal():
#    return render_template("reveal.html")
@app.route('/api/snow-qm-task/')
@app.route('/api/snow-qm-task/<collection_id>/<task_id>')
def render_snow_qm_task(collection_id=None,task_id=None):

    question = get_snow_qm_task(collection_id, task_id)
    response = make_response(question.render_html())
    response.mimetype = 'text/html'
    return response

@socketio.on('chat-message')
@lti(request='session', error=error)
def handle_chat_message(data, lti=lti):
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    if user is None:
        raise RequestDenied
    print(user)
    output = "{:s} {:s}: {:s}".format(user.firstname, user.lastname, data)
    print(output)
    app.logger.info(output)
    emit('chat-message', output, broadcast=True)

@socketio.on('get_snow_qm_task')
@lti(request='session', error=error)
def get_snow_qm_task_data(data, lti=lti):
    question = get_snow_qm_task(data['collection'], data['task'])
    try:
        user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
        statement = select([question_scores,Question.__table__]).where(and_(question_scores.c.user_id==user.id, question_scores.c.question_id==Question.__table__.c.id, Question.__table__.c.id==question.id)).order_by(desc('datetime'))
        results = db.session.execute(statement).first()
    except RequestDenied:
        pass
    try:
        formdata = json.loads(results.answer)
        print("got form data")
        print(formdata)
    except AttributeError:
        formdata = None
    try:
        question.build_form(formdata=formdata)
    except RequestDenied:
        pass
    print(question.form.data)
    data['html'] = question.render_html()
    data['question_id'] = question.id
    data['question'] = question.to_json()
    print('emitting form data')
    emit('snow_qm_task_data', data)

@app.route('/lti/', methods=['GET','POST'])
@lti(request='initial', error=error)
def lti_post(lti=lti):
    """ initial access page to the lti provider.
    This page provides authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    #print(request.headers.get('Authorization'))
    #print(session)
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    print(user)
    if user:
        resp = redirect("/lti2/")
        resp.headers.add('Set-Cookie','cross-site-cookie=bar; SameSite=None; Secure')
    else:
        form = UserInfoForm()
        resp = render_template('GetUserInfo.html', lti=lti, form=form)
    #resp.set_cookie('test', 'foo');
    # Ensure you use "add" to not overwrite existing cookie headers
    return resp

@app.route('/lti2/', methods=['GET'])
@lti(request='session', error=error)
def lti_get(lti=lti):
    """ initial access page to the lti provider.
    This page provides authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    #print(request.headers.get('Authorization'))
    #print(request.cookies.get('session'))
    #print(request.cookies.get('test'))
    #print(session)
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    print(user)
    if request.cookies.get('session_is_set') == 'true':
        if user:
            try:
                resp = redirect(request.args['redirect'])
            except:
                #return make_response('<meta http-equiv="Refresh" content="5; url="/static/teaching_assets/md/#schedule" />')
                resp = redirect("/static/teaching_assets/md/#schedule")
        else:
            form = UserInfoForm()
            resp = render_template('GetUserInfo.html', lti=lti, form=form)
    else:
        resp = redirect("/lti2/")
    #resp.set_cookie('same-site-cookie', 'foo', samesite='Lax');
    # Ensure you use "add" to not overwrite existing cookie headers
    #resp.headers.add('Set-Cookie','cross-site-cookie=bar; SameSite=None; Secure')
    resp.set_cookie('session_is_set', 'true');
    return resp


from marshmallow import Schema, fields, pre_dump
import operator

#class UserSchema(Schema):
#    id = fields.Int(dump_only=True)
#    username = fields.String(required=True)
#    firstname = fields.String(required=True)
#    lastname = fields.String(required=True)
#    lti_user_id = fields.String(required=False)
#
#class UserViewBase(GenericModelView):
#    model = models.User
#    schema = UserSchema()
#    authentication = MyHeaderAuthentication()
#    filtering = Filtering(lti_user_id=ColumnFilter(operator.eq, required=True))
#
#class UserListView(UserViewBase):
#    def get(self):
#        return self.list()
#
#    def post(self):
#        return self.create()
#
#class UserView(UserViewBase):
#    def get(self, id):
#        return self.retrieve(id)
#
#    def patch(self, id):
#        return self.update(id, partial=True)
#
#    def delete(self, id):
#        return self.destroy(id)
#
from .models.authentication import HeaderAuthentication as HeaderAuthentication_
from . import models
from models.User import get_users, get_user_by_id, get_user_by_lti_user_id
from models.Task import get_tasks, get_task_by_id, get_task_from_source, get_task_data_by_source_pattern
from models.Submission import get_submission_by_id, get_submissions
from models.Board import get_boards, get_board_by_id, get_latest_board
from models.Feedback import get_feedback
from models.util import SerializableGenerator
import flask_restful.representations.json

def new_alchemy_encoder():
    _visited_objs = []

    class AlchemyEncoder(json.JSONEncoder):
        def default(self, obj):
            print("running AlchemyEncoder on object "+obj+" of class "+obj.__class__)
            #if isinstance(obj.__class__, DeclarativeMeta):
            if isinstance(obj.__class__, db.Model):
                # don't re-visit self
                if obj in _visited_objs:
                    return None
                _visited_objs.append(obj)

                # an SQLAlchemy class
                fields = {}
                for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
                    fields[field] = obj.__getattribute__(field)
                # a json-encodable dict
                return fields

            return json.JSONEncoder.default(self, obj)

    return AlchemyEncoder


class ApiError(Exception):
    pass

from functools import wraps
class HeaderAuthentication(HeaderAuthentication_):
    credentials_arg = 'auth_token'
    def get_request_credentials(self):
        token = self.get_request_token()
        if token != app.config['AUTH_TOKEN']:
            print(token)
            print(app.config['AUTH_TOKEN'])
            raise ApiError(401, "Authentication failed")
        else:
            return self.get_credentials_from_token(token)

def alchemy_json_encoder(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        flask_restful.representations.json.settings['cls'] = new_alchemy_encoder()
        return f(*args, **kwargs)
    return wrapper

def api_authenticate(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if HeaderAuthentication().get_request_credentials():
            return f(*args, **kwargs)
        else:
            raise ApiError(401, "Authentication failed")
    return wrapper

class UserSchema(ma.ModelSchema):
    class Meta:
        model = db.User
        include_fk = True
    #tasks = fields.List(fields.Nested("TaskSchema", exclude=("boards",)))
    #boards = fields.List(fields.Nested("BoardSchema", exclude=("task","user")))
    #submissions = fields.List(fields.Nested("SubmissionSchema", exclude=("task","user",)))

user_schema = UserSchema(exclude=("boards",))
users_schema = UserSchema(many=True, exclude=("boards",))

class TaskSchema(ma.ModelSchema):
    submissions = fields.List(fields.Nested("SubmissionSchema", exclude=("task",)))
    #submissions = fields.List(fields.Nested("SubmissionSchema"))
    boards = fields.List(fields.Nested("BoardSchema", exclude=("task",)))
    data = fields.Function(lambda obj: obj.data())
    class Meta:
        model = db.Task
        include_fk = True

task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

class SubmissionSchema(ma.ModelSchema):
    class Meta:
        model = db.Submission
        include_fk = True
    user = fields.Nested("UserSchema")
    board = fields.Nested("BoardSchema", exclude=())
    task = fields.Nested("TaskSchema", exclude=("submissions","boards"))

submission_schema = SubmissionSchema()
submissions_schema = SubmissionSchema(many=True)

class BoardSchema(ma.ModelSchema):
    class Meta:
        model = db.Board
        include_fk = True
    task = fields.Nested("TaskSchema")
    user = fields.Nested("UserSchema", exclude=("boards","submissions",))
    data = fields.Dict()
    shapeStorage = fields.Dict()
    @pre_dump
    def load_data(self, obj):
        if obj is not None:
            obj.data = obj.get_data()
            obj.shapeStorage = obj.data
        return obj

board_schema = BoardSchema(exclude=("data_json",))
boards_schema = BoardSchema(many=True)

class FeedbackSchema(ma.ModelSchema):
    class Meta:
        model = db.Feedback
        include_fk = True
    data = fields.Dict()
    board = fields.Nested("BoardSchema", exclude=("submissions","feedback",))
    submission = fields.Nested("SubmissionSchema", exclude=("feedback",))
    @pre_dump
    def load_data(self, obj):
        obj.data = obj.get_data()
        return obj

feedback_schema = FeedbackSchema(exclude=("data_json",))
feedback_list_schema = FeedbackSchema(many=True, exclude=("data_json",))

class User(Resource):
    @api_authenticate
    def get(self, lti_user_id):
        user = get_user_by_lti_user_id(lti_user_id)
        #return user.to_json()
        return user_schema.dump(user)

class UserList(Resource):
    @api_authenticate
    def get(self):
        users = get_users()
        #return user.to_json()
        return users_schema.dump(users)

class Task(Resource):
    @api_authenticate
    def get(self, task_id):
        task = get_task_by_id(db.session, task_id)
        #return task.to_json()
        return task_schema.dump(task)

class TaskList(Resource):
    @api_authenticate
    def get(self):
        if 'task_id' in request.args:
            task_ids = request.args['task_id']
            tasks = [get_task_by_id(task_id) for task_id in task_ids]
        else:
            tasks = get_tasks()
        #return [task.to_json() for task in tasks]
        flask.ext.restful.representations.json.settings["cls"] = new_alchemy_encoder() 
        return tasks_schema.dump(tasks)

class SourcedTask(Resource):
    @api_authenticate
    def get(self, source):
        task = get_task_from_source(source)
        #return task.to_json()
        return task_schema.dump(task)

class SourcedTaskList(Resource):
    @api_authenticate
    def get(self):
        sources = request.args.getlist('source')
        tasks = [get_task_from_source(source) for source in sources]
        #return [task.to_json() for task in tasks]
        return tasks_schema.dump(tasks)

class SourcedTaskBoardList(Resource):
    @api_authenticate
    def get(self):
        sources = request.args.getlist('source')
        parser = reqparse.RequestParser()
        parser.add_argument('lti_user_id')
        args = parser.parse_args()
        user = get_user_by_lti_user_id(args['lti_user_id'])
        tasks = [get_task_from_source(source) for source in sources]
        for task in tasks:
            task.boards = task.get_user_boards(user)
        #return [task.to_json() for task in tasks]
        return tasks_schema.dump(tasks)


class TaskDataList(Resource):
    @api_authenticate
    def get(self, source_pattern):
        tasks_data = get_task_data_by_source_pattern(source_pattern)
        return SerializableGenerator(tasks_data)
        #return [task.to_json() for task in tasks]

class Submission(Resource):
    @api_authenticate
    def get(self, submission_id):
        submission = get_submission_by_id(db.session, submission_id)
        #return submission.to_json()
        return submission_schema.dump(submission)

class SubmissionList(Resource):
    @api_authenticate
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('data')
        args = parser.parse_args()
        kwargs = args['data'] or {}
        submissions = get_submissions(**kwargs)
        return submissions_schema.dump(submissions)
        #return([submission.to_json() for submission in get_submissions(**kwargs)])

class TaskSubmissionList(Resource):
    @api_authenticate
    def get(self, task_id):
        return(submissions_schema.dump(get_submissions(task_id=task_id)))

    @api_authenticate
    def post(self, task_id):
        parser = reqparse.RequestParser()
        task = get_task_by_id(task_id)
        parser.add_argument('lti_user_id')
        parser.add_argument('board_id')
        parser.add_argument('data')
        #for field in task.get_submission_fields():
        #    parser.add_argument(field)
        args = parser.parse_args()
        user = get_user_by_lti_user_id(args['lti_user_id'])
        submission = user.submit(task, args['data'], args['board_id'])
        return submission_schema.dump(submission), 201
        #return submission.to_json(), 201

class Board(Resource):
    @api_authenticate
    def get(self, lti_user_id, board_id):
        user = get_user_by_lti_user_id(lti_user_id)
        board = user.get_board_by_boardId(board_id)
        print("Getting board {:s} for user {:s}".format(board_id, lti_user_id))
        print(board)
        return board_schema.dump(board)

class LatestBoard(Resource): # FIXME: this is a mess; we should not be passing task_id along with board_id. Separate this into two separate resource handlers
    @api_authenticate
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task_id')
        parser.add_argument('submission_id')
        parser.add_argument('lti_user_id')
        args = parser.parse_args()
        lti_user_id = args.pop('lti_user_id')
        user = get_user_by_lti_user_id(lti_user_id)
        args['user_id'] = user.id
        print("getting latest board with args:")
        print(args)
        board = get_latest_board(**args)
        print(board)
        return board_schema.dump(board)

class BoardList(Resource):
    @api_authenticate
    def get(self):
        return(boards_schema.dump(get_boards()))

    @api_authenticate
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('lti_user_id')
        parser.add_argument('data', type=dict, location='json')
        parser.add_argument('data_json')
        parser.add_argument('task_id')
        parser.add_argument('boardId')
        parser.add_argument('file', type=FileStorage, location='files')
        args = parser.parse_args()
        data_json = args['data_json']
        if data_json is None:
            data = args['data']
            data_json = json.dumps(data)
        #if args['boardId'] is not None: # FIXME: maybe this should go in a put request instead
        #    print("saving board with id "+boardId)
        #    board = get_board_by_board_id(boardId)
        #    if board.user_id == user.id:
        #        board.save(data)
        #else:
        print(args)
        print(args['lti_user_id'])
        user = get_user_by_lti_user_id(args['lti_user_id'])
        file_upload = args['file']
        if file_upload is not None:
            filename = secure_filename("{:s}.png".format(args['boardId']))
        else:
            filename = None
        board = user.save_board(data_json, args['boardId'], args['task_id'], filename) # FIXME: allow client to set board_id
        if board is not None and file_upload is not None:
            filedir = pathlib.Path(app.config["PRIVATE_DATA_PATH"],user.lti_user_id.split(":")[0])
            filepath = pathlib.Path(filedir,filename)
            filedir.mkdir(parents=True, exist_ok=True) #FIXME: handle exceptions, e.g. file exists in place of directory
            with tempfile.NamedTemporaryFile(delete=False) as fp:
                file_upload.save(fp) 
            print("Saved temporary file at: {:s}".format(fp.name))
            tempfilepath = pathlib.Path(fp.name)
            tempfilepath.rename(filepath)
        return board_schema.dump(board), 201

class TaskBoard(Resource):
    @api_authenticate
    def get(self, task_id):
        board = user.get_latest_board_by_task_id(db.session, task_id)
        return board_schema.dump(board)

class TaskBoardList(Resource):
    @api_authenticate
    def get(self, task_id):
        return(boards_schema.dump(get_boards(task_id=task_id)))

    @api_authenticate
    def post(self, task_id):
        parser = reqparse.RequestParser()
        task = get_task_by_id(task_id)
        parser.add_argument('lti_user_id')
        parser.add_argument('data')
        #for field in task.get_board_fields():
        #    parser.add_argument(field)
        args = parser.parse_args()
        user = get_user_by_lti_user_id(args['lti_user_id'])
        board = user.submit(task, args['data'])
        return board_schema.dump(board)
        #return board.to_json(), 201

class Assignments(Resource):
    @api_authenticate
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('assignments', type=dict, location='json')
        args = parser.parse_args()
        assignments = args['assignments']
        users = []
        for (user_id, assignment) in assignments.items():
            user = get_user_by_id(user_id)
            user.assignment = assignment
            users.append(user)
        db.session.commit()
        return users_schema.dump(users)

class FeedbackList(Resource):
    @api_authenticate
    def get(self):
        return(feedback_list_schema.dump(get_feedback()))

#    @api_authenticate
#    def post(self):
#        print("posting feedback")
#        parser = reqparse.RequestParser()
#        parser.add_argument('users', type=list, location='json')
#        parser.add_argument('tasks', type=list, location='json')
#        parser.add_argument('submissions', type=list, location='json')
#        parser.add_argument('lti_user_id')
#        parser.add_argument('boardId')
#        parser.add_argument('data', type=dict, location='json')
#        args = parser.parse_args()
#        data = args['data']
#        user = get_user_by_lti_user_id(args['lti_user_id'])
#        board = user.save_board({}, args['boardId'])
#        if args['submissions'] is not None:
#            submissions = [get_submission_by_id(submission.id) for submission in args['submissions']]
#            for submission in submissions:
#                feedback = user.create_feedback(board, submission=submission)
#        else:
#            users = [get_user_by_id(user_id) for user_id in args['users']]
#            tasks = [get_task_from_source(task) for task in args['tasks']]
#            for recipient in users:
#                for task in tasks:
#                    feedback = user.create_feedback(board, recipient, task)
#        print(board)
#        print(board_schema.dump(board))
#        return board_schema.dump(board), 201
    @api_authenticate
    def post(self):
        print("posting feedback")
        parser = reqparse.RequestParser()
        parser.add_argument('submission_id', type=list, location='json')
        parser.add_argument('lti_user_id')
        parser.add_argument('boardId')
        parser.add_argument('data', type=dict, location='json')
        args = parser.parse_args()
        data = args['data']
        user = get_user_by_lti_user_id(args['lti_user_id'])
        board = user.save_board({}, args['boardId'])
        submission = get_submission_by_id(submission.id)
        feedback = user.create_feedback(board, submission=submission)
        return feedback_schema.dump(feedback), 201

class FileUpload(Resource):
    @api_authenticate
    def post(self):
        print("Received FileUpload POST request")
        parse = reqparse.RequestParser()
        parse.add_argument('file', type=FileStorage, location='files')
        parse.add_argument('boardId', type=str, location='form')
        args = parse.parse_args()
        file_upload = args['file']
        print(file_upload)
        boardId = args['boardId']
        print(boardId)
        return '', 201
        board = get_or_create_board_by_boardId(boardId)
        if board is not None:
            filename = "{:s}.png".format(boardId)
            file_upload.save(os.path.join(app.config["PRIVATE_DATA_PATH"],filename))
            board.background_image = filename
            db.session.commit()
        #chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        return board_schema.dump(board), 201

class File(Resource):
    #@api_authenticate
    def get(self, lti_user_id, filename):
        #parser = reqparse.RequestParser()
        #parser.add_argument('lti_user_id')
        #parser.add_argument('filename')
        #args = parser.parse_args()
        #user = get_user_by_lti_user_id(lti_user_id)
        filepath = os.path.join(app.config["PRIVATE_DATA_PATH"],lti_user_id.split(":")[0],filename)
        return send_file(filepath)


api = Api(app)
api.add_resource(User, "/api/user/<lti_user_id>")
api.add_resource(UserList, "/api/users/")
api.add_resource(Task, "/api/task/<task_id>")
api.add_resource(TaskList, "/api/tasks/")
api.add_resource(SourcedTask, "/api/task/source/<source>/")
api.add_resource(SourcedTaskList, "/api/tasks/source/")
api.add_resource(SourcedTaskBoardList, "/api/tasks/source/boards/")
api.add_resource(TaskDataList, "/api/tasks/data/<source_pattern>/")
api.add_resource(Submission, "/api/submission/<submission_id>")
api.add_resource(TaskSubmissionList, "/api/task/<task_id>/submissions/")
api.add_resource(SubmissionList, "/api/submissions/")
api.add_resource(Board, "/api/user/<lti_user_id>/board/<board_id>")
api.add_resource(LatestBoard, "/api/board/")
api.add_resource(BoardList, "/api/boards/")
api.add_resource(TaskBoard, "/api/task/<task_id>/board/")
api.add_resource(TaskBoardList, "/api/task/<task_id>/boards/")
api.add_resource(Assignments, "/api/assignments/")
api.add_resource(FeedbackList, "/api/feedback/")
api.add_resource(FileUpload, "/api/upload")
api.add_resource(File, "/api/file/<lti_user_id>/<filename>")

@app.route('/slides/<deck>')
@lti(request='session', error=error)
def slides(deck,lti=lti):
    with open(os.path.join(app.config["TEACHING_ASSETS_DIR"],'/slides/decks/{:s}.json'.format(deck))) as f:
        data = json.load(f)
    collection = data['collection']
    slides = [] 
    for slide in data['slides']:
        with open(os.path.join(app.config["TEACHING_ASSETS_DIR"],'/slides/slides/{:s}/{:s}'.format(collection,slide[0]))) as f:
            html = f.read()
            slides.append(html)
    """Serve the index HTML"""
    return render_template(reveal_template, slides)

@app.route('/')
@lti(request='session', error=error)
def algebra742live(lti=lti):
    """Serve the index HTML"""
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    if user:
        return render_template(ROOMS[0].template)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

@app.route('/admin/', methods=['GET', 'POST'])
@lti(request='session', role='staff', error=error)
def admin(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    if user.id==86:
        game = app.extensions['redis'].get('game').decode('utf-8')
        params = app.extensions['redis'].get('params').decode('utf-8')
        return render_template("admin.html", GameClasses=GameClasses, game=game, params=params)
    else:
        raise RequestDenied

@socketio.on('save_work')
@lti(request='session', error=error)
def save_work(data, lti=lti):
    print("saving work")
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    game = app.extensions['redis'].get('game').decode('utf-8')
    params = json.loads(app.extensions['redis'].get('params').decode('utf-8'))
    work = get_or_create(db.session, Work, user_id=user.id, template=params['template'])
    #work.data = json.dumps(data)
    work.data = data
    db.session.commit()

@app.route('/load_work', methods=['GET','POST'])
@lti(request='session', error=error)
def load_work(lti=lti):
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    game = app.extensions['redis'].get('game').decode('utf-8')
    params = json.loads(app.extensions['redis'].get('params').decode('utf-8'))
    work = get_or_create(db.session, Work, user_id=user.id, template=params['template'])
    response = app.response_class(
        response=work.data,
        status=200,
        mimetype='application/json'
    )
    return response

@socketio.on('set_game')
@lti(request='session', role='staff', error=error)
def set_game(data, lti=lti):
    app.extensions['redis'].set('game',data['game'])
    app.extensions['redis'].set('params',data['params'])
    ROOMS[0] = GameClasses[data['game']](**json.loads(data['params']))
    emit('update_game', {}, broadcast=True)

@socketio.on('connect')
@lti(request='session', error=error)
def on_connect(lti=lti):
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    ROOMS[0].add_player(request.sid, user)
    emit('reset_game', ROOMS[0].to_json(), room=request.sid)

@socketio.on('disconnect')
@lti(request='session', error=error)
def disconnect(lti=lti):
    player = ROOMS[0].get_player(request.sid)
    if player:
        ROOMS[0].remove_player(player)
        reset_game()

#@socketio.on('input')
#@lti(request='session', error=error)
#def input(data, lti=lti):
#    print("receiving input")
#    """submit response and rebroadcast game object"""
#    response = data['response']
#    player = ROOMS[0].get_player(request.sid)
#    try:
#        ROOMS[0].input(player, response, update_game)
#    except RequestDenied as err:
#        print(err.message) 

@socketio.on('get_question_data')
@lti(request='session', error=error)
def get_question_data(data, lti=lti):
    question = get_question_from_digraph_node(data['graph'],data['node'])
    data['html'] = question.render_html()
    data['question_id'] = question.id
    emit('question_data', data)

def output(data):
    print("emitting output")
    emit('output', data)

def update_game():
    emit('update_game', ROOMS[0].to_json(), broadcast=True)

@socketio.on('form_submit')
@lti(request='session', error=error)
def question_input(data, lti=lti):
    print("receiving input")
    """submit response and rebroadcast game object"""
    print(data)
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    if user is None:
        raise RequestDenied
    print(user)
    question_id = data['question_id']
    question_class = data['question_class']
    question = get_question(question_class, question_id)
    if question is None:
        raise RequestDenied
    #question = get_or_create(db.session, QuestionClasses[question_class], id=question_id)
    question.build_form(ImmutableMultiDict(data))
    print(question.form.data)
    correct = question.check_answer()
    if correct:
        print("answer is correct")
    else:
        print("answer is incorrect")
    output({'correct': True, 'message': None, 'question': question.to_json(), 'input_data': data})
    question.record_answer(user, question.score_answer())

#@socketio.on('form_submit')
#@lti(request='session', error=error)
#def form_submit(data, lti=lti):
#    print("receiving input")
#    """submit response and rebroadcast game object"""
#    print(data)
#    player = ROOMS[0].get_player(request.sid)
#    try:
#        ROOMS[0].input(player, data, output)
#    except RequestDenied as err:
#        print(err.message) 

def reset_game():
    emit('reset_game', ROOMS[0].to_json(), broadcast=True)

@app.route('/graphics/<engine>/<template>/<params_hash>', methods=['GET','POST'])
@lti(request='session', error=error)
def graphics(template=None, engine=None, params_hash=None, lti=lti):
    return send_file(graphics_path(app,engine,template,params_hash))

@app.route('/userinfo', methods=['GET','POST'])
@lti(request='session', error=error)
def SetUserInfo(lti=lti):
    from sqlalchemy.sql.expression import ClauseElement
    user = db.session.query(db.User).filter_by(lti_user_id=lti.name).first()
    if user:
        user.username = form.username.data
    else:
        form = UserInfoForm()
        user = db.User(lti_user_id=lti.name, username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data)
        db.session.add(user)
    db.session.commit()
    return render_template(ROOMS[0].template, user=user)
