from flask import current_app as app
from functools import wraps
from flask import render_template, request, redirect, url_for, send_file, make_response
from flask import jsonify
from flask_socketio import emit
from pylti.flask import lti
import models
from .models import db, User, RequestDenied
from .models.Question import get_question_from_digraph_node, get_snow_qm_task
from .models.Game import GameClasses
from .models.Work import Work
from .models import get_or_create
from . import socketio, ROOMS

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

@socketio.on('get_question_data')
def get_snow_qm_task(data, lti=lti):
    print('getting snow qm task data')
    print(data)
    question = get_snow_qm_task(data['collection'], data['task'])
    data['html'] = question.render_html()
    data['question_id'] = question.id
    emit('question_data', data, broadcast=True)

@app.route('/algebra742live_lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error)
def algebra742live_lti(lti=lti):
    """ initial access page to the lti provider.
    This page provides authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    print("starting lti auth")
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    print(user)
    if user:
        return(redirect(url_for('algebra742live')))
        #return render_template(ROOMS[0].template)
        #return render_template('index.html', user=user)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

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

@socketio.on('input')
@lti(request='session', error=error)
def input(data, lti=lti):
    print("receiving input")
    """submit response and rebroadcast game object"""
    response = data['response']
    player = ROOMS[0].get_player(request.sid)
    try:
        ROOMS[0].input(player, response, update_game)
    except RequestDenied as err:
        print(err.message) 

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
def form_submit(data, lti=lti):
    print("receiving input")
    """submit response and rebroadcast game object"""
    print(data)
    player = ROOMS[0].get_player(request.sid)
    try:
        ROOMS[0].input(player, data, output)
    except RequestDenied as err:
        print(err.message) 

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

