"""
Project Euler Problem #41
==========================

We shall say that an n-digit number is pandigital if it makes use of all
the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

import itertools

def is_prime(n):
    n = abs(n)

    if n == 2:
        return True

    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True 

largest = 3
for n in range(1,10):
    string = ""
    for i in range(1,n+1):
        string = string + str(i)
    for perm in itertools.permutations(string):
        perm = int("".join(perm))
        if is_prime(perm) and perm > largest:
            largest = perm

print(largest)
