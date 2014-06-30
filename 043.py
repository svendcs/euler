"""
Project Euler Problem #43
==========================

The number, 1406357289, is a 0 to 9 pandigital number because it is made
up of each of the digits 0 to 9 in some order, but it also has a rather
interesting sub-string divisibility property.

Let d[1] be the 1^st digit, d[2] be the 2^nd digit, and so on. In this
way, we note the following:

  * d[2]d[3]d[4]=406 is divisible by 2
  * d[3]d[4]d[5]=063 is divisible by 3
  * d[4]d[5]d[6]=635 is divisible by 5
  * d[5]d[6]d[7]=357 is divisible by 7
  * d[6]d[7]d[8]=572 is divisible by 11
  * d[7]d[8]d[9]=728 is divisible by 13
  * d[8]d[9]d[10]=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

# brute force
# The entire problem can be solved by analysis by hand

import itertools

def digit(a, n):
    return a[n-1]

def has_property(n):
    divisors = [2, 3, 5, 7, 11, 13, 17]
    for i in range(2, 9):
        con = int(digit(n, i)+digit(n, i+1)+digit(n, i+2))
        if not con % divisors[i-2] == 0:
            return False
    return True

string = "0123456789"
sum = 0

for perm in itertools.permutations(string):
    perm = "".join(perm)
    if has_property(perm):
        sum += int(perm)
print(sum)
