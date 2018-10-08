##
# The purpose of this program is to prompt a player to guess a number until
# they answer correctly, and then to display the number of attempts it took
# to guess the answer
# @Christie Ralston

# Initialize the constant of ANSWER
ANSWER = 8

# Initialize the variable of userGuess to be outside of 1 and 10
userGuess = 11

# Initialize a counter to start at 1
count = 0

# Establish a loop to continue until the user guesses the correct number
while userGuess != ANSWER:
    
    # Prompt the use to make a guess
    userGuess = int(input("Guess a number between 1 and 10: "))
    
    # Decide if the number is too high, too low, or correct
    if userGuess > ANSWER :
        print("Too high!")
    elif userGuess < ANSWER :
        print("Too low!")
    else :
        print("Correct!")
    
    # Increase the count by 1
    count = count + 1

# Print a blank line for formatting
print("\n")

# Display the number of guesses
if count == 1 :
    print("It took you %d guess." % count)
else :
    print("It took you %d guesses." % count)
