"""
Project Euler Problem #40
==========================

An irrational decimal fraction is created by concatenating the positive
integers:

                  0.123456789101112131415161718192021...
                               ^

It can be seen that the 12^th digit of the fractional part is 1.

If d[n] represents the n^th digit of the fractional part, find the value
of the following expression.

    d[1] * d[10] * d[100] * d[1000] * d[10000] * d[100000] * d[1000000]
"""

def digit(n, i):
    return int(str(n)[i])

next = 1
product = 1
n = 0
i = 1

while next <= 1000000:
    delta = len(str(i))
    if n + delta >= next:
        d = digit(i, next-n-1)
        product *= d
        next *= 10
    n += len(str(i))
    i += 1

print(product)
