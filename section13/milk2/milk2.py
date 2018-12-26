"""
ID: iocoder1
LANG: PYTHON2
TASK: milk2
"""

def getStart(slot):
    return slot["start"]

def getEnd(slot):
    return slot["end"]

# open files
fin = open ('milk2.in', 'r')
fout = open ('milk2.out', 'w')

# read N
N = int(fin.readline())

# create a series of slots
slots = []

# add time slots
for i in range(0, N):
    start, end = map(int, fin.readline().split())
    slot = {"start": start, "end": end}
    slots.append(slot)

# sort time slots
slots.sort(key=getStart)

# now merge slots
new_slots = []
aStart = slots[0]["start"];
aEnd   = slots[0]["end"];
for i in range(1, len(slots)):
    # if there is an intersection, do merge
    bStart = slots[i]["start"]
    bEnd   = slots[i]["end"]
    if ((bStart >= aStart and bStart <= aEnd) or
        (aStart >= bStart and aStart <= bEnd)):
        # perform merge        
        aStart = min(aStart, bStart)
        aEnd   = max(aEnd, bEnd)
    else:
        # add last slot and start from a new base
        new_slot = {"start": aStart, "end": aEnd}
        new_slots.append(new_slot)
        aStart = bStart
        aEnd   = bEnd

# add last one
new_slot = {"start": aStart, "end": aEnd}
new_slots.append(new_slot)

# find maximums
max_idle   = 0
max_active = 0
for i in range(len(new_slots)):
    # find max idle time
    if (i > 0):
        idle_time = new_slots[i]["start"] - new_slots[i-1]["end"]
        if (idle_time > max_idle):
            max_idle = idle_time
    # find max active time
    active_time = new_slots[i]["end"] - new_slots[i]["start"]
    if (active_time > max_active):
        max_active = active_time

# print maximums to output file
fout.write("%d %d\n" % (max_active, max_idle))

# close files
fin.close()
fout.close()

