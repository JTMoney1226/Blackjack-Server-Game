"""
Filename: card.py
Author: Jacob Miller
Purpose: Create the card class for the blackjack game"""

class Card:
    """
    Card class that will be the deck for the game.
    Instance Variabels:
        RANKS: The possible numbers the cards could have
        SUITS: The different card suits the card can have"""
    RANKS = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
    SUITS = ("Clubs", "Diamonds", "Spades", "Hearts")

    def __init__(self, rank, suit):
        """
        Sets the rank and suit of the card to an instance
            variable named self.rank and self.suit.
        Parameters:
            rank and suit are passed in.
        Instance Variables
            self.rank: int with the card rank
            self.suit: str with the card suit"""
        self.rank = rank
        self.suit = suit

    def __str__(self):
        """
        Print the rank and suit of the cards
        Returns the word form of the card
        Ex: 6 of Hearts, or King of Spades"""
        rank = ""
        if self.rank == 1:
            rank = "Ace"
        elif self.rank == 11:
            rank = "Jack"
        elif self.rank == 12:
            rank = "Queen"
        elif self.rank == 13:
            rank = "King"
        else:
            rank = str(self.rank)

        return rank + " of " + self.suit
