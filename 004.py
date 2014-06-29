"""
Project Euler Problem #4
=========================

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def reverse(a):
    return a[::-1]

def is_pal(a):
    return a == reverse(a)

largest = 0
for i in range(100, 999):
    for j in range(100, 999):
        product = i*j        
        if is_pal(str(product)) and product > largest:
            largest = product

print(largest)
