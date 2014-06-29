"""
Project Euler Problem #5
=========================

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?
"""

def evenly_divisible(n):
    for x in [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]:
        if n % x != 0:
            return False
    
    return True

i = 20
while True:
    if evenly_divisible(i):
        print(i)
        break
    i += 20
