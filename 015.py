"""
Project Euler Problem #15
==========================

Starting in the top left corner of a 2 * 2 grid, there are 6 routes
(without backtracking) to the bottom right corner.

How many routes are there through a 20 * 20 grid?
"""

mem = {}
mem[(0,0)] = 1
def paths(x, y):
    if not (x,y) in mem:
        mem[(x,y)] = 0
        if x > 0:
            mem[(x,y)] += paths(x-1,y)
        if y > 0:
            mem[(x,y)] += paths(x,y-1)
    return mem[(x,y)]

print(paths(20,20))
