# Chapter 3

# Write a function named collatz() that has one parameter named number. 
# If number is even, then collatz() should print number // 2 and return this value. 
# If number is odd, then collatz() should print and return 3 * number + 1.

# Then write a program that lets the user type in an integer 
#    and that keeps calling collatz() on that number until the function returns the value 1.

import sys

def collatz(number):
    if number <= 1:
        sys.exit('Invalid number')
    
    elif (number % 2 == 0):
        result = number // 2
        
        return result
    else:
        result = (number * 3) + 1
        
        return result

def get_input():
    return input('Enter number:\n')

def run():
    try:
        num = int(get_input())
        while num != 1:
            num = collatz(num)
            print(num)
    except ValueError:
        sys.exit('Not a number')

run()
    





