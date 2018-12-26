"""
ID: iocoder1
LANG: PYTHON2
TASK: sort3
"""

# check if all cross counts are zeros
def allzero(cross):
    if cross[1][2] != 0:
        return False
    if cross[1][3] != 0:
        return False
    if cross[2][1] != 0:
        return False
    if cross[2][3] != 0:
        return False
    if cross[3][1] != 0:
        return False
    if cross[3][2] != 0:
        return False
    return True

# open files
fin  = open ('sort3.in', 'r')
fout = open ('sort3.out', 'w')

# read N
N = int(fin.readline())

# initialize lists
nums  = [0] * N
count = [0] * 5
cross = [None] * 5

# initialize cross
for i in range(5):
    cross[i] = [0] * 5

# read numbers
for i in range(N):
    val = int(fin.readline())
    nums[i] = val
    count[val] = count[val]+1

# calculate cross counts
cur_num = 1
for i in range(N):
    while count[cur_num] == 0:
        cur_num = cur_num + 1
    val = nums[i]
    cross[val][cur_num] = cross[val][cur_num] + 1
    count[cur_num] = count[cur_num] - 1
    
# loop until all zeros
swaps = 0
while allzero(cross) == False:
    # do one swap
    swaps = swaps + 1
    # direct swap?
    if cross[1][2] > 0 and cross[2][1] > 0:
        cross[1][2] = cross[1][2] - 1
        cross[2][1] = cross[2][1] - 1
        cross[1][1] = cross[1][1] + 1
        cross[2][2] = cross[2][2] + 1
        continue
    if cross[1][3] > 0 and cross[3][1] > 0:
        cross[1][3] = cross[1][3] - 1
        cross[3][1] = cross[3][1] - 1
        cross[1][1] = cross[1][1] + 1
        cross[3][3] = cross[3][3] + 1
        continue
    if cross[2][3] > 0 and cross[3][2] > 0:
        cross[2][3] = cross[2][3] - 1
        cross[3][2] = cross[3][2] - 1
        cross[2][2] = cross[2][2] + 1
        cross[3][3] = cross[3][3] + 1
        continue
    # indirect swap?
    found = False
    for i in range(1, 4):
        for j in range(1, 4):
            if i != j and cross[i][j] > 0:
                i1 = i
                j1 = j
                found = True
                break
        if found == True:
            break
    # second element
    found = False
    for i in range(1, 4):
        for j in range(1, 4):
            if i == i1 and j == j1:
                continue
            if i != j and cross[i][j] > 0:
                i2 = i
                j2 = j
                found = True
                break
        if found == True:
            break
    # swap them
    cross[i1][j1] = cross[i1][j1] - 1
    cross[i2][j2] = cross[i2][j2] - 1
    cross[i1][j2] = cross[i1][j2] + 1
    cross[i2][j1] = cross[i2][j1] + 1

# print moves
fout.write(str(swaps) + "\n")

# close files
fin.close()
fout.close()

