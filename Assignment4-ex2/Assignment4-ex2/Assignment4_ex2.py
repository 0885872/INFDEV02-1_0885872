import random

firstScore = 0
secondScore = 0
x = 0

def intro():
    print "Welcome! Press 1 for Rock, 2 for Paper and 3 for Scissors"
    player1 = raw_input("Player 1, what's your name? ")
    print "Hello ", player1
    player2 = raw_input("Player 2, what's your name? ")
    print "Hello ", player2
    playGame()

def playGame():
    first = int(raw_input("Player 1, press 1(Rock), 2(Paper) of 3(Scissors) "))
    second = int(raw_input("Player 2, press 1(Rock), 2(Paper) of 3(Scissors) "))
    winCheck()
    
    for x < 1
    if (first == 1 & second == 2):
        secondScore = secondScore + 1
        print "First has rock, second has paper. Second wins!"
    elif (first == 1 & second == 3):
        firstScore = firstScore + 1
        print "First has Rock, second has Scissors. First wins!"
    elif (first == 2 & second == 1):
        firstScore = firstScore + 1
        print "First has paper, second has rock. First wins!"
    elif (first == 2 & second == 1):
        firstScore = firstScore + 1
        print "First has paper, second has rock. First wins!"
    
    



    

