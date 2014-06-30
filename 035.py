"""
Project Euler Problem #35
==========================

The number, 197, is called a circular prime because all rotations of the
digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
71, 73, 79, and 97.

How many circular primes are there below one million?
"""

# Sieve of Eratosthenes
primes = [True for i in range(1000000)]

for i in range(2, 1000000):
    if not primes[i]:
        continue
    for j in range(i+i, 1000000, i):
        primes[j] = False

def rotate(a):
    return a[1:] + a[:1]

def circular(n):
    a = str(n)
    for i in range(len(a)):
        if not primes[int(a)]:
            return False
        a = rotate(a)
    return True

count = 0
for i in range(2, len(primes)):
    if not primes[i]: continue
    if circular(i):
        count += 1
print(count)
