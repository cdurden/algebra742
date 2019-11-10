from flask import current_app as app
from flask import render_template, request
from flask_socketio import emit
from pylti.flask import lti
from .models import Player, Game, RequestDenied
from .models import db, User, error

@app.route('/algebra742live_lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def algebra742live_init(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        return render_template('memory.html')
        #return render_template('index.html', user=user)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

@app.route('/')
@lti(request='session', error=error, app=app)
def algebra742live():
    """Serve the index HTML"""
    return render_template('algebra742live.html')

@socketio.on('connect')
@lti(request='session', error=error, app=app)
def on_connect():
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    ROOM.add_player(request.sid, user)
    emit('reset_screen', DATA, room=request.sid)

@socketio.on('disconnect')
@lti(request='session', error=error, app=app)
def disconnect(lti=lti):
    player = ROOM.get_player(request.sid)
    if player:
        ROOM.remove_player(player)
        reset_game(room)

@socketio.on('input')
@lti(request='session', error=error, app=app)
def input(data, lti=lti):
    print("receiving input")
    """submit response and rebroadcast game object"""
    response = data['response']
    player = ROOM.get_player(request.sid)
    try:
        ROOM.input(player, response, update_game)
    except RequestDenied as err:
        print(err.message) 

def update_game(room):
    print("updating game")
    emit('update_game', ROOM.to_dict(), room=room)

def reset_game(room):
    print("reseting game")
    emit('reset_game', ROOM.to_dict(), room=room)

#@socketio.on('submit_answer')
#def on_submit_answer(data):
#    """flip card and rebroadcast game object"""
#    room = data['room']
#    answer = data['answer']
#    ROOMS[room].flip_card(card)
#    send(ROOMS[room].to_json(), room=room)
