import random

class GameStart:
    def __init__ (self):
        self.would_you_like_to_play = None
        self.what_is_players_name = None
        self.how_many_decks = None

    def play_prompt(self):
        self.would_you_like_to_play = input("Would you like to play High and Low? y/n: ")

        if self.would_you_like_to_play.lower() not in ("y", "n"):
            self.play_prompt()
        else:
            self.what_is_players_name = input("What is your name?: ")

    def deck_prompt(self):
        self.deck_prompt = int(input("How many decks do you want to use? 1-4:"))
        if 1 <= self.deck_prompt <= 4:
            pass
        else:
            self.deck_prompt()

    def start_game(self):
        self.play_prompt()
        self.deck_prompt()
        # print(self.would_you_like_to_play, self.what_is_players_name, self.how_many_decks)


# this is a blueprint for making cards. in the parenthesis we have defined what attributes from the blueprint
# that we want each card object to have.
class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    

class Deck:
    def __init__(self):
        self.card_suit_dictionary = {
            "Clubs": 1,
            "Diamonds": 2,
            "Hearts": 3,
            "Spades": 4
            }
        self.card_value_dictionary = {
            "2": 2, 
            "3": 3, 
            "4": 4,
            "5": 5,
            "6": 6,
            "7": 7,
            "8": 8,
            "9": 9,
            "10": 10,
            "J": 11,
            "Q": 12,
            "K": 13,
            "A": 14
        }

        self.cards = []

    def card_generator(self):
        temp_cards = []
        for suit in self.card_suit_dictionary:
            # print(f'In loop: suit: {suit}')
            for value in self.card_value_dictionary:
                temp_cards.append(Card(suit, value))
        self.cards = temp_cards

    def multiply_shuffle_deck(self):
        
        multiplied_deck = self.cards * game.deck_prompt
        random.shuffle(multiplied_deck)
        self.cards = multiplied_deck
        for card in self.cards:
            print(f'CARD: {card.value} {card.suit}')



class Player:
    def __init__(self):
        self.name = game.what_is_players_name
        self.hand = []
        self.wins = 0
        self.ties = 0
        self.losses = 0


class Dealer:
    def __init__(self):
        self.name = "Dealer"
        self.hand = []
        self.wins = 0
        self.ties = 0
        self.losses = 0
        

game = GameStart()
game.start_game()


deck = Deck()
deck.card_generator()
deck.multiply_shuffle_deck()



the_player = Player()
the_dealer = Dealer()
print(f"player: {the_player.name} {deck.cards[0].value} {deck.cards[0].suit}")
print(f"dealer: {the_dealer.name} {deck.cards[1].value} {deck.cards[1].suit}")

# win conditions.
def player_win():
    print(f"{the_player.name} wins")
    the_player.wins = the_player.wins + 1
    the_dealer.losses = the_dealer.losses + 1
    deck.cards = deck.cards[2:]

def dealer_win():
    print(f"{the_dealer.name} wins")
    the_dealer.wins = the_dealer.wins + 1
    the_player.losses = the_player.losses + 1
    deck.cards = deck.cards[2:]

def tie_condition():
    print(f"{the_player.name} and {the_dealer.name} tie!")
    the_dealer.ties = the_dealer.ties + 1
    the_player.ties = the_player.ties + 1
    deck.cards = deck.cards[2:]

def card_draw():
    if deck.cards[0].value > deck.cards[1].value:
        player_win()
        
    elif deck.cards[1].value > deck.cards[0].value:
        dealer_win()
        
    elif deck.cards[0].value == deck.cards[1].value:
        if deck.cards[0].suit == deck.cards[1].suit:
            tie_condition()
        elif deck.cards[0].suit > deck.cards[1].suit:
            player_win()
        elif deck.cards[0].suit < deck.cards[1].suit:
            dealer_win()
    

        
        
card_draw()

print(f"{the_player.name} has: {the_player.wins} wins, {the_player.losses} losses, {the_player.ties} ties.")
print(f"{the_dealer.name} has: {the_dealer.wins} wins, {the_dealer.losses} losses, {the_dealer.ties} ties.")
print(f'Cards left: {len(deck.cards)} \n')