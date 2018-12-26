"""
ID: iocoder1
LANG: PYTHON2
TASK: gift1
"""

import collections

# open files
fin = open ('gift1.in', 'r')
fout = open ('gift1.out', 'w')

# accounts
A = collections.OrderedDict()

# read number of participants
n = int(fin.readline())

# read participant names and create accounts
for i in range(0, n):
    A[fin.readline().strip()] = 0

# read every user's activity
for i in range(0, n):
    # first line contains person name
    giver = fin.readline().strip()
    # next line contains gift size and number of givens
    gift, gnum = map(int, fin.readline().split())
    # next gnum lines contain names of givens
    for j in range(0, gnum):
        given = fin.readline().strip()
        A[given] += gift/gnum
        A[giver] -= gift/gnum

for name in A:
    fout.write(name + " " + str(A[name]) + "\n")

# close files
fin.close()
fout.close()

