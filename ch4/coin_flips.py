# Chapter 4

# Write a program to find out how often a streak of six heads 
# or a streak of six tails comes up in a randomly generated list of heads and tails. 
#
# Your program breaks up the experiment into two parts: 
#  the first part generates a list of randomly selected 'heads' and 'tails' values,
#  and the second part checks if there is a streak in it. 
# 
# Put all of this code in a loop that repeats the experiment 10,000 times 
# so we can find out what percentage of the coin flips contains
#  a streak of six heads or tails in a row.
# 
#  As a hint, the function call random.randint(0, 1) will
#  return a 0 value 50% of the time and a 1 value the other 50% of the time.

import random

def run():
    numberOfStreaks = 0

    for experimentNumber in range(10000):
        if streak_in_100_flips():
            numberOfStreaks += 1

    print('Chance of streak: %s%%' % (numberOfStreaks / 100))

def streak_in_100_flips():
    streak = 1
    curr = ""
    prev = ""

    for x in range(100):
        # Code that creates a list of 100 'heads' or 'tails' values.
        curr = 'H' if random.randint(0,1) == 0 else 'T'

        if(curr == prev):
            streak += 1
        else:
            streak = 1

        prev = curr

        # Code that checks if there is a streak of 6 heads or tails in a row.
        if streak == 6:
            return True


    return False

run()

