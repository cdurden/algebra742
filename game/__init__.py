"""Object for tracking game status"""
from datetime import datetime
import time
import random
import math
import string
import os

class RequestDenied(Exception):
    def __init__(self, message):
        self.message = message

# dictionaries
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DECKS_ROOT = os.path.join(APP_ROOT, 'decks')
#DICTIONARIES = {
#    "CAH" :         FILE_ROOT + "/cah_code_names.txt",
#    "Pop Culture" : FILE_ROOT + "/code_names_pop.txt",
#    "Standard" :    FILE_ROOT + "/code_names_dict.txt",
#    "Simple" :      FILE_ROOT + "/code_names_simple.txt",
#    "French" :      FILE_ROOT + "/code_names_french.txt",
#    "Portuguese" :  FILE_ROOT + "/code_names_portuguese.txt",
#    "German" :  FILE_ROOT + "/code_names_german.txt"
#}
# colors per team
RED = 'R'
BLUE = 'B'
GREEN = 'G'
# num words per board
BOARD_SIZE = {
    'normal': 25,
    'large': 81
}
BIG_BLACKOUT_SPOTS = [4, 20, 24, 36, 40, 44, 56, 60, 76]


class Card(object):
    def __init__(self, i, info=None, position=None):
        if type(i) != int:
            raise TypeError("card must be an integer. Got type {:s}.".format(type(i)))
        self.i = i
        self.info = info
        self.position = None
    def __eq__(self, other):
        return self.i == other.i
    def to_dict(self):
        return({ 
                'i': self.i,
                'info': self.info,
                'position': self.position,
                })

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
    def to_dict(self):
        return({ 
                'session_id': self.session_id,
                'user': self.user.to_dict(),
                'correct': self.correct,
                'incorrect': self.incorrect,
                'matched_cards': [card.to_dict() for card in self.matched_cards]),
                'color': self.color,
                })

class Game(object):
    # pylint: disable=too-many-instance-attributes
    """Object for tracking game stats"""
    def __init__(self, deck_name='clt1', size='normal', teams=2, wordbank=False, mix=False):
        self.active_player = 0
        self.flipped_cards = []
        #self.matched_cards = [[],[]]
        self.deck_name = deck_name
        self.matches = [x/2 for x in range(0,16)]
        #self.player_data = {} 
        self.players = []
        self.room = self.generate_room_id()
        self.date_created = datetime.now()
        self.date_modified = self.date_created
        self.__load_deck()
        random.shuffle(self.deck)
        for position,card in enumerate(self.deck):
            card.position = position
#
#        self.wordbank = wordbank
#        self.starting_color = RED
#        self.size = size
#        self.teams = teams
#        self.dictionary = dictionary
#        self.mix = mix
#        self.dictionaries = DICTIONARIES.keys()
#        self.minWords = BOARD_SIZE[self.size]

        # gererate board
        #self.generate_board()
    def matched_cards(self):
        matched_cards = []
        for player in self.players:
            matched_cards += player.matched_cards
        return(matched_cards)

    def get_player(self, session_id):
        for player in self.players:
            if player.session_id == session_id:
                return(player)
        return(None)

    def player_is_active(self, player):
        return(self.players[self.active_player] == player)

    def activate_next_player(self):
        self.active_player = (self.active_player+1)%len(self.players)

    def match_is_flipped(self):
        if len(set(self.flipped_cards)) != 2:
            return(False)
        else:
            print(self.flipped_cards[0]);
            print(self.flipped_cards[1]);
            return(self.matches[self.flipped_cards[0].i]==self.matches[self.flipped_cards[1].i])

    def input(self, player, data, update_game_callback):
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
                update_game_callback(self.room)
            else: # player is not active
                if self.match_is_flipped() == data_to_bool[data]:
                    player.correct += 1
                else:
                    player.incorrect += 1

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

    def __load_deck(self):
        with open(os.path.join(DECKS_ROOT,self.deck_name), 'r') as deck_file:
            self.deck = [Card(i,info=elem) for i,elem in enumerate(deck_file.read().split('\n')) if len(elem.strip()) > 0]

    # Not sure if anything below is necessary
    def to_json(self):
        """Serialize object to JSON"""
        return {
            "game_id": self.game_id,
            "starting_color": self.starting_color,
            "players": self.players,
            "date_created": str(self.date_created),
            "date_modified": str(self.date_modified),
            "playtime": self.__playtime(),
            "board": self.board,
            "solution": self.solution,
            "options": {
                "dictionary": self.dictionary,
                "size": self.size,
                "teams": self.teams,
                "mix": self.mix,
                "custom": self.wordbank
            },

        }

    def generate_board(self, newGame=False):
        """Generate a list of words"""
        # remove current words from bank if newGame and not shuffle
        if newGame and hasattr(self, 'words') and (self.wordbank and len(self.wordbank) - self.minWords >= self.minWords):
            for word in self.words:
                self.wordbank.remove(word)
        self.words = self.__get_words(self.size)
        self.layout = self.__get_layout(self.size, int(self.teams))
        self.board = dict.fromkeys(self.words, False)
        self.solution = dict(zip(self.words, self.layout))


    def __playtime(self):
        # 2018-08-12 10:12:25.700528
        fmt = '%Y-%m-%d %H:%M:%S'
        d1 = self.date_created
        d2 = self.date_modified
        # Convert to Unix timestamp
        d1_ts = time.mktime(d1.timetuple())
        d2_ts = time.mktime(d2.timetuple())

        return round(float(d2_ts-d1_ts) / 60, 2)


    def __get_words(self, size):
        """Generate a list of words"""
        if not self.dictionary in DICTIONARIES.keys():
            print("Error: dictionary '" + self.dictionary + "' doesn't exist")
            return None
        # override words with the wordbank
        words = self.wordbank
        if not self.wordbank:
            if self.mix:
                words = []
                for key in self.mix:
                    # load and shuffle current dict
                    tempWords = self.__load_words(key)
                    random.shuffle(tempWords)
                    # get word ratio (rounded up)
                    numWords = int(math.ceil((self.mix[key]/100.0)*BOARD_SIZE[size]))
                    words = words + tempWords[0:numWords]
            else:
                words = self.__load_words(self.dictionary)
        random.shuffle(words)
        final_words = words[0:BOARD_SIZE[size]]
        return final_words

    def __load_words(self, dict):
        words_file = open(DICTIONARIES[dict], 'r')
        return [elem for elem in words_file.read().split('\n') if len(elem.strip()) > 0]

    def __get_layout(self, size, teams):
        """Randomly generate a card layout"""
        size = BOARD_SIZE[size]
        self.starting_color = RED
        green = 0
        # normal board size
        if size == BOARD_SIZE['normal']:
            if teams == 3:
                blue = 5
                red = 5
                green = 5
            else:
                blue = 8
                red = 8

            bystanders = size - blue - red - green - 2
        # large board size
        else:
            if teams == 2:
                blue = 8
                red = 8
            elif teams == 3:
                blue = 8
                red = 8
                green = 8
            num_blackouts = 9
            bystanders = size - num_blackouts - blue - red - green - 3
        # if 2 teams, pick a starting team
        if teams == 2:
            if random.random() < 0.5:
                blue += 1
                self.starting_color = BLUE
            else:
                red += 1
        # if 3 teams, pick a starting team
        else:
            if random.random() < 0.333:
                blue += 1
                self.starting_color = BLUE
            elif random.random() > 0.666:
                green += 1
                self.starting_color = GREEN
            else:
                red += 1

        mix = ["B"] * blue
        mix.extend(["R"] * red)
        if green > 0:
            mix.extend(['G'] * green)
        mix.extend(["X"])
        if size == BOARD_SIZE['large']:
            mix.extend(['X'])
        mix.extend(["O"] * bystanders)
        random.shuffle(mix)
        if size == BOARD_SIZE['large']:
            for i in BIG_BLACKOUT_SPOTS:
                mix.insert(i, '-')
        return mix
