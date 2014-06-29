"""
Project Euler Problem #7
=========================

By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
that the 6^th prime is 13.

What is the 10001^st prime number?
"""

def is_prime(n):
    if n % 2 == 0:
        return False
    
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2

    return True 

i = 3
j = 1

while True:
    if is_prime(i) :
        j += 1

    if j == 10001 :
        break

    i += 1

print(i)

    
