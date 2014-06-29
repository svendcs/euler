"""
Project Euler Problem #26
==========================

A unit fraction contains 1 in the numerator. The decimal representation of
the unit fractions with denominators 2 to 10 are given:

   1/2  =  0.5
   1/3  =  0.(3)
   1/4  =  0.25
   1/5  =  0.2
   1/6  =  0.1(6)
   1/7  =  0.(142857)
   1/8  =  0.125
   1/9  =  0.(1)
  1/10  =  0.1

Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can
be seen that ^1/[7] has a 6-digit recurring cycle.

Find the value of d < 1000 for which ^1/[d] contains the longest recurring
cycle in its decimal fraction part.
"""

def cycle_length(b):
    marked = {}
    counter = 0;
    a = 1

    while a % b != 0:
        counter += 1
        if a%b in marked:
            return counter - marked[a%b]

        marked[a % b] = counter
        a *= a%b * 10

    return 0

best = 2
for d in range(1, 1000):
    if cycle_length(d) > cycle_length(best):
        best = d 

print(best)
