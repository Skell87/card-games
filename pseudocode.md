<!-- 

run...
    "do you want to play high and low? y/n"
        prompt.lower
        if player enters ! y or n:
            prompt again.
        prompt the player to play the game, only accepts a y or n response, accounts for capital and lower
    "ask for player name"
    !!!THIS IS DONE!!!
        

    "how many decks would you like to use? 1-4"
        prompt player for number input to decide how many decks to use in the game. 
        this should be a variable that then gets plugged into the generated list to multiply it. for example...
        3 decks.
        var deck_multiplyer = (prompt input 3)
        card deck = generated card list * 3
        !!!THIS IS DONE!!!

    at this point we have 2 instanciated players
    one is a dealer and one is the player with their name.
    we also have an instanced deck with cards populated.

    now. 
    the players need to draw a card from the top of the deck
        when right after player instantiation
        how
    the cards they each draw must be compared by value
        when 
        how
    a win/lose/draw counter needs to go up by one.
        when 
        how
    prompt to play again
        when
        how: prompt, if Y then execute from beginning, elif N then break.

    
    game starts. player is dealt a card, dealer is dealt a card.
        program should have a list of suits and a dictionary of card values.
        go over each and join them together in a new list
        then multiply that list by the number of decks a player wants to play with.
        then it should pull one "card" off of the list for the dealer and for the player 
        then it should compare the values of each to declare winner.
            highest value wins unless tie.
                if dealer card is > player card
                    dealer wins
                    add 1 to dealer victory count
                elif player card is > dealer card
                    player wins
                    add 1 to dealer victory count
                else tie.
        after winner is declared it should 
        then it should prompt to play again and pull one card for each.
        when the list is empty prompt for a reshuffle and reshuffle the cards back into the list.
    program checks value of dealers card vs players card and declares winner.
    program asks "would you like to play again?"

 -->