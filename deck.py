"""
Filename: deck.py
Author: Xander Stephens
Purpose: Assemble the cards into a deck to play from"""

from card import Card
import random

class Deck(Card):
    """
    This is the class that contains the card objects. The cards will be added to the class
    to make the deck."""
    def __init__(self):
        """
        Create deck of cards class by calling the constants
        from Card and setting them to suit and rank, then
        passing them into the Card constructor.
        Instance Variables:
            self.cards: list of cards in the deck
           """
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.cards.append(Card(rank,suit))

    def __str__(self):
        """
        Print the deck of cards into the instance variable
        named: result
        Returns: result"""
        result = ""
        for c in self.cards:
            result += str(c) + "\n"
        return result           

    def deal(self):
        """
        Return one card from the top of the deck, 
        and remove it from the list.
        If the deck length is less than 0,
        then it returns none."""
        if len(self) > 0:
            return self.cards.pop(0)
        else:
            return None

    def shuffle(self):
        """Shuffle the list of cards"""
        random.shuffle(self.cards)

    def __len__(self):
        """Return the length of the deck of cards"""
        return len(self.cards)