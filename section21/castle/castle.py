"""
ID: iocoder1
LANG: PYTHON2
TASK: castle
"""

def printGraph(nodes):
        for src in nodes:
            for dst in src["adj"]:
                print "(",src["row"],src["col"],") -> (",dst["row"],dst["col"],")"

def floodFill(nodes, new_component):
    num_visited = 1
    while num_visited != 0:
        num_visited = 0
        for i in nodes:
            if i["cmp"] == -2:
                num_visited = num_visited + 1
                i["cmp"] = new_component
                for j in i["adj"]:
                    if j["cmp"] == 0:
                        j["cmp"] = -2

def findComponents(nodes):
    num_components = 0
    for i in nodes:
        i["cmp"] = 0
    for i in nodes:
        if i["cmp"] == 0:
            num_components += 1
            i["cmp"] = -2
            floodFill(nodes, num_components)    
    sizes = [0] * (num_components+1)
    for i in nodes:
        sizes[i["cmp"]] += 1
    return sizes

# open files
fin  = open ('castle.in', 'r')
fout = open ('castle.out', 'w')

# read N and M
N,M = map(int, fin.readline().split())
nodes = [{} for i in range(M * N)]
walls = []

# read castle rooms
for i in range(M):
    words = fin.readline().split()
    for j in range(N):
        # read walls
        senw = int(words[j])
        west = senw & 1
        nort = senw & 2
        east = senw & 4
        sout = senw & 8
        # add current node to list of nodes
        nodes[i*N+j]["row"] = i
        nodes[i*N+j]["col"] = j
        nodes[i*N+j]["adj"] = []
        # add walls between the rooms to list of walls
        if west == 0:
            # we've got no wall to the west
            nodes[i*N+j]["adj"].append(nodes[(i)*N+(j-1)])
        elif j != 0:
            # we've got a  wall to the west
            walls.append({"s":nodes[i*N+j], "d":nodes[(i)*N+(j-1)], "t":"w"})
        if (nort == 0):
            # we've got no wall to the north
            nodes[i*N+j]["adj"].append(nodes[(i-1)*N+(j)])
        elif i != 0:
            # we've got a  wall to the north
            walls.append({"s":nodes[i*N+j], "d":nodes[(i-1)*N+(j)], "t":"n"})            
        if (east == 0):
            # we've got no wall to the east
            nodes[i*N+j]["adj"].append(nodes[(i)*N+(j+1)])
        elif j < N-1:
            # we've got a  wall to the east
            walls.append({"s":nodes[i*N+j], "d":nodes[(i)*N+(j+1)], "t":"e"}) 
        if (sout == 0):
            # we've got no wall to the south
            nodes[i*N+j]["adj"].append(nodes[(i+1)*N+(j)])
        elif i < M-1:
            # we've got a  wall to the south
            walls.append({"s":nodes[i*N+j], "d":nodes[(i+1)*N+(j)], "t":"s"}) 
        # check walls

# compute base components number
base_cmp = findComponents(nodes)
base_max = max(base_cmp)

# try to add add an edge every time and see what happens.
max_cmp = 0
max_num = 1000000000
for wall in walls:
    # get node info
    cur_row = wall["s"]["row"]
    cur_col = wall["s"]["col"]
    # are both guys in the same component?
    cur_max_cmp = 0
    if wall["s"]["cmp"] == wall["d"]["cmp"]:
        # same comp
        cur_max_cmp = base_cmp[wall["s"]["cmp"]]
    else:
        # two diff components
        cur_max_cmp = base_cmp[wall["s"]["cmp"]] + base_cmp[wall["d"]["cmp"]]
    # compare
    if (cur_max_cmp > max_cmp):
        max_num = 1000000000
        max_cmp = cur_max_cmp
    # add to list of maxes if it is a maximum    
    if (cur_max_cmp == max_cmp):
        # priority first for "farthest to the west"
        m = cur_col*M*4
        # then if tied, "farthest to the south"
        m += (M-1-cur_row)*4
        # then if tied, N then E
        if wall["t"] == "n":
            m += 0
        elif wall["t"] == "e":
            m += 1
        elif wall["t"] == "s":
            m += 2
        elif wall["t"] == "w":
            m += 3
        # if m < max_num, set it
        if (m < max_num):
            max_num = m

# extract information about maximum module
max_sid = ""
if ((max_num%4) == 0):
    max_sid = "N"
elif ((max_num%4) == 1):
    max_sid = "E" 
elif ((max_num%4) == 2):
    max_sid = "S" 
elif ((max_num%4) == 3):
    max_sid = "W" 
max_num /= 4
max_row = M-1-(max_num%M) + 1
max_num /= M
max_col = max_num + 1

# print settings
fout.write(str(len(base_cmp)-1) + "\n")
fout.write(str(base_max) + "\n")
fout.write(str(max_cmp) + "\n")
fout.write(str(max_row) + " " + str(max_col) + " " + max_sid + "\n")

# close files
fin.close()
fout.close()

