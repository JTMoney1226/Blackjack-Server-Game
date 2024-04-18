"""
Filename: dealer.py
Author: Xander Stephens
Purpose: Create the dealer class, which is 
         a child class of Player"""

from player import Player

class Dealer(Player):
    """
    This is the class for the dealer. The dealer is an object that has
    cards
    """
    def __init__(self, cards=[]):
        Player.__init__(self, cards)
        """
        Is a player and has the same features of the player
        Also has the list of cards
        Instance Variables:
            self.showOneCard: shows one card from the
                              dealers hand
            """
        self.showOneCard = True

    def __str__(self):
        """Override the player method and show the dealer cards"""
        result = ""
        if self.showOneCard:
            result += str(self.cards[0])
        else:
            result += Player.__str__(self)
        return result

    def hit(self, deck):
        """Have the dealer hit until they reach 17 at the minimum"""
        self.showOneCard = False
        while self.getPoints() < 17:
            self.cards.append(deck.deal())

    def clearHand(self):
        """Clears the dealers hand for the next round"""
        self.cards.clear()