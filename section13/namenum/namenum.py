"""
ID: iocoder1
LANG: PYTHON2
TASK: namenum
"""

# conversion from alphabet to num
lookup = ['?']*256
lookup[ord('A')] = '2';
lookup[ord('B')] = '2';
lookup[ord('C')] = '2';
lookup[ord('D')] = '3';
lookup[ord('E')] = '3';
lookup[ord('F')] = '3';
lookup[ord('G')] = '4';
lookup[ord('H')] = '4';
lookup[ord('I')] = '4';
lookup[ord('J')] = '5';
lookup[ord('K')] = '5';
lookup[ord('L')] = '5';
lookup[ord('M')] = '6';
lookup[ord('N')] = '6';
lookup[ord('O')] = '6';
lookup[ord('P')] = '7';
lookup[ord('R')] = '7';
lookup[ord('S')] = '7';
lookup[ord('T')] = '8';
lookup[ord('U')] = '8';
lookup[ord('V')] = '8';
lookup[ord('W')] = '9';
lookup[ord('X')] = '9';
lookup[ord('Y')] = '9';

# open files
din  = open ('dict.txt', 'r')
fin  = open ('namenum.in', 'r')
fout = open ('namenum.out', 'w')

# read cow's id
cowid = fin.readline().strip()

# read lines of dictionary
noAnswer = True
for line in din:
    # get dictionary word
    name = line.strip()
    # convert dictionary word into id
    dictid = ['?']*len(name)
    for i in range(len(name)):
        dictid[i] = lookup[ord(name[i])]
    # compare dictid with cowid
    equal = True
    if len(name) == len(cowid):
        for i in range(len(cowid)):
            if (dictid[i] != cowid[i]):
                equal = False
        if equal == True:
            fout.write(name + "\n")
            noAnswer = False
    else:
        equal = False

# print NONE if no answer
if noAnswer == True:
    fout.write("NONE\n")

# close files
din.close()
fin.close()
fout.close()

