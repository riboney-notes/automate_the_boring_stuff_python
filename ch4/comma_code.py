# Chapter 4
# Write a function that takes a list value as an argument 
# and returns a string with all the items separated by a comma and a space
#  with an "and" inserted before the last item. 
# Ex: spam = ['apples', 'bananas', 'tofu', 'cats'] would return
#   'apples, bananas, tofu, and cats'.

import sys

def prettifyList(arg):
    if not isinstance(arg, list) or not (len(arg) >= 1):
        sys.exit('Argument is not valid!')

    modifiedArg = arg.copy()
    modifiedArg.insert(-1, 'and')

    stringModifiedArg = ", ".join(map(str, modifiedArg))

    return stringModifiedArg

print(prettifyList(['apples', 'bananas', 'tofu', 'cats']))