"""
ID: iocoder1
LANG: PYTHON2
TASK: barn1
"""

def cloneBoards(boards):
    ret = []
    for i in range(len(boards)):
        board = {"start": boards[i]["start"],
                 "end"  : boards[i]["end"]}
        ret.append(board)
    return ret

def getLargestGaps(stalls, board):
    cur_start = -1
    max_size  = 0
    max_gaps  = []
    for i in range(board["start"], board["end"]+1):
        if (stalls[i] == True and cur_start != -1):
            size = i-cur_start
            if size > max_size:
                max_size = i-cur_start
                max_gaps = []
            if size == max_size:
                max_gaps.append({"start": cur_start, "end": i-1, "size": i-cur_start})
            cur_start = -1
        elif stalls[i] == False:
            if cur_start == -1:
                cur_start = i                
    return max_gaps

def getNumBlockedStalls(stalls, boards):
    total = 0
    for i in range(len(boards)):
        total += boards[i]["end"] - boards[i]["start"] + 1
    return total

def splitBoards(stalls, boards):
    # reached maximum?
    if len(boards) == M:
        return getNumBlockedStalls(stalls, boards)
    # find board with largest gap size
    board_idx        = 0
    largest_gaps     = []
    largest_gap_size = 0
    for i in range(len(boards)):
        cur_gaps = getLargestGaps(stalls, boards[i])
        if (len(cur_gaps) and cur_gaps[0]["size"] > largest_gap_size):
            largest_gaps     = cur_gaps
            largest_gap_size = cur_gaps[0]["size"]
            board_idx        = i
    # no gaps?
    if largest_gap_size == 0:
        return getNumBlockedStalls(stalls, boards)
    # break the board into two boards in a back-tracking manner:
    min_blocked = 100000
    for i in range(len(largest_gaps)):
        cur_gap = largest_gaps[i]
        new_boards = cloneBoards(boards)
        new_board = {"start": cur_gap["end"]+1, 
                     "end"  : boards[board_idx]["end"]}
        new_boards[board_idx]["end"] = cur_gap["start"]-1
        new_boards.append(new_board)
        num_blocked = splitBoards(stalls, new_boards)
        if (num_blocked < min_blocked):
            min_blocked = num_blocked
            break
    return min_blocked

# open files
fin  = open ('barn1.in', 'r')
fout = open ('barn1.out', 'w')

# read parameters:
# M: maximum number of boards
# S: total number of stalls
# C: number of occupied stalls
M,S,C = map(int, fin.readline().split())

# read stall information
stalls = [False]*S
first  = 10000
last   = 0
for i in range(C):
    idx = int(fin.readline())-1
    stalls[idx] = True
    if idx < first:
        first = idx
    if idx > last:
        last = idx

# create first board
boards = [{"start": first, "end": last}]

# try to split until we reach maximum
blocked = splitBoards(stalls, boards)

# print out number of stalls blocked by boards
fout.write(str(blocked) + "\n")

# close files
fin.close()
fout.close()

