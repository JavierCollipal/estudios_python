"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format

A single line containing a positive integer, .

Constraints

Output Format

Print Weird if the number is weird. Otherwise, print Not Weird.
"""


def evaluateN(number):
    if number % 2 == 1:
        print('Weird')
    elif number % 2 == 0 and 2 <= number <= 5:
        print('Not Weird')
    elif number % 2 == 0 and 6 <= number <= 20:
        print('Weird')
    elif number % 2 == 0 and number > 20:
        print('Not Weird')
    else:
        print('Not Weird')


evaluateN(20)
