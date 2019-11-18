#import gevent.monkey
#gevent.monkey.patch_all()
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
import game
from game import RequestDenied

# initialize Flask
from pylti.flask import lti
from algebra742 import User, error
VERSION = '0.0.1'
app = Flask(__name__)
app.config.from_object('config')
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def to_dict(self):
        return({ 'id': self.id,
                 'username': self.username,
                 'firstname': self.firstname,
                 'lastname': self.lastname,
                 'lti_user_id': self.lti_user_id })

def error(exception=None):
    """ render error page

    :param exception: optional exception
    :return: the error.html template rendered
    """
    return render_template('error.html')


@app.route('/memory_lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def memory_init(lti=lti):
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

@app.route('/memory')
@lti(request='session', error=error, app=app)
def memory():
    """Serve the index HTML"""
    return render_template('memory.html')

@socketio.on('create')
@lti(request='session', error=error, app=app)
def on_create(data, lti=lti):
    """Create a game lobby"""
    #username = data['username']
    gm = game.Game()
    room = gm.room
    ROOMS[room] = gm
    data['room'] = room
    on_join(data)
    #join_room(room)
    #emit('join_room', {'room': room})

@socketio.on('disconnect')
@lti(request='session', error=error, app=app)
def disconnect(lti=lti):
    for room in ROOMS:
        player = ROOMS[room].get_player(request.sid)
        if player:
            ROOMS[room].remove_player(player)
            reset_game(room)

@socketio.on('join')
@lti(request='session', error=error, app=app)
def on_join(data, lti=lti):
    print("joining room")
    """Join a game lobby"""
    #username = data['username']
    room = data['room']
    print(lti)
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if room in ROOMS:
        # add player and rebroadcast game object
        try:
            ROOMS[room].add_player(request.sid, user)
        except RequestDenied as err:
            emit('error', {'error': 'Unable to join room. {:s}'.format(err.message)})
        join_room(room)
        #send(ROOMS[room].to_json(), room=room)
        emit('join_room', {'room': room})
        reset_game(room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'})

@socketio.on('input')
@lti(request='session', error=error, app=app)
def input(data, lti=lti):
    print("receiving input")
    """submit response and rebroadcast game object"""
    room = data['room']
    response = data['response']
    player = ROOMS[room].get_player(request.sid)
    try:
        ROOMS[room].input(player, response, update_game)
    except RequestDenied as err:
        print(err.message) 

def update_game(room):
    print("updating game")
    emit('update_game', {'flipped_cards': map(lambda card: card.to_dict(), ROOMS[room].flipped_cards), 'players': map(lambda player: player.to_dict(), ROOMS[room].players), 'active_player': ROOMS[room].active_player}, room=room)

def reset_game(room):
    print("reseting game")
    emit('reset_game', {'flipped_cards': map(lambda card: card.to_dict(), ROOMS[room].flipped_cards), 'players': map(lambda player: player.to_dict(), ROOMS[room].players), 'active_player': ROOMS[room].active_player}, room=room)


@socketio.on('flip_card')
@lti(request='session', error=error, app=app)
def on_flip_card(data, lti=lti):
    """flip card and rebroadcast game object"""
    print("flipping card")
    room = data['room']
    card = int(data['card'])
    player = ROOMS[room].get_player(request.sid)
    try:
        assert player is not None
    except AssertionError:
        emit('error', {'error': 'Unable to flip card. Player {:s} not in game'.format(request.sid)})
    try:
        ROOMS[room].flip_card(player, card, lambda: emit('prompt', { 'player': player.to_dict() }, room=request.sid))
        update_game(room)
    except RequestDenied as err:
        print(err.message)
    #send(ROOMS[room].to_json(), room=room)

#@socketio.on('submit_answer')
#def on_submit_answer(data):
#    """flip card and rebroadcast game object"""
#    room = data['room']
#    answer = data['answer']
#    ROOMS[room].flip_card(card)
#    send(ROOMS[room].to_json(), room=room)

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0')
