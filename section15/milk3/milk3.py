"""
ID: iocoder1
LANG: PYTHON2
TASK: milk3
"""

# capacities and values
C = []
V = []
sols = []

# hashtable
hashtable = [None]*1000000

# calculate hash value for a specific setting
def hashval(V):
    return (V[0] + V[1]*100 + V[2]*10000) % len(hashtable)

# get specific setting from hashtable
def isHashed(V):
    h = hashval(V)
    p = hashtable[h]
    while p != None:
        if p["A"]==V[0] and p["B"]==V[1] and p["C"]==V[2]:
            return True
        p = p["next"]
    return False

# add specific setting to hashtables
def hashPut(V):
    h = hashval(V)
    p = {"A":V[0], "B":V[1], "C":V[2], "next":hashtable[h]}
    hashtable[h] = p

# pour from bottle to another bottle
def pour(V, C, bfrom, bto):
    q = min(C[bto] - V[bto], V[bfrom])
    V[bfrom] -= q
    V[bto]   += q

# recursively find solutions
def rec(V, C):
    global sols
    # have we already reached this state before?
    if (isHashed(V)):
        return
    # record this state so that we do not visit again
    hashPut(V)
    # is this the required solution?
    if V[0] == 0:
        sols.append(V[2])
    # at this level, we have six options:
    for src in range(3):
        for dest in range(3):
                Vcopy = [V[0], V[1], V[2]]
                pour(Vcopy, C, src, dest)
                rec(Vcopy, C)

# open files
fin  = open ('milk3.in', 'r')
fout = open ('milk3.out', 'w')

# read capacities from input file
words = fin.readline().split()
C.append(int(words[0]))
C.append(int(words[1]))
C.append(int(words[2]))

# initialize buckets
V.append(0)
V.append(0)
V.append(C[2])

# DFS
rec(V, C)

# sort solutions
sols.sort()

# print all solutions
for i in range(len(sols)-1):
    fout.write("%d " % sols[i])
fout.write("%d\n" % sols[-1])

# close files
fin.close()
fout.close()

