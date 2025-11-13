"""
Filename: player.py
Author: Jacob Miller
Purpose: Creates the player and what they are
         able to do."""

from card import Card

class Player(Card):
    """
    This is the class for each player. The clients playing have a player object that has
    cards and money.
    The player also has a done variable to determine if they are finished with their hand before the dealer hits."""
    def __init__(self, cards=[], money=100):
        """
        Create the player
            Instance Variables:
                self.cards: the cards that the player has"""
        self.cards = cards
        self.done = False
        self.playAgain = False
        self.money = money

    def __str__(self):
        """
        Show the player what their current hand is along with
        their current points
        Instance Variable:
            result: stores players hand and points
        returns result"""
        result = ""
        for c in self.cards:
            result += str(c) + " "
        result += "\n" + str(self.getPoints())
        return result

    def hit(self, card):
        """
        Draw a card from the deck and add it to
        the players hand."""
        self.cards.append(card)

    def getPoints(self):
        """
        Returns the amount of points the players cards add up to
        Instance Variables:
            score: set equal to 0 each time the function is called
        returns: score"""
        score = 0
        for c in self.cards:
            if c.rank > 9:
                score += 10
            elif c.rank == 1:
                score += 11
            else:
                score += c.rank
        for c in self.cards:
            if score > 21:
                if c.rank == 1:
                    score -= 10
        return score

    def hasBlackJack(self):
        """
        Returns True if there are only 2 cards in the players hand 
        and they equal 21, the player has blackjack.
        """
        return (len(self.cards) == 2 and self.getPoints() == 21)
    
    def clearHand(self):
        """Clears the players hand for the next round."""
        self.cards.clear()

    def getIsDone(self):
        """
        Returns the value of if they player is done."""
        return self.done

    def setIsDone(self):
        """
        Turns the done condition to True once they have finished their turn."""
        self.done = True
    
    def reset(self):
        """
        Change player's playAgain and done statuses back to False."""
        self.playAgain = False

        self.done = False
