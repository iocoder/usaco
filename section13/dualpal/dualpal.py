"""
ID: iocoder1
LANG: PYTHON2
TASK: dualpal
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
fin  = open ('dualpal.in', 'r')
fout = open ('dualpal.out', 'w')

# read N and S
N,S = map(int, fin.readline().split())

# find first N numbers > S such that they are palindrome in more than 2 bases [B:2->10]
while N > 0:
    S    = S+1
    Pals = 0
    for B in range(2, 11):
        if isPalindrome(represent(S, B)):
            Pals += 1
    if Pals >= 2:
        fout.write("%d\n" % S)
        N -= 1

# close files
fin.close()
fout.close()

