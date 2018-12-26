"""
ID: iocoder1
LANG: PYTHON2
TASK: zerosum
"""

# try all combinations
def tryAll(expr, curNum, maxNum, fout):
    if curNum > maxNum:
        # evaluate
        filtExpr = filter(lambda a: a != ' ', expr)
        nums = filtExpr.replace('+',' ').replace('-',' ').split()
        ops = filter(lambda a: a == '+' or a == '-', expr)
        tot = int(nums[0])
        for i in range(1, len(nums)):
            if ops[i-1] == '+':
                tot += int(nums[i])
            else:
                tot -= int(nums[i])
        if tot == 0:
            fout.write(expr+"\n")
    else:
        # try blank
        tryAll(expr+" "+str(curNum), curNum+1, maxNum, fout)
        # try add
        tryAll(expr+"+"+str(curNum), curNum+1, maxNum, fout)
        # try sub
        tryAll(expr+"-"+str(curNum), curNum+1, maxNum, fout)

# open files
fin  = open ('zerosum.in', 'r')
fout = open ('zerosum.out', 'w')

# read N
N = int(fin.readline().strip())

# try all combinations
tryAll("1", 2, N, fout)

# close files
fin.close()
fout.close()
