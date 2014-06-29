"""
Project Euler Problem #20
==========================

n! means n * (n - 1) * ... * 3 * 2 * 1

Find the sum of the digits in the number 100!
"""

import math

a = str(math.factorial(100))
sum = 0

for i in range(len(a)):
    sum += int(a[i])

print(sum)
