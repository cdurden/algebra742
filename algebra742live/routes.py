from flask import current_app as app
from functools import wraps
from flask import render_template, request, redirect, url_for, send_file, make_response
from flask import jsonify
from flask_socketio import emit
from pylti.flask import lti
import models
from .models import db, User, RequestDenied
from .models.Question import Question, question_scores, get_question_from_digraph_node, get_snow_qm_task, get_question
from .models.Game import GameClasses
from .models.Work import Work
from .models import get_or_create
from . import socketio, ROOMS
from werkzeug.datastructures import MultiDict, ImmutableMultiDict
from sqlalchemy.sql import select, and_, desc

from flask_wtf import Form
from wtforms import TextField, IntegerField, BooleanField, FieldList, StringField, RadioField, IntegerField, FormField, TextAreaField
import json
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

@socketio.on('get_snow_qm_task')
@lti(request='session', error=error)
def get_snow_qm_task_data(data, lti=lti):
    print('getting snow qm task data')
    print(data)
    question = get_snow_qm_task(data['collection'], data['task'])
    try:
        user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
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
    data['html'] = question.render_html()
    data['question_id'] = question.id
    print('sending snow qm task data')
    emit('snow_qm_task_data', data, broadcast=True)

@app.route('/lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error)
def algebra742live_lti(lti=lti):
    """ initial access page to the lti provider.
    This page provides authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    print(user)
    if user:
        try:
            resp = redirect(request.args['redirect'])
        except:
            #return make_response('<meta http-equiv="Refresh" content="5; url="/static/teaching_assets/md/#schedule" />')
            resp = redirect("/static/teaching_assets/md/#schedule")
    else:
        form = UserInfoForm()
        resp = render_template('GetUserInfo.html', lti=lti, form=form)
    resp.set_cookie('same-site-cookie', 'foo', samesite='Lax');
    # Ensure you use "add" to not overwrite existing cookie headers
    resp.headers.add('Set-Cookie','cross-site-cookie=bar; SameSite=None; Secure')
    return resp

from marshmallow import Schema, fields
import operator
from flask_resty import GenericModelView, Api, Filtering, ColumnFilter
from flask_resty.exceptions import ApiError
from .models.authentication import HeaderAuthentication
from . import models

class MyHeaderAuthentication(HeaderAuthentication):
    credentials_arg = 'auth_token'
    def get_request_credentials(self):
        token = self.get_request_token()
        if token != app.config['AUTH_TOKEN']:
            raise ApiError(401, "Authentication failed")
        else:
            return self.get_credentials_from_token(token)

class UserSchema(Schema):
    id = fields.Int(dump_only=True)
    username = fields.String(required=True)
    firstname = fields.String(required=True)
    lastname = fields.String(required=True)
    lti_user_id = fields.String(required=False)

class UserViewBase(GenericModelView):
    model = models.User
    schema = UserSchema()
    authentication = MyHeaderAuthentication()
    filtering = Filtering(lti_user_id=ColumnFilter(operator.eq, required=True))

class UserListView(UserViewBase):
    def get(self):
        return self.list()

    def post(self):
        return self.create()

class UserView(UserViewBase):
    def get(self, id):
        return self.retrieve(id)

    def patch(self, id):
        return self.update(id, partial=True)

    def delete(self, id):
        return self.destroy(id)

api = Api(app, prefix="/api")
api.add_resource("/users/", UserListView, UserView)

@app.route('/slides/<template>')
@lti(request='session', error=error)
def slides(template,lti=lti):
    """Serve the index HTML"""
    return render_template(template)

@app.route('/')
@lti(request='session', error=error)
def algebra742live(lti=lti):
    """Serve the index HTML"""
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
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
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user.id==86:
        game = app.extensions['redis'].get('game').decode('utf-8')
        params = app.extensions['redis'].get('params').decode('utf-8')
        return render_template("admin.html", GameClasses=GameClasses, game=game, params=params)
    else:
        raise RequestDenied

@socketio.on('save_work')
@lti(request='session', error=error)
def save_work(data, lti=lti):
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    game = app.extensions['redis'].get('game').decode('utf-8')
    params = json.loads(app.extensions['redis'].get('params').decode('utf-8'))
    work = get_or_create(db.session, Work, user_id=user.id, template=params['template'])
    #work.data = json.dumps(data)
    work.data = data
    print(data)
    db.session.commit()

@app.route('/load_work', methods=['GET','POST'])
@lti(request='session', error=error)
def load_work(lti=lti):
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
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
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
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
    print('getting question data')
    print(data)
    question = get_question_from_digraph_node(data['graph'],data['node'])
    data['html'] = question.render_html()
    data['question_id'] = question.id
    emit('question_data', data, broadcast=True)

def output(data):
    print("emitting output")
    emit('output', data)

def update_game():
    print("updating game")
    emit('update_game', ROOMS[0].to_json(), broadcast=True)

@socketio.on('form_submit')
@lti(request='session', error=error)
def question_input(data, lti=lti):
    print("receiving input")
    """submit response and rebroadcast game object"""
    print(data)
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user is None:
        raise RequestDenied
    question_id = data['question_id']
    question_class = data['question_class']
    question = get_question(question_class, question_id)
    if question is None:
        raise RequestDenied
    #question = get_or_create(db.session, QuestionClasses[question_class], id=question_id)
    question.build_form(ImmutableMultiDict(data))
    print(question.form)
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
    print("reseting game")
    emit('reset_game', ROOMS[0].to_json(), broadcast=True)

@app.route('/graphics/<engine>/<template>/<params_hash>', methods=['GET','POST'])
@lti(request='session', error=error)
def graphics(template=None, engine=None, params_hash=None, lti=lti):
    return send_file(graphics_path(app,engine,template,params_hash))

@app.route('/userinfo', methods=['GET','POST'])
@lti(request='session', error=error)
def SetUserInfo(lti=lti):
    from sqlalchemy.sql.expression import ClauseElement
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        user.username = form.username.data
    else:
        form = UserInfoForm()
        user = User(lti_user_id=lti.name, username=form.username.data, firstname=form.firstname.data, lastname=form.lastname.data)
        db.session.add(user)
    db.session.commit()
    return render_template(ROOMS[0].template, user=user)

