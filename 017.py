"""
Project Euler Problem #17
==========================

If the numbers 1 to 5 are written out in words: one, two, three, four,
five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written
out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and
forty-two) contains 23 letters and 115 (one hundred and fifteen) contains
20 letters. The use of "and" when writing out numbers is in compliance
with British usage.
"""

# Numbers 1-9
a = 3 + 3 + 5 + 4 + 4 + 3 + 5 + 5 + 4

# Numbers 10-19
b = 3 + 6 + 6 + 8 + 8 + 7 + 7 + 9 + 8 + 8

# Numbers 20-99
c = 10 * (6 + 6 + 5 + 5 + 5 + 7 + 6 + 6) + 8 * a

# Numbers 100-999
d = a * 100 + (a+b+c) * 9 + 7 * 9 + 10 * 9 * 99

# 1-1000
e = a + b + c + d + 11

print(e)
