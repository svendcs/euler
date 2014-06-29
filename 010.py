"""
Project Euler Problem #10
==========================

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

sum = 0

numbers = {}

for i in range(2, 2000000):
    if not i in numbers:
        sum += i
        for j in range(i, 2000000, i):
            numbers[j] = False

print(sum)
