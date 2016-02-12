#!/usr/bin/env python3
# Generates a list of "slides", each a list containing a number of "tiles".
# Each tile has an "index" which represents a "blank" or an image

import random, json
from copy import deepcopy

FRAMECOUNT = 900

with open("sources.json") as sourcefile:
    sources = json.load(sourcefile)
FRUITCOUNT = len(sources)

def main():

    initfruit = newfruit()
    hardframe0 = [[initfruit]]
    hardframe1 = [[hardframe0[0][0], newfruit()]]
    hardframe2 = [hardframe1[0],[newblank(),newfruit()]]
    hardframe3 = [[hardframe2[0][0], hardframe2[0][1], newblank()],[newblank(), hardframe2[1][1], newblank()],[newblank(),newblank(),newfruit()]]

    # This framelist hardcodes the first few shapes, and is just me experimenting
    framelist = [hardframe0,hardframe1,hardframe2]

    while len(framelist) < FRAMECOUNT:
        current = framelist[len(framelist)-1]

        newframe = deepcopy(current)

        rows = len(newframe)
        cols = len(newframe[0])

        switch = random.randint(1,4)

        # Add row:        
        if ((rows == 1  and (cols >= 2)) or (rows == 2 and cols == 3)) and switch == 1:
            newframe = newrow(newframe)

        # Add column:
        elif (cols == 1 or cols == 2) and (rows == 2 or rows == 3) and switch == 2:
            newframe = newcol(newframe)

        # Drop row:
        elif ((rows == 2 and cols == 3) or rows == 3) and switch == 3:
            newframe = newframe[:-1]

        # Drop column:
        elif ((cols == 2 and rows == 1) or (cols == 3 and rows == 2)) and switch == 4:
            newframe = dropcol(newframe)

        newframe = modify(newframe,random.randint(1,4))

        framelist.append(newframe)

    with open("slide_deck.json",'w') as outfile:
        json.dump(framelist, outfile)

def newtile():
    if random.choice((0,1,2)):
        return newfruit()
    else:
        return newblank()

def newfruit():
    return random.randint(1,FRUITCOUNT)

def newblank():
    return -1

def newrow(frame):
    row = []
    for _ in range(len(frame[0])):
        row.append(newtile())
    frame.append(row)
    return frame

def newcol(frame):
    for row in frame:
        row.append(newtile())
    return frame

def dropcol(frame):
    newframe = []
    for row in frame:
        newframe.append(row[:-1])
    return newframe

def modify(frame, changes):
    
    for _ in range(changes):    
        i = random.randint(0,len(frame)-1)
        j = random.randint(0,len(frame[0])-1)

        if frame[i][j] > 0:
            frame[i][j] = newblank()
        else:
            frame[i][j] = newfruit()

    if len(frame) == 0 and len(frame[0]) == 0 and frame[0][0] == -1:
        frame[0][0] = newfruit()

    return frame

if __name__ == "__main__":
    main()
