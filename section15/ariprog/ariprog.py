"""
ID: iocoder1
LANG: PYTHON2
TASK: ariprog
"""

# open files
fin  = open ('ariprog.in', 'r')
fout = open ('ariprog.out', 'w')

# read N and M
N = int(fin.readline())
M = int(fin.readline())

# construct array of bisquares
# isBi[b] = True if b is bisquare
isBi = [False]*(250*250*3)
bisquares = []

# enumerate all bisquares
bmax = 0
bcnt = 0
for i in range(M+1):
    for j in range(M+1):
        b = i*i+j*j
        if (b > bmax):
            bmax = b
        if isBi[b] == False:
            bcnt += 1
            bisquares.append(b)
        isBi[b] = True
bisquares.sort()

# enumerate all sequences
total = 0
for b in range(1, bmax+1):
    i = 0
    while i < bcnt and bisquares[i]+b*(N-1) <= bmax:
        a = bisquares[i]
        if not isBi[a+b]:
            i += 1
            continue
        n = 2
        while n < N and isBi[a+b*n]:
            n += 1
        if n == N:
            # we found a bisquare progression
            fout.write("%d %d\n" % (a, b))
            total += 1
            if total == 10000:
                break
        i += 1
    if total == 10000:
        break

# None?
if total == 0:
    fout.write("NONE\n")

# close files
fin.close()
fout.close()

