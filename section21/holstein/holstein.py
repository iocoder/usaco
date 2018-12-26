"""
ID: iocoder1
LANG: PYTHON2
TASK: holstein
"""
def comb(fout, scoop, req, start, rem, chosen, sums):
    if rem == 0:
        # evaluate chosen
        valid = True
        for j in range(0, len(sums)):
            if sums[j] < req[j]:
                valid = False
        # solved?
        if valid == True:
            fout.write(str(len(chosen))+" ")
            for j in range(0, len(chosen)):
                fout.write(str(chosen[j]+1))
                if j < len(chosen)-1:
                    fout.write(" ")
                else:
                    fout.write("\n")
        # return status
        return valid
    else:
        for i in range(start, len(scoop)):
            # try to take this one
            chosen.append(i)
            # add the values of scoop
            for j in range(0, len(sums)):
                sums[j] = sums[j] + scoop[i][j]
            # recursive loop
            valid = comb(fout, scoop, req, i+1, rem-1, chosen, sums)
            # remove scoop
            chosen.pop()
            # remove the values of scoop
            for j in range(0, len(sums)):
                sums[j] = sums[j] - scoop[i][j]
            # problem solved?
            if valid == True:
                return True
        # problem not solved yet
        return False

# open files
fin  = open ('holstein.in', 'r')
fout = open ('holstein.out', 'w')

# read V
V = int(fin.readline())

# read requirements
req = map(int, fin.readline().split())

# read G
G = int(fin.readline())

# read scoops
scoop = [None] * G
for i in range(G):
    scoop[i] = map(int, fin.readline().split())

# try different combinations
for i in range(1, G+1):
    valid = comb(fout, scoop, req, 0, i, [], [0]*V);
    if valid == True:
        break

# close files
fin.close()
fout.close()

