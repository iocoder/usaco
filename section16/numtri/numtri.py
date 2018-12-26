"""
ID: iocoder1
LANG: PYTHON2
TASK: numtri
"""

# open files
fin  = open ('numtri.in', 'r')
fout = open ('numtri.out', 'w')

# read number of rows
R = int(fin.readline())

# read the rows themselves
V = [0]*(1000*1000)
cnt = 0
for r in range(R):
    words = fin.readline().split()
    for w in words:
        V[cnt] = int(w)
        cnt = cnt+1

# calculate the sums in a dynamic programming fashion
S = [0]*(1000*1000)
child = (R+1)*(R+2)/2-2
checkpoint = R
cur_row = R-1
for i in range(cnt-1, -1, -1):
    S[i] = V[i] + max(S[child], S[child+1])
    child -= 1
    checkpoint -= 1
    if (checkpoint == 0):
        checkpoint = cur_row
        cur_row -= 1
        child -= 1

# print sum of largest route
fout.write(str(S[0]) + "\n")

# close files
fin.close()
fout.close()

