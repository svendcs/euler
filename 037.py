"""
Project Euler Problem #37
==========================

The number 3797 has an interesting property. Being prime itself, it is
possible to continuously remove digits from left to right, and remain
prime at each stage: 3797, 797, 97, and 7. Similarly we can work from
right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left
to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
"""

limit = 1000000

primes = [True for i in range(limit)]
primes[1] = False

for i in range(2, limit):
    if not primes[i]:
        continue
    for j in range(i+i, limit, i):
        primes[j] = False

def truncatable_prime(n):
    a = str(n)
    b = ""

    while a != "":
        a, b = a[:-1], a[-1:]+b

        if not primes[int(b)]:
            return False
        if a != "" and not primes[int(a)]:
            return False
    return True

sum = 0
count = 0
i = 7
while count < 11:
    i += 1
    if not primes[i]: continue
    if not truncatable_prime(i): continue

    count += 1
    sum += i

print(sum)