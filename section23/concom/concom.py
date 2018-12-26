"""
ID: iocoder1
LANG: PYTHON2
TASK: concom
"""

# open files
fin  = open ('concom.in', 'r')
fout = open ('concom.out', 'w')

# read N
N = 100

# shares[i][j] = share of company i in j
shares = [None] * (N)
for i in range(0, N):
    shares[i] = [0] * (N)

# controls[i][j] = company i controls j
controls = [None] * (N)
for i in range(0, N):
    controls[i] = [False] * (N)

# credits[i]: company credits for all other companies
credits = [None] * (N)
for i in range(0, N):
    credits[i] = [None] * (N)
    for j in range(0, N):
        credits[i][j] = {'val': 0, 'slave': j}

# creditHash[i]: hash table for company i
creditHash = [None] * (N)
for i in range(0, N):
    creditHash[i] = [None] * (N)
    for j in range(0, N):
        creditHash[i][j] = credits[i][j]

# read all shares
lineCount = int(fin.readline().strip())
for curLine in range(0, lineCount):
    toks = fin.readline().strip().split()
    i = int(toks[0])-1
    j = int(toks[1])-1
    p = int(toks[2])
    shares[i][j] = p
    creditNode = creditHash[i][j]
    creditNode['val'] = creditNode['val'] + p

# loop over all companies
for i in range(0, N):
    # loop until no more credit
    while True:
        # get maximum-credit slave
        maxVal = 0
        maxJ = 0
        maxIndex = 0
        maxNode = None
        for curIndex in range(0, N):
            creditNode = credits[i][curIndex]
            if creditNode != None and creditNode['val'] > maxVal:
                maxVal = creditNode['val']
                maxJ = creditNode['slave']
                maxIndex =curIndex
                maxNode = creditNode
        # no more slaves
        if maxVal <= 50:
            break
        # own this bitch
        controls[i][maxJ] = 1
        # remove from list of credits (to avoid processing again)
        credits[i][maxIndex] = None
        # add credits of all children
        for k in range(0, N):
            creditNode = creditHash[i][k]
            creditNode['val'] = creditNode['val'] + shares[maxJ][k]

# print all controls
for i in range(0, N):
    for j in range(0, N):
        if i != j and controls[i][j]:
            fout.write(str(i+1)+" "+str(j+1)+"\n")

# close files
fin.close()
fout.close()
