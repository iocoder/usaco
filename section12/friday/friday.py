"""
ID: iocoder1
LANG: PYTHON2
TASK: friday
"""

# let's consider year 0 (the year just before year 1)
# In year 0, March 1st was a Friday
# We will assign number 0..6 to week days Sat..Fri.
# So, in year 0, March 1st was day 4 (Wed).
# Now let's assume that year starts with March and ends with Feb,
# and assign numbers 3..14 for months.
# i.e, Jan of year 1 is actually month 13 of year 0,
# and Jan of 1990 is aactually month 13 of year 1989.

# given this new definition, for year 0:
# month 1, day 1 was day-of-week 4 as shown above.
# inside that month, we can find day-of-week easily:
# DOW = (d + 3) % 7 where d is day. The 3 forces first
# day of March to be 4.

# now we need to modify the 3 to represent the shift introduced by 
# months of year 0. For instance, March is 31. So this 
# is going to introduces a 3-day shift in the
# DOW formula for April, and so on.
# Given a month m, we want to know the total shifts
# happened by previous months.
# Month         Number    Shifts-By-Prev
# ------------------------------------------
# March           3          3 (3)
# April           4          6 (6)
# May             5          8 (1)
# June            6         11 (4)
# July            7         13 (6)
# August          8         16 (2)
# September       9         19 (5)
# October        10         21 (0)
# November       11         24 (3)
# December       12         26 (5)
# January        13         29 (1)
# February       14         32 (4)

# By regression, we can deduce that:
# -> shifts = round(2.6*m-4.77)
# convert round operation to floor
# -> shifts = floor(2.6*m-4.27)
# now add 2.6 and subtract 2.6:
# -> shifts = floor(2.6*m+2.6-6.87)
# interestingly, rounding 6.87 to 7 will result in no error:
# -> shifts = floor(2.6*m+2.6-7)
# -7 can move outside the floor
# -> shifts = floor(2.6*m+2.6) - 7
# use 13/5 instead of 2.6
# -> shifts = floor(13*(m+1)/5) - 7
# now we reconstruct the DOW formula:
# -> DOW = (d + floor(13*(m+1)/5) - 7) % 7
# we know that 7 % 7 is 0:
# -> DOW = (d + floor(13*(m+1)/5)) % 7

# For years, we will divide year number into
# two vars:
# y = the least two significant digits of year
# Y = the highest two significant digits of year

# Next step is to add shifts introduced by
# previous years. Each year is 365 years.
# Because 365%7 = 1, each year results
# in 1-day shift. So the new formula will be:
# -> DOW = (d + floor(13*(m+1)/5) + y) % 7
# where y is year number inside the century.

# Inside a century, there are several leap
# years that introduce extra shifts:
# -> DOW = (d + floor(13*(m+1)/5) + y + floor(y/4)) % 7

# For a normal century, there are 36524 days
# -> DOW = (d + floor(13*(m+1)/5) + y + floor(y/4) + 5*Y) % 7

# Every 400 century, first year is a leap year
# -> DOW = (d + floor(13*(m+1)/5) + y + floor(y/4) + 5*Y + floor(Y/4)) % 7

# This awesome formula is called Zeller's congruence. We will
# use this formula to calculate day-of-week.

def dayOfWeek(day, month, year):
    d = day
    m = (month-3)%12 + 3
    if (month < 3):
        year -= 1
    y = year%100
    Y = year/100
    return (d + (13*(m+1))/5 + y + y/4 + 5*Y + Y/4)%7

# initialize list of week days
days = [0]*7

# open files
fin = open ('friday.in', 'r')
fout = open ('friday.out', 'w')

# read number of years
n = int(fin.readline())

# loop over years
for year in range(1900, 1900+n):
    for month in range(1, 13):
        days[dayOfWeek(13, month, year)] += 1

# print days of week
fout.write(' '.join(str(e) for e in days) + "\n")

# close files
fin.close()
fout.close()

