"""
Project Euler Problem #42
==========================

The n^th term of the sequence of triangle numbers is given by, t[n] =
1/2n(n+1); so the first ten triangle numbers are:

                 1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its
alphabetical position and adding these values we form a word value. For
example, the word value for SKY is 19 + 11 + 25 = 55 = t[10]. If the word
value is a triangle number then we shall call the word a triangle word.

Using words.txt [http://projecteuler.net/project/words.txt], a 16K text
file containing nearly two-thousand common English words, how many are
triangle words?
"""

import urllib.request

def position(c):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    return alphabet.index(c)+1

def word_value(w):
    return sum(position(c) for c in w)

triangle_numbers = set()
for i in range(1, 100):
    n = int(1/2*i*(i+1))
    triangle_numbers.add(n)

# Fetch words
url = "http://projecteuler.net/project/words.txt"
text = urllib.request.urlopen(url).read().decode('utf-8')
words = [word.strip('"') for word in text.split(',')]

# Count
triangle_words = [word for word in words if word_value(word) in triangle_numbers]
print(len(triangle_words))
