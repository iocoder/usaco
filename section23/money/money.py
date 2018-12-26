"""
ID: iocoder1
LANG: PYTHON2
TASK: money
"""

# recursive solution
def recSol(coinVec, coins, curCoin, rem, dp):
    count = 0
    if dp[rem][curCoin] != -1:
        return dp[rem][curCoin]
    if curCoin == len(coins):
        if rem == 0:
            # valid combination
            count = 1
    else:
        # how many coins can be consumed?
        maxQu = rem/coins[curCoin]
        for i in range(0, maxQu+1):
            coinVec[curCoin] = i
            newRem = rem - coins[curCoin]*i
            count = count + recSol(coinVec, coins, curCoin+1, newRem, dp)
        coinVec[curCoin] = 0
    dp[rem][curCoin] = count
    return count

# open files
fin  = open ('money.in', 'r')
fout = open ('money.out', 'w')

# read N and V
V, N = map(int, fin.readline().split(' '))

# read coins
coins = [None]*V
curIdx = 0
for line in fin:
    for coin in line.split(' '):
        coins[curIdx] = int(coin)
        curIdx = curIdx + 1

# coin vector
coinVec = [0] * V
dp = [None] * (N+1)
for i in range(0, N+1):
    dp[i] = [-1] * (V+1)
    
# done
count = recSol(coinVec, coins, 0, N, dp)
fout.write(str(count)+"\n")

# close files
fin.close()
fout.close()
