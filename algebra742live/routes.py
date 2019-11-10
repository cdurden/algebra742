from flask import current_app as app
from flask import render_template, request
from flask_socketio import emit
from pylti.flask import lti
from .models import db, User, Player, Game, RequestDenied
from . import socketio, ROOMS

def error(exception=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')

@app.route('/algebra742live_lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error)
def algebra742live_init(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        return render_template('algebra742live.html')
        #return render_template('index.html', user=user)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

@app.route('/')
@lti(request='session', error=error)
def algebra742live():
    """Serve the index HTML"""
    return render_template('algebra742live.html')

@socketio.on('connect')
@lti(request='session', error=error)
def on_connect(lti=lti):
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    ROOMS[0].add_player(request.sid, user)
    emit('reset_screen', ROOMS[0].to_json(), room=request.sid)

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

def update_game():
    print("updating game")
    emit('update_game', ROOMS[0].to_json(), broadcast=True)

def reset_game():
    print("reseting game")
    emit('reset_game', ROOMS[0].to_json(), broadcast=True)

