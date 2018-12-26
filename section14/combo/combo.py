"""
ID: iocoder1
LANG: PYTHON2
TASK: combo
"""

visited = [False]*100*100*100
total = 0

def enum(farmer, comb, N, i):
    global visited
    global total
    if (i == 3):
        # try out a given combination
        val = comb[0] + comb[1]*100 + comb[2]*100*100
        if visited[val] == False:
            visited[val] = True
            total += 1
    else:
        # try 5 states
        comb[i] = (farmer[i] - 2 + N)%N
        enum(farmer, comb, N, i+1)
        comb[i] = (farmer[i] - 1 + N)%N
        enum(farmer, comb, N, i+1)
        comb[i] = farmer[i]
        enum(farmer, comb, N, i+1)
        comb[i] = (farmer[i] + 1 + N)%N
        enum(farmer, comb, N, i+1)
        comb[i] = (farmer[i] + 2 + N)%N
        enum(farmer, comb, N, i+1)

# open files
fin  = open ('combo.in', 'r')
fout = open ('combo.out', 'w')

# read N
N = int(fin.readline())

# read 3 numbers, farmer's lock
farmer = []
for word in fin.readline().split():
    farmer.append(int(word)-1)

# read 3 numbers, master lock
master = []
for word in fin.readline().split():
    master.append(int(word)-1)

# enumerate all possible farmer's lock
enum(farmer, [0, 0, 0], N, 0)

# enumerate all possible master lock
enum(master, [0, 0, 0], N, 0)

# print number of combinations
fout.write(str(total) + "\n")

# close files
fin.close()
fout.close()

