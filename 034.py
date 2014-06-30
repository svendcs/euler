"""
Project Euler Problem #34
==========================

145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of
their digits.

Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

import math

def digits_sum(n):
    sum = 0
    while n:
        sum += math.factorial(n % 10)
        n = int(n/10)
    return sum

def is_curious(n):
    return digits_sum(n) == n

sum = 0
for i in range(10, 1000000): # let infinity = 1000000
    if is_curious(i):
        sum += i
print(sum)
