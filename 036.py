"""
Project Euler Problem #36
==========================

The decimal number, 585 = 1001001001[2] (binary), is palindromic in both
bases.

Find the sum of all numbers, less than one million, which are palindromic
in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include
leading zeros.)
"""

def convert_base(n):
    res = ""
    while n:
        res = str(n %2) + res
        n = int(n/2)
    return res

def palindromic(n):
    n = str(n)
    return n == n[::-1]

numbers = [i for i in range(1000000) if palindromic(i) and palindromic(convert_base(i))]

print(sum(numbers))
