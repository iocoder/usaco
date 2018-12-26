"""
ID: iocoder1
LANG: PYTHON2
TASK: hamming
"""

def getDist(num1, num2):
    bits = num1^num2
    ones = 0
    while bits != 0:
        ones = ones + (bits&1)
        bits = bits >> 1
    return ones

# open files
fin  = open ('hamming.in', 'r')
fout = open ('hamming.out', 'w')

# read N, B, and D
N,B,D = map(int, fin.readline().split())

# find codes
codes = []
for i in range(0, 1<<B):
    # assume i is valid
    valid = True
    # test i against all current codes
    for code in codes:
        if getDist(code, i) < D:
            valid = False
            break
    # if i is still valid, add it
    if valid:
        codes.append(i)
    if len(codes) == N:
        break

# print codes
for i in range(0, len(codes)):
    fout.write(str(codes[i]))
    if i == len(codes)-1 or i%10 == 9:
        fout.write("\n")
    else:
        fout.write(" ")

# close files
fin.close()
fout.close()
