"""
ID: iocoder1
LANG: PYTHON2
TASK: nocows
"""

# RECURRENCE RELATION:
#
# NO OF TRESS OF (N nodes, K levels) =
#   TAKE 1 NODE AS ROOT
#   Possible childrens:
#    subtree(1)    subtree(N-2)
#    subtree(2)    subtree(N-3)
#           ....
#    subtree(N-2)  subtree(1)
#   For each possible pair of subtrees(i,N-1-i), calculate the following:
#     <PART 1>
#     no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-2 levels)
#   + no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-3 levels)
#   + no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-4 levels)
#          ...
#   + no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes,   1 level )
#      + 
#     <PART 2>
#     no_of_trees(i nodes, K-2 levels)*no_of_trees(N-1-i nodes, K-1 levels)
#   + no_of_trees(i nodes, K-3 levels)*no_of_trees(N-1-i nodes, K-1 levels)
#   + no_of_trees(i nodes, K-4 levels)*no_of_trees(N-1-i nodes, K-1 levels)
#          ...
#   + no_of_trees(i nodes,   1 level )*no_of_trees(N-1-i nodes, K-1 levels)
#      +
#     <PART 3>
#     no_of_trees(i nodes, K-1 levels)*no_of_trees(N-1-i nodes, K-1 levels)
#
#   The result of the summation of the three parts is the no of trees that should be returned
#
#   This can be done in a forward-dynamic programming fashion: start at 1,1

# open files
fin  = open ('nocows.in', 'r')
fout = open ('nocows.out', 'w')

# create dp: dp[i][j] = no of trees of i levels and j nodes
dp = [None] * 101
for i in range(0, 101):
    dp[i] = [0] * 201

# create agg: agg[i][j] = no of trees of 1 to i levels and j nodes
agg = [None] * 101
for i in range(0, 101):
    agg[i] = [0] * 201

# first level can consist of only 1 node:
dp[1][1] = 1;
for i in range(1, 101):
    agg[i][1] = 1

# for each no of levels, apply the recurrence:
for k in range(2, 101):
    for n in range(3, 201):
        tot_count = 0
        # loop over possible divisions:
        for i in range(1, n-1):
            left_n = i
            right_n = n-1-i
            # PART1: left_k=k-1, right_k=1-->k-2
            tot_count = tot_count + dp[k-1][left_n]*agg[k-2][right_n]
            # PART2: left_k=1-->k-2, right_k=k-1
            tot_count = tot_count + agg[k-2][left_n]*dp[k-1][right_n]
            # PART3: left_k=k-1, right_k=k-1
            tot_count = tot_count + dp[k-1][left_n]*dp[k-1][right_n]
        # store count
        dp[k][n] = tot_count
        for i in range(k, 101):
            agg[i][n] = agg[i][n] + tot_count

# read N, K
n,k = map(int, fin.readline().strip().split(" "))

# output dp[k][n]
fout.write(str(dp[k][n]%9901)+"\n")

# close files
fin.close()
fout.close()
