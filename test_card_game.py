from card_game import Deck
import random

def test_multiply_shuffle_deck():
    test_deck = Deck()
    test_deck.card_generator()
    expected_length = len(test_deck.cards) * 2
    expected_suit_counts = {suit: 0 for suit in test_deck.card_suit_dictionary}

    game = MockGame()
    game.deck_prompt = 2
    test_deck.multiply_shuffle_deck()

    assert len(test_deck.cards) == expected_length

    for card in test_deck.cards:
        expected_suit_counts[card.suit] += 1
    for suit, count in expected_suit_counts.items():
        assert count == len(test_deck.cards) // len(test_deck.card_suit_dictionary)

    class MockGame:
        def __init__(self):
            self.deck_prompt = 0