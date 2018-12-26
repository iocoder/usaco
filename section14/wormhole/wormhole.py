"""
ID: iocoder1
LANG: PYTHON2
TASK: wormhole
"""

total = 0

def printPairings(wormholes, mypair, N):
    for i in range(N):
        x1 = wormholes[i]["x"]
        y1 = wormholes[i]["y"]
        x2 = wormholes[mypair[i]]["x"]
        y2 = wormholes[mypair[i]]["y"]
        print "(%d,%d) --> (%d,%d)" % (x1,y1,x2,y2)
    print "==========================="

def simulate(wormholes, mypair, N, start):
    visited = [False]*N
    cur = start    
    # move:
    while True:
        # already visited?
        if visited[cur]:
            # a cycle has been found!
            return False
        # mark as visited
        visited[cur] = True
        # perform the tunnelling
        cur = mypair[cur]
        # now we are at the paired wormhole
        # find next wormhole in the same x direction
        min_x = 2000000000
        next = -1
        for i in range(N):
            c1 = wormholes[i]["x"] <  min_x
            c2 = wormholes[i]["x"] >  wormholes[cur]["x"]
            c3 = wormholes[i]["y"] == wormholes[cur]["y"]
            if c1 and c2 and c3:
                min_x = wormholes[i]["x"]
                next = i
        # no wormhole in the same row?
        if next == -1:
            return True # simulation done
        # move to next wormhole
        cur = next

def rec(wormholes, mypair, N):
    # recursively enumerate all possible pairings
    global total
    # find first wormhole that is unpaired
    i = -1
    for e in range(N):
        if (mypair[e] == -1):
            i = e
            break
    # are we done yet?
    if i > -1:
        # try all possible pairings
        for j in range(i+1, N):
            if mypair[j] == -1:
                # try out this pairing
                mypair[i] = j
                mypair[j] = i
                rec(wormholes, mypair, N)
                mypair[i] = -1
                mypair[j] = -1
    else:
        # all pairs are assigned
        # we must make sure that the pairing assignment doesn't
        # induce any form of infinite cycle
        # we try to simulate cow movement by starting
        # at any wormhole then move in x+ direction.
        isLoopy = False
        for i in range(N):
            if not simulate(wormholes, mypair, N, i):
                # if simulation is not successful, this pairing
                # introduces a loop
                isLoopy = True
                break
        # add to count
        if isLoopy:
            total += 1

# open files
fin  = open ('wormhole.in', 'r')
fout = open ('wormhole.out', 'w')

# read N (number of wormholes)
N = int(fin.readline())

# read wormhole coordinates
wormholes = []
for i in range(N):
    x,y = map(int, fin.readline().split())
    wormholes.append({"x": x, "y": y})

# try pairings
mypair = [-1] * N
rec(wormholes, mypair, N)

# print number of pairings
fout.write(str(total) + "\n")

# close files
fin.close()
fout.close()

