"""
ID: iocoder1
LANG: PYTHON2
TASK: skidesign
"""

# the trick in this problem is that the mass removed
# from tallest elevations needn't be equal to the
# mass added to shortest elevations. Problem
# statement doesn't say at all that mass removed
# from highest hills will be used for shortest.

# open files
fin  = open ('skidesign.in', 'r')
fout = open ('skidesign.out', 'w')

# read N (number of hills)
N = int(fin.readline())

# read hill elevations
hills = [0]*N
for i in range(N):
    hills[i] = int(fin.readline())

# try all possible pairings
minCost = 100000000
for i in range(0, 83):
    hmin = i
    hmax = i+17
    cost = 0
    for h in hills:
        if h < hmin:
            cost += (h-hmin)**2
        elif h > hmax:
            cost += (hmax-h)**2
    if (cost < minCost):
        minCost = cost

# print minimum cost
fout.write(str(minCost) + "\n")

# close files
fin.close()
fout.close()

