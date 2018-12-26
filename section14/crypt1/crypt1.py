"""
ID: iocoder1
LANG: PYTHON2
TASK: crypt1
"""    

def isEncodable(num, digits, limit):
    flag = True
    if num >= limit or num < limit/10:
        flag = False
    while num > 0:
        if not digits[num%10]:
            flag = False
        num = num/10
    return flag

# open files
fin  = open ('crypt1.in', 'r')
fout = open ('crypt1.out', 'w')

# read N
N = int(fin.readline())

# read N numbers
digits = [False]*10
for digit in fin.readline().split():
    digits[int(digit)] = True

# loop over all possibilities
sols = 0
for abc in range (1000):
    for d in range (10):
        for e in range (10):
            de = d*10+e
            # apply conditions:
            # abc      must be encodable
            # de       must be encodable
            # abc*e    must be encodable
            # 10*d*abc must be encodable
            # abc*de   must be encodable
            c1 = isEncodable(abc,    digits, 1000)
            c2 = isEncodable(de,     digits, 100)
            c3 = isEncodable(abc*e,  digits, 1000)
            c4 = isEncodable(abc*d,  digits, 1000)
            c5 = isEncodable(abc*de, digits, 10000)
            if c1 and c2 and c3 and c4 and c5:
                sols += 1

# print out number of solutions
fout.write(str(sols) + "\n")

# close files
fin.close()
fout.close()

