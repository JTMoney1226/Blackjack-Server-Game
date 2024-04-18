"""
Filename: client_handler.py
Author: Xander Stephens
Creates the client handler for multiple clients on the server
Also plays the blackjack game and acts as the dealer for the players.
"""

from codecs import decode
from threading import Thread

CODE = "ascii"
BUFSIZE = 1024

class ClientHandler(Thread):
    """
    Creates the client handler for the server
    Instance Variables:
        self.client: set equal to client from the server"""
    def __init__(self, client, game):
        """
        Client handler creates the game object from a shared object. Created and stores player object 
        and client object."""
        Thread.__init__(self)
        self.client = client
        self.game = game
        self.player = self.game.createPlayer()

    def play(self, bet):
        """Begin the game and get input from the player.
           Handle input for the game and prints the winner/loser.
           passes in the players bet."""
        self.bet = bet
        self.sendMssg("\n" * 100 + "This is your hand: " + self.player.__str__() + "\n\nThis is the dealer's hand: " 
                      + self.game.dealer.__str__() + "\nWould you like to double down? Y/N")
        double = self.recvMssg()
        if double in ("Y", "y"):
            self.doubleDown()
        else:
            self.sendMssg("\nWould you like to hit? Y/N")
            self.hits()
        self.player.setIsDone() 
        self.sendMssg("Waiting on server")
        while True:
            if self.game.isRoundOver():
                break
        self.sendMssg(self.gameResult() + "\nWould you like to play again? Y/N" )

    def doubleDown(self):
        """
        Doubles the bet of the player, adds a card to their hand, and makes them stay."""
        self.player.hit(self.game.deck.deal())
        self.bet *= 2

    def hits(self):
        """
        Deals one more card from the dealer and adds it to your hand."""
        while True:
            hit = self.recvMssg()
            if hit in ("Y", "y"):
                self.player.hit(self.game.deck.deal())
            else:
                break
            if self.player.getPoints() > 21:
                break
            else:
                self.sendMssg(str(self.player) + "\n" + str(self.game) + "\nWould you like to hit? Y/N")   

    def gameResult(self):
        """
        Once the player stops hitting, or busts, this determines the game result."""
        self.game.dealer.hit(self.game.deck)

        if self.player.hasBlackJack():
            #Player has blackjack and wins
            self.player.money += self.bet * 2.25
            self.player.money += 20
            outcome = "You have blackjack, and beat the dealer!\nYou had: " + str(self.player) + " points!\nThe dealer had " \
                + str(self.game.dealer) + " points.\nYou have $" + str(self.player.money) + " left."
            
        elif self.player.getPoints() == self.game.dealer.getPoints():
            #This is if the player and dealer tie. The dealer still wins but the player doesn't lose their bet.
            outcome = "The dealer won with " + str(self.game.dealer) + " points.\nYou had " + \
                str(self.player) + " points.\nYou have $" + str(self.player.money) + " left."
            
        elif self.game.dealer.getPoints() > 21 and self.player.getPoints() <= 21:
            #Player wins when they don't bust but the dealer does.
            self.player.money += self.bet * 2
            self.player.money += 20
            outcome = "You had the winning hand with " + str(self.player) + " points!\nThe dealer bust with " \
                + str(self.game.dealer) + " points.\nYou have $" + str(self.player.money) + " left."
                            
        elif self.player.getPoints() <= 21 and self.player.getPoints() > self.game.dealer.getPoints():
            #Player beats the dealer and does not bust
            self.player.money += self.bet * 2
            self.player.money += 20
            outcome = "You had the winning hand with " + str(self.player) + " points!\nThe dealer had " \
                + str(self.game.dealer) + " points.\nYou have $" + str(self.player.money) + " left."
            
        elif self.player.getPoints() > 21:
            #Player busts, the dealer automatically wins
            self.player.money -= self.bet
            outcome = "The dealer won with " + str(self.game.dealer) + " points.\nYou bust with " \
                + str(self.player) + " points.\nYou have $" + str(self.player.money) + " left."
            
        else:
            #The dealer had more points than you even though you didn't bust.
            self.player.money -= self.bet
            outcome = "The dealer won with " + str(self.game.dealer) + " points.\nYou had " + \
                str(self.player) + " points.\n You have " + str(self.player.money) + " left." 
        return outcome
        

    def run(self):
        """
        Does the work for the server."""
        while True:
            if self.player.money < 0:
                self.client.close()
                break
            self.sendMssg("You have $" + str(self.player.money) +  \
                          ". You must keep a positive balance to stay in the game. If you don't you will be diconnected. How much would you like to bet this round? ")
            bet = int(self.recvMssg())
            while bet > self.player.money:
                self.sendMssg("Invalid bet. How many would you like to bet this round?")
                bet = int(self.recvMssg())
                if bet < self.player.money:
                    break
            self.play(bet)
            reply = self.recvMssg()
            if reply not in ("y", "Y"):
                break
            self.game.reset(self.player)
        self.client.close()

    def sendMssg(self, message):
        """
        Method to send a message to the client.
        Instance Variables:
            message: the message to be sent to the client."""
        self.client.send(bytes(str(message), CODE))

    def recvMssg(self):
        """
        Reveives a message from the client and returns it."""
        return decode(self.client.recv(BUFSIZE), CODE)