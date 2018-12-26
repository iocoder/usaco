"""
ID: iocoder1
LANG: PYTHON2
TASK: milk
"""

def getKey(farmer):
    return farmer["price"]

# open files
fin  = open ('milk.in', 'r')
fout = open ('milk.out', 'w')

# read N (milk to buy) and M (number of farmers)
N,M = map(int, fin.readline().split())

# loop over M farmers
farmers = []
for i in range(M):
    # read P (price) and A (amount) of farmer
    P,A = map(int, fin.readline().split())
    # create farmer structure
    farmer = {"price": P, "amount": A}
    # add to list
    farmers.append(farmer)

# sort farmers based on their price
farmers.sort(key=getKey)

# buy milk in greedy manner
i = 0
total = 0
while N != 0:
    deal = min(N, farmers[i]["amount"])
    total += deal * farmers[i]["price"]
    i += 1
    N -= deal

# print total money spent
fout.write(str(total) + "\n")

# close files
fin.close()
fout.close()

