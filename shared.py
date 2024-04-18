"""
Filename: shared.py
Author: Xander Stephens
Purpose: File of all shared objects in the game"""

from player import Player
from dealer import Dealer
from deck import Deck

class SharedCell:
    """
    Shares objects between all of things in the game."""
    def __init__(self, clients):
            """
            Creates all of the objects that are shared between clients."""
            self.deck = Deck()
            self.deck.shuffle()
            self.players = []
            self.dealer = Dealer([self.deck.deal(), self.deck.deal()])
            self.clients = clients

    def __str__(self):
        """
        Tells all the players in the game the current hand of all players."""
        state = ""
        num = 1
        for player in self.players:
            state += "Player " + str(num) + ":\n" + str(player) + "\n"
            num += 1
        return state

    def createPlayer(self):
        """
        Creates a player for each connected client."""
        player = Player([self.deck.deal(), self.deck.deal()])
        self.players.append(player)
        return player
    
    def reset(self, player):
        """
        Function for resetting the hand for another round.
        Passes in the player object to reset their cards."""
        self.deck = Deck()
        self.deck.shuffle()
        player.clearHand()
        self.dealer.clearHand()
        player.hit(self.deck.deal())
        player.hit(self.deck.deal())
        self.dealer.cards.append(self.deck.deal())
        player.reset()

    def isRoundOver(self):
        """
        Check if all of the players in the game are done. If they are all done, 
        it returns True, else it returns False.
        Instance Variables:
            done: A list of True or False based on if the player is done
        Returns True if ALL players are finished or False if there are unfinished players."""
        done = []
        for self.player in self.players:
            done.append(self.player.getIsDone())
        if False in done:
            return False
        else:
            return True
            
    def getDealerHand(self):
        """
        Gets the dealers hand to return it to the client handler."""
        return self.dealer.__str__()
    
    def playAgain(self):
        """
        Checks if each player is finished and returns True if they are and False if they aren't."""
        done = []
        for self.player in self.players:
            done.append(self.player.getPlayAgain())
        if False in done:
            return False
        else:
            return True