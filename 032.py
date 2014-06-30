"""
Project Euler Problem #32
==========================

The product 7254 is unusual, as the identity, 39 * 186 = 7254, containing
multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product
identity can be written as a 1 through 9 pandigital.
HINT: Some products can be obtained in more than one way so be sure to
only include it once in your sum.
"""

def is_pandigital(a, b, c) :
    digits = {}
    string = str(a)+str(b)+str(c)

    for c in string:
        if c in digits or c == '0':
            return False
        digits[c] = True
    return len(string) == 9

products = {}
for a in range(2, 100):
    for b in range(123, int(10000/a)+1):
        c = a * b
        if is_pandigital(a, b, c):
            products[c] = c

print(sum(products))
