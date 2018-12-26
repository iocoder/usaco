"""
ID: iocoder1
LANG: PYTHON2
TASK: preface
"""

# roman symbols and vals
symbols=["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
vals=[1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
counts = {"I": 0, "V": 0, "X": 0, "L": 0, "C": 0, "D": 0, "M": 0}

# open files
fin  = open ('preface.in', 'r')
fout = open ('preface.out', 'w')

# read N
N = int(fin.readline())

# find roman symbols
for n in range(1, N+1):
    while n > 0:
        for i in range(0, len(vals)):
            if n >= vals[i]:
                n = n - vals[i]
                for c in symbols[i]:
                    counts[c] = counts[c] + 1
                break

# print counts:
for sym in ["I", "V", "X", "L", "C", "D", "M"]:
    if counts[sym] > 0:
        fout.write(sym + " " + str(counts[sym]) + "\n")

# close files
fin.close()
fout.close()
