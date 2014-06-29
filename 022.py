"""
Project Euler Problem #22
==========================

Using names.txt [http://projecteuler.net/project/names.txt], a 46K text
file containing over five-thousand first names, begin by sorting it into
alphabetica order. Then working out the alphabetical value for each name,
multiply this value by its alphabetical position in the list to obtain a
name score.

For example, when the list is sorted into alphabetical order, COLIN, which
is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
COLIN would obtain a score of 938 * 53 = 49714.

What is the total of all the name scores in the file?
"""

import urllib.request

def score(name):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    score = 0
    for c in name:
        score += alphabet.index(c) + 1

    return score


# fetch list
url = "http://projecteuler.net/project/names.txt"
text = urllib.request.urlopen(url).read().decode('utf-8')

# convert to list
names = [name.strip('"') for name in text.split(',')]
names.sort()

n = 0
for i in range(len(names)):
    n += (i+1) * score(names[i])

print(n)
