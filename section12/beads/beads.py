"""
ID: iocoder1
LANG: PYTHON2
TASK: beads
"""

def equ(a, b):
    if a == b or a == 'w' or b == 'w':
        return True
    else:
        return False

# open files
fin = open ('beads.in', 'r')
fout = open ('beads.out', 'w')

# read number of beads
n = int(fin.readline())

# read beads string
beads = fin.readline().strip()

# try different cuts
maximum = 0
for i in range(0, len(beads)):
    # initialize visited array   
    visited = [False]*len(beads)
    # calculate befores
    befores = 0;
    j = (i-1)%len(beads);
    color = beads[j];
    while j != i and equ(beads[j], color):
        befores += 1
        if color == 'w':
            color = beads[j]
        visited[j] = True
        j = (j-1)%len(beads)
    # calculate afters
    afters = 0
    k = i;
    color = beads[k];
    while (not visited[k]) and equ(beads[k], color):
        afters += 1
        if color == 'w':
            color = beads[k]
        visited[k] = True
        k = (k+1)%len(beads)
    # calculate maximum
    if befores+afters > maximum:
        maximum = befores+afters

# output maximum
fout.write(str(maximum) + "\n");

# close files
fin.close()
fout.close()

