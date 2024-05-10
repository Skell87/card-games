
# def play_prompt():
#     would_you_like_to_play = input("Would you like to play High and Low? y/n: ")

#     if would_you_like_to_play.lower() not in ("y", "n"):
#         play_prompt()
#     else:
#         what_is_players_name = input("What is your name young lad or lass?: ")
#         return would_you_like_to_play, what_is_players_name
        
# def deck_prompt():
#             how_many_decks = input("How many decks would you like to use? 1-4: ")
#             if 1<= int(how_many_decks) <= 4:
#                 return how_many_decks
#                 pass
#             else:
#                 deck_prompt()
# play_prompt()
# deck_prompt()
# print(would_you_like_to_play, what_is_players_name, how_many_decks)
        # in oop objects can be like real world objects such as a deck of cards.

# in order to make an object, we need to make a class. 
#classes can function as a blueprint that will describe what methods and attributes our object will have
# attributes: what it is or has ex: name, height, age
# methods: what an object can do ex: run, jump etc.

# what does a deck have and what does it do?
class Card:
    def __init__(self, number_value, suit):
     #has:
        self.number_value = number_value
        self.suit = suit
    
    pass
     #does:
     # its compared against
        #its drawn, when drawn it will belong to a player or dealer. so who its going to.
   


#maybe have the cards here and a function to loop through one at a time.
# we have a dictionary { key: value } where key is card number and value is card value
        # we could instantiate each card in a loop ex: card = Card(10, "heart")
        # make a nested loop to eventually make an list(its really an array) of cards.
        #shuffle it (google)

        # make list of suits
        # make a dictionary or a list of numbers
        #empty list to push card objects on to as we build them
        # nested loop first loop through suit, then through "numbers"
        # append to empty list ^ a new card object card(value, suit)
        #then shuffle
        # then assign a list of cards to self. cards.
         

class Deck:
    def __init__ (self):
        
        # self.cards = cards {
        #     key:value
        # }
        # [{ number_value, suit }]
        self.card_suit_list = ["Clubs", "Diamonds", "Hearts", "Spades"]
        self.card_value_dictionary = {}
    pass

    



class Player:
    #has:
    hands = None
    #does:
    pass

#function pull deck info, pull hand info, do code, for game.