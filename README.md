# Introduction

For your final project, you and your partner(s) will be expanding upon the Blackjack example from the textbook.

# Overview

You will need to implement the base game from the example and the following features and requirements (the grade percentage for each feature is in parenthesis):

* Technical Requirements (5%)
* Base game (10%)
* Distributed multiplayer functionality (40%)
* Betting functionality (10%)
* Hand splitting functionality (20%)
* Double-down functionality (10%)
* Peer Review (5%)

# Instructions

## Setup

1. Pick a name for your group
2. Accept the assignment on GitHub Classroom
    1. The first person to accept the assignment will enter the name for the group
    2. Everyone else will just select the group to join
3. Clone the repository
4. Read all of the Instructions
5. Complete the project
6. Fill out the Peer Review

## Technical Requirements (5%)

1. Your code should follow the basic Python conventions
2. Each file should have a **docstring** including:
    1. The filename
    2. Author
    3. Purpose
3. Each class should have a **docstring** including:
    1. Purpose
    2. Instance Variables (especially if they use other classes)
4. Each function should have a **docstring** describing:
    1. Purpose
    2. Parameters and Instance Variables used
    3. Return values (if any)


## Base Game (15%)

Implement the base Blackjack game in a similar fashion to the example in the textbook.

* The goal is to obtain cards whose total is as close to but still less than 21
    * Face cards count as 10
    * Aces can count as either 1 or 11
    * All other cards have their number value
* All Players and the Dealer are dealt two cards from the same deck
* Only one card in the Dealer's hand is visible to the Players
    * All other cards are visible to all Players
* Players "hit" to add a card from the deck to their hand or "stay" to end the round
* If the Deck runs out of Cards, a new Deck is shuffled, and the game continues
* If their total is less than 21, they may "hit" again or "stay"
* If they go over 21, they "bust" and automatically lose
* Once all Players have "stayed" or "bust", the Dealer reveals their cards and must "hit" until they have at least 17 
* If the Dealer "busts", all Players who have not also "bust" win
* If a Player has a higher total than the Dealer, they win
* If a Player ties with the Dealer, they neither win or lose
* If a Player has less that the Dealer, they lose
* If the Dealer has a Blackjack, a Player must also have a Blackjack to tie, otherwise they lose
    * A Blackjack is having a total of 21 with the first two Cards. (i.e. a 10 or above and an Ace)
* If the Player has a Blackjack, the Dealer must also have a Blackjack to tie, otherwise the Player wins

### Student Learning Outcomes

* Demonstrate an ability to implement classes with a given interface using Python

## Distributed Multiplayer Functionality (40%)

This version of Blackjack will be played over a network with a central Server and multiple Clients.

* A central Server application will manage all gameplay
* Players issue commands to the Server through the Client
* All Players are dealt cards from the same Deck
* When a new Client connects, if the round is not over, the Server deals in a new Player
* Players may issue commands to the Server in any order
    * e.g. two Players may decide to "hit" at the same time
* All Players' hands are visible to all Clients
    * Any updates are sent to all Clients
    * e.g. When one Player "hits" all Players can see the dealt Card
* Once all Players have "stayed" or "bust", the round is over and the Dealer has their turn
    * Once the Dealer finishes its turn and the scores are counted, a new round begins, and the Players are asked if they want to continue
    * New Clients can connect during the Dealer's turn, but Players are not dealt cards until the next round begins

### Student Learning Outcomes

* Demonstrate an ability to create a distributed application over a network with multiple concurrent clients using Python

## Betting Functionality (10%)

Players start the game with a certain number of Chips. At the beginning of a round, Players bet a certain number of Chips.

* If a Player "busts" or loses to the Dealer, they lose their bet
    * e.g. If a Player has 100 chips, bets 10 chips at the beginning of the round and loses, they will have 90 chips at the end of the round
* If the Player wins, they receive double their bet back
    * e.g. If a Player has 100 chips, bets 10 chips at the beginning of the round and wins, they will have 110 chips at the end of the round
* If the Player has a Blackjack and wins, they receive 2.25 times their bet (rounded down) back
    * e.g. If a Player has 100 chips, bets 10 chips, gets a Blackjack and wins, they will have 112 chips at the end of the round
* If the Player and the Dealer tie, they Player receives just their bet back
    * e.g. If a Player has 100 chips, bets 10 chips at the beginning of the round and ties, they will have 100 chips at the end of the round

### Student Learning Outcomes

* Demonstrate an ability to create and maintain multiple concurrent user states using Python
    * e.g. Handling multiple bank accounts concurrently in the same application

## Hand Splitting Functionality (20%)

When a Player has an opening hand with two cards of the same rank, they may "split" the hand and play two hands.

* e.g. If the Player is dealt the 8 of Clubs and the 8 of Spades, the Player may decide to "split". Two new hands are created, one with the 8 of Clubs and a new Card and one with the 8 of Spades and a new Card
* Gameplay: 
    * The two new hands are played separately
    * Each hand can win or lose like normal
    * The Player should play one hand until they "stay" or "bust" before moving on to the other hand
    * If necessary, the Player can "split" the new hands as well
* Betting:
    * Each new hand requires an additional, matching bet
    * e.g. If a Player bets 10 chips on the opening hand, then decides to "split", they must be able to bet an additional 10 chips for the new hand

### Student Learning Outcomes

* Demonstrate an ability to refactor, design, and implement new classes using Python
* Demonstrate an ability to transition between different states in an application

## Double-Down Functionality (10%)

On their opening hand, a Player may choose to "double-down". They double their initial bet and receive only one more card.

* e.g. If a Player bets 10 chips on the opening hand, then decides to "double-down", they double their bet to 20 chips and receive only one card.
* A Player may only "double-down" on their opening hand
    * i.e. A Player may not "double-down" after a "hit"

### Student Learning Outcomes

* Demonstrate an ability to transition between different states in an application

## Peer Review (5%)

Complete the Peer Review in Canvas. Be sure to read the instructions carefully and evaluate both yourself and your teammate(s).

### Student Learning Outcomes

* Demonstrate an ability to collaborate and problem-solve with others on a team

# Final Notes

How you decide to implement the requirements is up to you. Here are some useful tips.

* The examples from Units 9 and 10 will be helpful, but you will still have to heavily modify them
* Keep your functions and methods short and simple with clear inputs and outputs
    * If you have long functions, see if you can break them up into smaller simpler functions
* Classes can be a double-edged sword. They can help you organize and reuse your code, but they also make your code more complex

As usual, let me know if you have any questions.