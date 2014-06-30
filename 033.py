"""
Project Euler Problem #33
==========================

The fraction 49/98 is a curious fraction, as an inexperienced
mathematician in attempting to simplify it may incorrectly believe that
49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less
than one in value, and containing two digits in the numerator and
denominator.

If the product of these four fractions is given in its lowest common
terms, find the value of the denominator.
"""

import fractions

res = fractions.Fraction(1, 1)

for a in range(10, 100):
    for b in range(a+1, 100):
        if b % 10 == 0: continue

        first = [int(a/10),a%10]
        second = [int(b/10),b%10]
        if any(i in second for i in first) and not all(i in second for i in first):
            if first[0] in second: 
                x = first[0]
            else:
                x = first[1]
            first.remove(x)
            second.remove(x)

            if a*second[0] == b*first[0]:
                res *= fractions.Fraction(first[0], second[0])

print(res.denominator)
