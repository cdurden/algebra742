from . import app
APP_ROOT = os.path.dirname(os.path.abspath(__file__))
DECKS_ROOT = os.path.join(APP_ROOT, 'decks')

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
                'matched_cards': map(lambda card: card.to_dict(), self.matched_cards),
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
        self.matches = map(lambda x: x/2, range(0,16))
        #self.player_data = {} 
        self.players = []
        self.room = self.generate_room_id()
        self.date_created = datetime.now()
        self.date_modified = self.date_created
        #self.__load_deck()
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

#    def __load_deck(self):
#        with open(os.path.join(DECKS_ROOT,self.deck_name), 'r') as deck_file:
#            self.deck = [Card(i,info=elem) for i,elem in enumerate(deck_file.read().split('\n')) if len(elem.strip()) > 0]

    # Not sure if anything below is necessary
    def to_dict(self):
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
class RequestDenied(Exception):
    def __init__(self, message):
        self.message = message

