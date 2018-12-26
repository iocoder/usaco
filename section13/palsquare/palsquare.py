"""
ID: iocoder1
LANG: PYTHON2
TASK: palsquare
"""

def represent(num, base):
    chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    rep = ""
    while num != 0:
        rep = str(chars[num%base]) + rep
        num = num / base
    return rep

def isPalindrome(rep):
    isPal = True
    for i in range(0, len(rep)/2):
        if rep[i] != rep[len(rep)-i-1]:
            isPal = False
    return isPal

# open files
fin  = open ('palsquare.in', 'r')
fout = open ('palsquare.out', 'w')

# read base
B = int(fin.readline())

# loop from 1 to 300
for N in range(1, 301):
    # get representation of N and N*N in B
    rep_N  = represent(N,   B)
    rep_NN = represent(N*N, B)
    # if palindrome, print it
    if (isPalindrome(rep_NN)):
        fout.write(rep_N + " " + rep_NN + "\n")

# close files
fin.close()
fout.close()

