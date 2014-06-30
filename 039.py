"""
Project Euler Problem #39
==========================

If p is the perimeter of a right angle triangle with integral length
sides, {a,b,c}, there are exactly three solutions for p = 120.

                    {20,48,52}, {24,45,51}, {30,40,50}

For which value of p < 1000, is the number of solutions maximised?
"""

import math

count = [0 for i in range(1000)]

for a in range(1000):
    for b in range(1000):
        c = math.sqrt(a**2 + b**2)
        if(c != int(c)): continue
        c = int(c)

        if(a + b + c >= 1000): continue
        count[a+b+c] += 1

best = 0

for i in range(1000):
    if count[i] > count[best]:
        best = i

print(best)