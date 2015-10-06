import random

firstScore = 0
secondScore = 0
x = 0


print "Welcome! Press 1 for Rock, 2 for Paper and 3 for Scissors"
player1 = raw_input("Player 1, what's your name? ")
print "Hello ", player1
player2 = raw_input("Player 2, what's your name? ")
print "Hello ", player2




decision1 = raw_input("Player 1: Rock, paper or scissors?").lower()
decision2 = raw_input("Player 2: Rock, paper or scissors?").lower()
for x in range(0,1):
    if (decision1 == "rock" and decision2 == "rock"):
        print "It's a tie!"
    elif(decision1 == "rock" and decision2 == "paper"):
        print "Player 2 wins!"
    elif (decision1 == "rock" and decision2 == "scissors"):
        print "Player 1 wins!"
    elif (decision1 == "rock" and decision2 == "lizard"):
        print "Player 1 wins!"
    elif (decision1 == "rock" and decision2 == "spock"):
        print "Player 2 wins!"
    elif (decision1 == "paper" and decision2 == "rock"):
        print "Player 1 wins!"
    elif (decision1 == "paper" and decision2 == "paper"):
        print "It's a tie!"
    elif (decision1 == "paper" and decision2 == "scissors"):
        print "Player 2 wins!"
    elif (decision1 == "paper" and decision2 == "lizard"):
        print "Player 2 wins!"
    elif (decision1 == "paper" and decision2 == "spock"):
        print "Player 1 wins!"
    elif (decision1 == "scissors" and decision2 == "rock"):
        print "Player 2 wins!"
    elif (decision1 == "scissors" and decision2 == "paper"):
        print "Player 1 wins!"
    elif (decision1 == "scissors" and decision2 == "scissors"):
        print "It's a tie!"
    elif (decision1 == "scissors" and decision2 == "lizard"):
        print "Player 1 wins!"
    elif (decision1 == "scissors" and decision2 == "spock"):
        print "Player 2 wins!"
    elif (decision1 == "lizard" and decision2 == "rock"):
        print "Player 2 wins!"
    elif (decision1 == "lizard" and decision2 == "paper"):
        print "Player 1 wins!"
    elif (decision1 == "lizard" and decision2 == "scissors"):
        print "Player 2 wins!"
    elif (decision1 == "lizard" and decision2 == "lizard"):
        print "It's a tie!"
    elif (decision1 == "lizard" and decision2 == "spock"):
        print "Player 1 wins!"
    elif (decision1 == "spock" and decision2 == "rock"):
        print "Player 1 wins!"
    elif (decision1 == "spock" and decision2 == "paper"):
        print "Player 2 wins!"
    elif (decision1 == "spock" and decision2 == "scissors"):
        print "Player 1 wins!"
    elif (decision1 == " spock" and decision2 == "lizard"):
        print "Player 2 wins!"
    elif (decision1 == "spock" and decision2 == "spock"):
        print "It's a tie!"
    else:
        print "You have entered an invalid answer, please try again"




    

