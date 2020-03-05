from flask import current_app as app
from flask import render_template, request
from flask_socketio import emit
from pylti.flask import lti
from .models import db, User, RequestDenied
from .models.Question import get_question_from_digraph_node
from . import socketio, ROOMS

from flask_wtf import Form
from wtforms import TextField, IntegerField, BooleanField, FieldList, StringField, RadioField, IntegerField, FormField, TextAreaField

def error(exception=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')

class UserInfoForm(Form):
    """ Add data from Form

    :param Form:
    """
    username = StringField('username')
    firstname = StringField('firstname')
    lastname = StringField('lastname')

@app.route('/reveal/', methods=['GET', 'POST'])
def reveal():
    return render_template("reveal.html")

@app.route('/algebra742live_lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error)
def algebra742live_lti(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        return render_template(ROOMS[0].template)
        #return render_template('index.html', user=user)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

@app.route('/')
@lti(request='session', error=error)
def algebra742live():
    """Serve the index HTML"""
    return render_template(ROOMS[0].template)

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
    print(data)
    question = get_question_from_digraph_node(data['graph'],data['node'])
    data['html'] = question.render_html()
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

