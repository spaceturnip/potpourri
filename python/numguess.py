
#!/usr/bin/env python3

"""numguess.py

have the user guess a number at random,
the range can be chosen from the command line.
"""

import sys
import random

#let the range of numbers be chosen at execution time
try:
    numrange = int(sys.argv[1])
except:
    numrange = 50 #default if nothing passed in from the shell.

guesses = 0

theNumber = random.randint(1,numrange)

guessed = False
while(not guessed):

    guess = int(input("Guess a number between 1 and " + str(numrange) + " > "))
    guesses += 1

    if guess == theNumber:
        print("That's right!\n")
        guessed = True
    elif guess > theNumber:
        print("That number is too big!")
        print("Try again.\n")
    elif guess < theNumber:
        print("That number is too small!")
        print("Try again.\n")

##End of while

print("That took you", guesses, "guess", end='')

#grammar
if guesses == 1:
    print(".")
else:
    print("es.")

