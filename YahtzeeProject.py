##
# The purpose of this program is to display a simulated game of Yahtzee between
# a human player and a computer player, and to tally the score throughout it
# @Christie Ralston

# Define constants for two of a kind and yahtzee
TWO_OF_A_KIND_SCORE = 20
YAHTZEE_SCORE = 50

# Import the randint function
from random import randint

# Set the initial human and computer scores to zero
humanTotalScore = 0
compTotalScore = 0

# Begin the program with a user response of Y
userResponse = "Y"

while userResponse == "Y" :

    # Define the variables for the human player's dice and the computer's dice
    humanDieOne = randint(1,6)
    humanDieTwo = randint(1,6)
    humanDieThree = randint(1,6)
    compDieOne = randint(1,6)
    compDieTwo = randint(1,6)
    compDieThree = randint(1,6)

    # Display the human player's first three rolls
    print("Player rolls: %d, %d, %d" % (humanDieOne, humanDieTwo, humanDieThree))

    # Calculate the human player's turn score
    if humanDieOne == humanDieTwo and humanDieTwo == humanDieThree :
        humanTurnScore = YAHTZEE_SCORE
        print("Yahtzee! (+%d)" % turnScore)
    elif humanDieOne == humanDieTwo or humanDieOne == humanDieThree or humanDieTwo == humanDieThree :
        humanTurnScore = TWO_OF_A_KIND_SCORE
        print("Two of a Kind! (+%d)" % humanTurnScore)
    else :
        humanTurnScore = (humanDieOne + humanDieTwo + humanDieThree)
        print("Chance! (+%d)" % humanTurnScore)
    
    # Display the computer player's first three rolls
    print("Computer rolls: %d, %d, %d" % (compDieOne, compDieTwo, compDieThree))

    # Calculate the computer player's turn score
    if compDieOne == compDieTwo and compDieTwo == compDieThree :
        compTurnScore = YAHTZEE_SCORE
        print("Yahtzee! (+%d)" % compTurnScore)
    elif compDieOne == compDieTwo or compDieOne == compDieThree or compDieTwo == compDieThree :
        compTurnScore = TWO_OF_A_KIND_SCORE
        print("Two of a Kind! (+%d)" % compTurnScore)
    else :
        compTurnScore = compDieOne + compDieTwo + compDieThree
        print("Chance! (+%d)" % compTurnScore)

    # Tally the total running score for the human and computer players
    humanTotalScore = humanTotalScore + humanTurnScore
    compTotalScore = compTotalScore + compTurnScore

    # Display the total running score for the human and computer players
    print("")   
    print("=============================")
    print("Player total points: %d" % humanTotalScore)
    print("Computer total points: %d" % compTotalScore)
    print("=============================")
    print("")   

    # Ask the player if they would would like to play again
    userInput = input("Roll again (Y or N)? ")
    userResponse = userInput.upper()