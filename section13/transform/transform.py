"""
ID: iocoder1
LANG: PYTHON2
TASK: transform
"""

def createSquare(N):
    square = [None]*N;
    for i in range(N):
        square[i] = ['?']*N;
    return square

def readSquare(fd, N):
    square = createSquare(N)
    for i in range(N):
        line = fd.readline().strip();
        for j in range(N):
            square[i][j] = line[j]
    return square

def cloneSquare(src, N):
    dest = createSquare(N)
    for i in range(N):
        for j in range(N):
            dest[i][j] = src[i][j]
    return dest

def compareSquare(src, dest, N):
    equal = True
    for i in range(N):
        for j in range(N):
            if (src[i][j] != dest[i][j]):
                equal = False
    return equal

def rotateSquare(src, N):
    # just create a clone from "src"
    dest = cloneSquare(src, N)
    # perform the rotation
    # before:
    # +---+---+---+
    # | 1 | 2 | 3 |
    # +---+---+---+
    # | 4 | 5 | 6 |
    # +---+---+---+
    # | 7 | 8 | 9 |
    # +---+---+---+
    #
    # after:
    # +---+---+---+
    # | 7 | 4 | 1 |
    # +---+---+---+
    # | 8 | 5 | 2 |
    # +---+---+---+
    # | 9 | 6 | 3 |
    # +---+---+---+
    for i in range(N):
        for j in range(N):
            dest[i][j] = src[N-j-1][i]
    # return the rotated matrix
    return dest


def reflectSquare(src, N):
    # just create a clone from "src"
    dest = cloneSquare(src, N)
    # perform the reflection
    # before:
    # +---+---+---+
    # | 1 | 2 | 3 |
    # +---+---+---+
    # | 4 | 5 | 6 |
    # +---+---+---+
    # | 7 | 8 | 9 |
    # +---+---+---+
    #
    # after:
    # +---+---+---+
    # | 3 | 2 | 1 |
    # +---+---+---+
    # | 6 | 5 | 4 |
    # +---+---+---+
    # | 7 | 8 | 7 |
    # +---+---+---+
    for i in range(N):
        for j in range(N):
            dest[i][j] = src[i][N-j-1]
    return dest

# open files
fin = open ('transform.in', 'r')
fout = open ('transform.out', 'w')

# read N
N = int(fin.readline())

# read the "before" and "after" squares
before    = readSquare(fin, N);
after     = readSquare(fin, N);
transform = 0

# try 90-degree rotation
if transform == 0:
    rotate90 = rotateSquare(before, N)
    if compareSquare(after, rotate90, N):
        transform = 1

# try 180-degree rotation
if transform == 0:
    rotate180 = rotateSquare(rotate90, N)
    if compareSquare(after, rotate180, N):
        transform = 2

# try 270-degree rotation
if transform == 0:
    rotate270 = rotateSquare(rotate180, N)
    if compareSquare(after, rotate270, N):
        transform = 3

# try reflection
if transform == 0:
    reflect = reflectSquare(before, N)
    if compareSquare(after, reflect, N):
        transform = 4

# try reflection+rotate90
if transform == 0:
    reflect90 = rotateSquare(reflect, N)
    if compareSquare(after, reflect90, N):
        transform = 5

# try reflection+rotate180
if transform == 0:
    reflect180 = rotateSquare(reflect90, N)
    if compareSquare(after, reflect180, N):
        transform = 5

# try reflection+rotate270
if transform == 0:
    reflect270 = rotateSquare(reflect180, N)
    if compareSquare(after, reflect270, N):
        transform = 5

# try no change
if transform == 0:
    if compareSquare(after, before, N):
        transform = 6

# try invalid
if transform == 0:
    transform = 7

# output transform number
fout.write(str(transform) + "\n")

# close files
fin.close()
fout.close()

