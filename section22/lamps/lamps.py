"""
ID: iocoder1
LANG: PYTHON2
TASK: lamps
"""

# switch a lamp
def switch(lamps, i):
    if lamps[i] == 'O':
        lamps[i] = 'F'
    elif lamps[i] == 'F':
        lamps[i] = 'O'

# commands
def apply_cmd(lamps, cmd):
    # loop over all elements
    for i in range(0, len(lamps)):
        # process the element depending on the command type
        if cmd == 0:
            # switch any element
            switch(lamps, i)
        elif cmd == 1:
            # switch if odd
            if ((i+1)%2) == 1:
                switch(lamps, i)
        elif cmd == 2:
            # switch if even
            if ((i+1)%2) == 0:
                switch(lamps, i)
        elif cmd == 3:
            # switch if 3K+1
            if (i%3)==0:
                switch(lamps, i)

# check if happy ending
def happy_end(lamps):
    valid = True
    for lamp in lamps:
        if lamp == 'F':
            valid = False
            break
    return valid

# compare two solutions:
def is_greater(sol1, sol2):
    for i in range(0, len(sol1)):
        if (sol1[i] == 'O' and sol2[i] == 'F'):
            return 1
        elif (sol1[i] == 'F' and sol2[i] == 'O'):
            return -1
    return 0 # equal

# add solution in order
def add_sol(sols, new_sol):
    indx = 0
    for i in range(0, len(sols)):
        # loop until sols[i] is greater than new_sol
        rel = is_greater(sols[i], new_sol)
        # solution exist?
        if rel == 0:
            return
        # sols[i] > new_sol? stop here
        if rel == 1:
            indx = i
            break
        else:
            indx = i+1
    sols.insert(indx, new_sol)

# open files
fin  = open ('lamps.in', 'r')
fout = open ('lamps.out', 'w')

# read N
N = int(fin.readline())

# read C
C = int(fin.readline())

# initialize lamp states
last_lamps = ['U']*N

# read ON lamps
indx_list = map(int, fin.readline().split())
for indx in indx_list[:-1]:
    last_lamps[indx-1] = 'O'

# read OFF lamps    
indx_list = map(int, fin.readline().split())
for indx in indx_list[:-1]:
    last_lamps[indx-1] = 'F'
    
# all possible combs
combs = [[], [0], [1], [2], [3], [0,1], [0,2], [0,3], [1,2], [1,3], [2,3],
         [0,1,2], [0,1,3], [0,2,3], [1,2,3], [0,1,2,3]]

# all solutions
sols = []

# try all possible combs:
for comb in combs:
    # calculate no of distinct commands
    no_steps = len(comb)
    # all other commands must cancel each other
    if C >= no_steps and ((C-no_steps)%2)==0:
        # this comb is a possible combination. clone last_lamps for modification
        lamps = list(last_lamps)
        # simulate the changes
        for cmd in comb:
            apply_cmd(lamps, cmd)
        # happy ending?
        if happy_end(lamps):
            # create a new all-ON lamps
            sol = ['O'] * N
            # apply commands in row
            for cmd in comb:
                apply_cmd(sol, cmd)
            # add solution to list of sols
            add_sol(sols, sol)

# print all sols
for sol in sols:
    for lamp in sol:
        if lamp == 'O':
            fout.write("1")
        else:
            fout.write("0")
    fout.write("\n")

# no sols?
if len(sols) == 0:
    fout.write("IMPOSSIBLE\n")

# close files
fin.close()
fout.close()

