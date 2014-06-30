"""
Project Euler Problem #28
==========================

Starting with the number 1 and moving to the right in a clockwise
direction a 5 by 5 spiral is formed as follows:

                              21 22 23 24 25
                              20  7  8  9 10
                              19  6  1  2 11
                              18  5  4  3 12
                              17 16 15 14 13

It can be verified that the sum of both diagonals is 101.

What is the sum of both diagonals in a 1001 by 1001 spiral formed in the
same way?
"""

spiral = {}
max_size = 1001

def ring(size, i):
    offset = int((max_size - size)/2)
    y = offset+1
    while y < max_size-offset:
        spiral[(max_size-offset-1,y)] = i
        y += 1
        i += 1

    x = max_size - offset - 2 
    while x >= offset:
        spiral[(x,max_size-offset-1)] = i
        x -= 1
        i += 1

    y = max_size - offset - 2
    while y >= offset:
        spiral[(offset,y)] = i
        y -= 1
        i += 1

    x = offset+1
    while x < max_size-offset:
        spiral[(x,offset)] = i
        x += 1
        i += 1
    return i

offset = int((max_size - 1)/2)
spiral[(offset,offset)] = 1
i = 2
for j in range(3, max_size+1, 2):
    i = ring(j, i)

sum = 0
for i in range(max_size):
    sum += spiral[(i,i)]
    sum += spiral[(max_size-1-i,i)]
sum -= 1

print(sum)
