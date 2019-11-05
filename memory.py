from flask import Flask, render_template, request
from flask_socketio import SocketIO, join_room, emit
import game
from game import RequestDenied

# initialize Flask
from pylti.flask import lti
from algebra742 import app, db, User, error
socketio = SocketIO(app)
ROOMS = {} # dict to track active rooms

@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET'])
@app.route('/lti/', methods=['GET', 'POST'])
@lti(request='initial', error=error, app=app)
def index(lti=lti):
    """ initial access page to the lti provider.  This page provides
    authorization for the user.

    :param lti: the `lti` object from `pylti`
    :return: index page for lti provider
    """
    user = db.session.query(User).filter_by(lti_user_id=lti.name).first()
    if user:
        return render_template('index.html', user=user)
    else:
        form = UserInfoForm()
        return render_template('GetUserInfo.html', lti=lti, form=form)

@lti(request='session', error=error, app=app)
@app.route('/memory')
def index():
    """Serve the index HTML"""
    return render_template('memory.html')

@socketio.on('create')
def on_create(data):
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
def disconnect():
    for room in ROOMS:
        player = ROOMS[room].get_player(request.sid)
        if player:
            ROOMS[room].remove_player(player)
            reset_game(room)

@socketio.on('join')
def on_join(data):
    print("joining room")
    """Join a game lobby"""
    #username = data['username']
    room = data['room']
    if room in ROOMS:
        # add player and rebroadcast game object
        try:
            ROOMS[room].add_player(request.sid)
        except RequestDenied as err:
            emit('error', {'error': 'Unable to join room. {:s}'.format(err.message)})
        join_room(room)
        #send(ROOMS[room].to_json(), room=room)
        emit('join_room', {'room': room})
        reset_game(room)
    else:
        emit('error', {'error': 'Unable to join room. Room does not exist.'})

@socketio.on('input')
def input(data):
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
def on_flip_card(data):
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
    socketio.run(app, debug=True)
