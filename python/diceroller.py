#!/usr/bin/env python3
""" diceroller.py
    
    A simple script to use python to simulate the rolling of dice.

    reads a dice roll in the format XdY then rolls X number of Y sided dice
    showing the results of each roll and the total of all of the dice.
"""

import random
import sys


def diceRoll(sides):
    """ returns a number between 1 and sides. """
    return random.randint(1, sides)

def printUsage(name):
    print(name, " - Simulated dice rolls.")
    print("\n", 'usage\n\n', name, " XdY: a Y sided die X times") 
        
#begin main program


# collect the roll string from stdin and do some sanity checks
if len(sys.argv) == 2:
    toRoll = sys.argv[1].lower()

    #a roll is 2 numbers separated by the letter 'd'
    if toRoll.index('d') and len(toRoll.split('d')) == 2: 
        num, sides = toRoll.split('d')
        #both sides of the d need to be numbers
        if num.isdigit() and sides.isdigit():
            num = int(num)
            sides = int(sides)
            #and a positive number
            if num > 0 and sides > 0:

                rolls = []
                total = 0
                plural = ''
                
                #print a header
                #grammar is important
                if num == 1:
                    plural = 'die:'
                else:
                    plural = 'dice:'

                print("Rolling", num, sides, "sided", plural)

                for roll in range(num):
                    rolls.append(diceRoll(sides))
                    print('Roll', roll + 1, "-", rolls[roll])
                
                for roll in rolls:
                    total += roll

                print('\nTotal:', total)
else:
    printUsage(sys.argv[0])


