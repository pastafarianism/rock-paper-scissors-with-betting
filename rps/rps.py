
#currently needs betting to be chosen by the user, also needs a huge buildup through some sort of animation (dotmatrix library, perhaps?)

#also theres a bug where if you lose at the same time that you make a bad input it shows the bad input message like 1000x per second. crazy stuff

import time
import random
import os

startOver = 1
pot = 110
fee = 10
wins = 0
losses = 0
stalemates = 0
gameIsActive = 2+2 != 5
print("ROCK PAPER SCISSORS WITH BETTING :)")
print(" ")
print("RULES:")
print("1. Wins double your earnings.")
print("2. Losses halve your earnings.")
print("3. You pay 10 credits every time you wish to play.")
print("4. No playing without paying.")
print("5. Type end to stop playing, if you want to. But why would you want to? :)")
print(" ")
print("Have fun, and play responsibly!")

while gameIsActive:
 
  while startOver == 1 and pot > 10:
    print(" ")
    pot = pot - fee
    print("Your wallet: " + str(pot))
    print("Your wins: " + str(wins))
    print("Your losses: " + str(losses))
    print("Your stalemates: " + str(stalemates))
    hand = input("Rock, paper, scissors! ").lower()

    startOver = 0
    ai = random.randint(1,3)

  while pot < 10:
    print("Sorry bucko, but you don't have enough to play. Better luck next time!")
    print(" ")
    print("\ GAME OVER /")
    print("Your final wallet: " + str(pot))
    print("Your final wins: " + str(wins))
    print("Your final losses: " + str(losses))
    print("Your final stalemates: " + str(stalemates))
    exit()
 
  if hand == "rock":
    hand = 1
    announce2 = "Rock"
  elif hand == "paper":
    hand = 2
    announce2 = "Paper"
  elif hand == "scissors":
    hand = 3
    announce2 = "Scissors"
  elif hand == "end":
    print("You have manually chosen to end the game. Goodbye!")
    print(" ")
    print("\ GAME OVER /")
    print("Your final wallet: " + str(pot))
    print("Your final wins: " + str(wins))
    print("Your final losses: " + str(losses))
    print("Your final stalemates: " + str(stalemates))
    exit()
  else:
    fee = 5
    startOver = 1
    print("Sorry, the only options are rock, paper, and scissors. Play the game, bucko.")
  if ai == 1:
    announce = "Rock"
  elif ai == 2:
    announce = "Paper"
  elif ai == 3:
    announce = "Scissors"
 
  if hand == ai:
    print(" ")
    print("Stalemate!")
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    pot = pot*1
    fee = 0
    stalemates = stalemates + 1
    print(" ")
    startOver = 1
 
  if hand == 1 and ai == 2: #Rock vs paper
    print(" ")
    print("Lost!")
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    fee = 10
    startOver = 1
    pot = pot*0.5
    losses = losses + 1
    print(" ")

  if hand == 1 and ai == 3: #Rock vs scissors
    print(" ")
    print("Won!")
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    fee = 10
    startOver = 1
    print(" ")
    pot = pot*2
    wins = wins + 1

  if hand == 2 and ai == 1: #Paper vs rock
    print(" ")
    print("Won!")
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    fee = 10
    startOver = 1
    print(" ")
    pot = pot*2
    wins = wins + 1

  if hand == 2 and ai == 3: #Paper vs scissors
    print(" ")
    print("Lost!")  
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    fee = 10
    startOver = 1
    print(" ")
    pot = pot*0.5
    losses = losses + 1

  if hand == 3 and ai == 1: #Scissors vs rock
    print(" ")
    print("Lost!")
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    fee = 10
    startOver = 1
    pot = pot*0.5
    print(" ")
    losses = losses + 1

  if hand == 3 and ai == 2: #Scissors vs paper
    print(" ")
    print("Won!")
    print("Matchup: " + announce2 + " (YOU) vs " + announce + (" (AI)"))
    fee = 10
    startOver = 1
    pot = pot*2
    print(" ")
    wins = wins + 1 