"""
Project Euler Problem #38
==========================

Take the number 192 and multiply it by each of 1, 2, and 3:

  192 * 1 = 192
  192 * 2 = 384
  192 * 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. We
will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
and 5, giving the pandigital, 918273645, which is the concatenated product
of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed as
the concatenated product of an integer with (1,2, ... , n) where n > 1?
"""

def pandigital(a):
    marked = {"0": True}
    for c in a:
        if c in marked:
            return False
        marked[c] = True
    return len(marked) == 10

def concatenated_product(a, n):
    product = ""

    for i in range(1, n+1):
        product += str(a * i)
    return product

best = 1
for n in range(2, 10):
    for a in range(1, 10000):
        product = concatenated_product(a, n)
        if len(product) > 9: break
        if not pandigital(product): continue

        product = int(product)
        if product > best:
            best = product

print(best)