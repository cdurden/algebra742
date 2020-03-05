#from .. import db
from flask_sqlalchemy import SQLAlchemy
import random
import string
from datetime import datetime
from networkx.drawing.nx_pydot import read_dot
import os
import json

db = SQLAlchemy()

def get_question_from_digraph_node(graph, node):
    questions_digraph = read_dot(os.path.join(app.config["DOT_PATH"],data['graph']+'.dot'))
    node_data = questions_digraph.nodes[data['node']]
    for k,v in node_data.items():
        node_data[k.strip("\"")] = node_data.pop(k).strip("\"").replace("\\","")
        question = get_or_create(db.session, QuestionClasses[node_data['class']], params_json=node_data['params'])
    return(question)

class Player(object):
    def __init__(self, session_id, user):
        self.session_id = session_id
        self.user = user
        self.correct = 0
        self.incorrect = 0
        self.matched_cards = []
        self.color = "yellow"
    def __eq__(self, other):
        return self.session_id == other.session_id
    def __repr__(self):
        return json.dumps(self.to_json())
    def to_json(self):
        return({ 
                'session_id': self.session_id,
                'user': self.user.to_json(),
                'correct': self.correct,
                'incorrect': self.incorrect,
                'matched_cards': [card.to_json() for card in self.matched_cards],
                'color': self.color,
                })

class Game(object):
    # pylint: disable=too-many-instance-attributes
    """Object for tracking game stats"""
    def __init__(self, deck_name='clt1', size='normal', teams=2, wordbank=False, mix=False):
        self.active_player = 0
        self.flipped_cards = []
        self.scripts = []
        #self.matched_cards = [[],[]]
        self.deck_name = deck_name
        self.matches = [x/2 for x in range(0,16)]
        #self.player_data = {} 
        self.players = []
        self.room = self.generate_room_id()
        self.date_created = datetime.now()
        self.date_modified = self.date_created
        #self.screen_html = ""
        #self.__load_deck()
        #random.shuffle(self.deck)
        #for position,card in enumerate(self.deck):
        #    card.position = position
    def input(self, player, data, output_callback):
        pass

    def get_player(self, session_id):
        for player in self.players:
            if player.session_id == session_id:
                return(player)
        return(None)

    def player_is_active(self, player):
        return(self.players[self.active_player] == player)

    def activate_next_player(self):
        self.active_player = (self.active_player+1)%len(self.players)

    def add_player(self, session_id, user):
        """Add playername to player array"""
        player = Player(session_id, user)
        for _player in self.players:
            if _player.session_id == session_id:
                raise RequestDenied("player with id {:s} already exists in this game".format(session_id))
        self.players.append(player)

    def remove_player(self, player):
        """Remove playername to player array"""
        if self.player_is_active(player):
            self.activate_next_player()
        self.players.remove(player)

    @classmethod
    def generate_room_id(cls):
        """Generate a random room ID"""
        id_length = 5
        return ''.join(random.SystemRandom().choice(
            string.ascii_uppercase) for _ in range(id_length))

    # Not sure if anything below is necessary
    def to_json(self):
        """Serialize object to JSON"""
        return {
            #"screen_html": self.screen_html(),
            "scripts": self.scripts,
            "active_player": self.active_player,
            "players": [player.to_json() for player in self.players],
        }

class CardGame(Game):
    def input(self, player, data, output_callback):
        if player not in self.players:
            raise KeyError("player is not in the game.")
        if len(self.flipped_cards) == 2:
            data_to_bool = {'y': True, 'n': False}
            if self.player_is_active(player): # player is active
                if self.match_is_flipped() and data_to_bool[data]:
                    #self.matched_cards[player] += self.flipped_cards
                    player.matched_cards += self.flipped_cards
                    player.correct += 1
                else: # cycle to the next player
                    if not self.match_is_flipped() and not data_to_bool[data]:
                        player.correct += 1
                    else:
                        player.incorrect += 1
                    self.activate_next_player()
                self.flipped_cards = []
                output_callback()
            else: # player is not active
                if self.match_is_flipped() == data_to_bool[data]:
                    player.correct += 1
                else:
                    player.incorrect += 1

    def matched_cards(self):
        matched_cards = []
        for player in self.players:
            matched_cards += player.matched_cards
        return(matched_cards)

    def match_is_flipped(self):
        if len(set(self.flipped_cards)) != 2:
            return(False)
        else:
            print(self.flipped_cards[0]);
            print(self.flipped_cards[1]);
            return(self.matches[self.flipped_cards[0].i]==self.matches[self.flipped_cards[1].i])

    def flip_card(self, player, card_position, input_callback):
        try:
            card = self.deck[card_position]
        except IndexError:
            raise RequestDenied("There is no card at that position in the deck")
        if player not in self.players:
            raise KeyError("player is not in the game.")
        #if type(player) != int:
        #    raise TypeError("player must be an integer. Got type {:s}.".format(type(player)))
        if card not in self.deck:
            raise TypeError("card must in the deck.")
        """Assign color to card in solution dict"""
        if self.player_is_active(player) and len(self.flipped_cards) < 2 and card not in self.matched_cards() and card not in self.flipped_cards: 
            self.flipped_cards.append(card)
            if len(self.flipped_cards) == 2:
                input_callback()
        else:
            raise RequestDenied("Player {:s} tried to flip a{:s} card when player {:s} was active and {:d} cards were already flipped".format(player.session_id, ' matched' if card in self.matched_cards() else (' flipped' if card in self.flipped_cards else ''), self.players[self.active_player].session_id, len(self.flipped_cards)))
#    def __load_deck(self):
#        with open(os.path.join(DECKS_ROOT,self.deck_name), 'r') as deck_file:
#            self.deck = [Card(i,info=elem) for i,elem in enumerate(deck_file.read().split('\n')) if len(elem.strip()) > 0]


class Node:
    def __init__(self,val):
        self.val = val
        self.next = None # the pointer initially points to nothing

class RevealJSPresentationGame(Game):
    def __init__(self, **kwargs):
        Game.__init__(self, kwargs)
        self.template = "reveal.html"
    def input(self, player, data, output_callback):
        node = data['node']
        graph = data['graph']
        question = get_question_from_digraph_node(graph, node)
        #assert(graph == self.question_digraph.graph['name'])
        #question = self.question_digraph.nodes[node]['_question_obj']
        question.build_form(data)
        if question.check_answer():
            output_callback({'correct': True, 'message': None, 'graph': graph, 'node': node})
        else:
            output_callback({'correct': False, 'message': None, 'graph': graph, 'node': node})


class QuestionDigraphGame(Game):
    def __init__(self, question_digraph, **kwargs):
        Game.__init__(self, kwargs)
        self.template = "memory.html"
        self.question_digraph = question_digraph
        self.active_node = question_digraph.graph['graph']['start']
        self.active_question = question_digraph.nodes[self.active_node]['_question_obj']
        self.scripts = self.active_question.scripts()

    def screen_html(self):
        print(self.active_question)
        self.active_question.build_form()
        return(self.active_question.render_html())

    def next(self):
        self.active_node = next(self.question_digraph.successors(self.active_node))
        self.active_question = self.question_digraph.nodes[self.active_node]['_question_obj']

    # FIXME: This input function is now broken. It does not respond in any sensible way. Need to clarify how this game works. Originally the output was to update the screen with the new question.
    def input(self, player, data, output_callback):
        self.active_question.build_form(data)
        if self.active_question.check_answer():
            self.next()
            self.screen_html()
            output_callback()

    def to_json(self):
        """Serialize object to JSON"""
        gamedata = Game.to_json(self)
        gamedata.update({
            "screen_html": self.screen_html(),
        })
        return(gamedata)

class QuestionGame(Game):
    def __init__(self, questions, **kwargs):
        Game.__init__(self, kwargs)
        self.questions = questions
        self.active_question = self.questions.head
        self.scripts = self.active_question.data.scripts()

    def screen_html(self):
        print(self)
        print(self.questions)
        print(self.questions.head)
        print(self.active_question)
        self.active_question.data.build_form()
        return(self.active_question.data.render_html())

    def input(self, player, data, update_game_callback):
        self.active_question.data.build_form(data)
        if self.active_question.data.check_answer():
            self.active_question = self.active_question.next
            self.screen_html()
            update_game_callback()

class RequestDenied(Exception):
    def __init__(self, message):
        self.message = message

def get_or_create(session, model, defaults=None, **kwargs):
    from sqlalchemy.sql.expression import ClauseElement
    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        params = dict((k, v) for k, v in kwargs.items() if not isinstance(v, ClauseElement))
        params.update(defaults or {})
        instance = model(**params)
        session.add(instance)
        return instance

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    firstname = db.Column(db.String(80), nullable=False)
    lastname = db.Column(db.String(80), nullable=False)
    lti_user_id = db.Column(db.String(255), unique=True, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username
    def to_json(self):
        return({ 'id': self.id,
                 'username': self.username,
                 'firstname': self.firstname,
                 'lastname': self.lastname,
                 'lti_user_id': self.lti_user_id })

class ListNode:
    """
    A node in a singly-linked list.
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return repr(self.data)


class SinglyLinkedList:
    def __init__(self):
        """
        Create a new singly-linked list.
        Takes O(1) time.
        """
        self.head = None

    def __repr__(self):
        """
        Return a string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        curr = self.head
        while curr:
            nodes.append(repr(curr))
            curr = curr.next
        return '[' + ', '.join(nodes) + ']'

    def prepend(self, data):
        """
        Insert a new element at the beginning of the list.
        Takes O(1) time.
        """
        self.head = ListNode(data=data, next=self.head)

    def append(self, data):
        """
        Insert a new element at the end of the list.
        Takes O(n) time.
        """
        if not self.head:
            self.head = ListNode(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = ListNode(data=data)

    def find(self, key):
        """
        Search for the first element with `data` matching
        `key`. Return the element or `None` if not found.
        Takes O(n) time.
        """
        curr = self.head
        while curr and curr.data != key:
            curr = curr.next
        return curr  # Will be None if not found

    def remove(self, key):
        """
        Remove the first occurrence of `key` in the list.
        Takes O(n) time.
        """
        # Find the element and keep a
        # reference to the element preceding it
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        # Unlink it from the list
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    def reverse(self):
        """
        Reverse the list in-place.
        Takes O(n) time.
        """
        curr = self.head
        prev_node = None
        next_node = None
        while curr:
            next_node = curr.next
            curr.next = prev_node
            prev_node = curr
            curr = next_node
        self.head = prev_node
