"""
ID: iocoder1
LANG: PYTHON2
TASK: ride
"""

# calculate string value
def calc(name):
    val = 1
    for char in name:
        val *= ord(char)-ord('A')+1
    val %= 47
    return val

# open files
fin = open ('ride.in', 'r')
fout = open ('ride.out', 'w')

# read comet name and group name
lines = fin.read().splitlines();
comet = lines[0]
group = lines[1]

# make decision
if calc(comet) == calc(group):
    fout.write("GO\n")
else:
    fout.write("STAY\n")

# close files
fin.close()
fout.close()

