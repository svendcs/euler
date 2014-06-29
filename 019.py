"""
Project Euler Problem #19
==========================

You are given the following information, but you may prefer to do some
research for yourself.

  * 1 Jan 1900 was a Monday.
  * Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
  * A leap year occurs on any year evenly divisible by 4, but not on a
    century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth
century (1 Jan 1901 to 31 Dec 2000)?
"""

def leap_year(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    
    return year % 4

def days(year, month):
    if month in [4, 6, 11]:
        return 30
    if month in [2]:
        return 29 if leap_year(year) else 28
    else:
        return 31


day = 1
sundays = 0

# The year 1900
for month in range(1, 13):
    day += days(1900, month)

for year in range(1901, 2001):
    for month in range(1, 13):
        if day % 7 == 0:
            sundays += 1
        day += days(year, month)

print(sundays)
