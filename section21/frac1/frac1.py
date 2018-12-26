"""
ID: iocoder1
LANG: PYTHON2
TASK: frac1
"""

import math;

def recSearch(den, low, high, N, fout):
    # make sure we are still in range
    if den > N:
        return
    # calculate first and last points
    start = int(math.floor(low))
    end   = int(math.ceil(high))
    if low - start > 0.99999:
        start = start + 1
    if end - high > 0.99999:
        end = end - 1
    # mark last start point
    last = low
    # loop over all possible points
    for i in range(start+1, end, 1):
        # deep search between last & i
        recSearch(den+1, float(last*(den+1))/float(den), float(i*(den+1))/float(den), N, fout)
        # print i/den
        fout.write(str(i)+"/"+str(den)+"\n");
        # update last
        last = i
    # deep search between last and end
    recSearch(den+1, float(last*(den+1))/float(den), float(high*(den+1))/float(den), N, fout)

# open files
fin  = open('frac1.in', 'r')
fout = open('frac1.out', 'w')

# read N
N = int(fin.readline());

# level 1:
fout.write("0/1\n")
recSearch(2, 0.0, 2.0, N, fout)
fout.write("1/1\n")

# close files
fin.close()
fout.close()

