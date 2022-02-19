#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     17/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    pass

if __name__ == '__main__':
    main()
filename = "advent_2016_day2.txt"
accessMode = "r"
myFile = open(filename, accessMode)

array=[[0,0,1,0,0],[0,2,3,4,0],[5,6,7,8,9],[0,"A","B","C",0],[0,0,"D",0,0]]

x,y = 2,0
lines=myFile.read()
new_list=lines.split("\n")
for line in new_list:

    for inst in line:
        if inst=="U":

            if x==0 or array[(x-1)][y]==0:          # check if position at upper edge
                continue                            # if so, leave as is and move on to next instruction
            else:
                x -= 1                                  # if no problems, increase x by 1
                continue

        if inst=="D":

            if x==4 or array[(x+1)][y]==0:                  # as above with lower edge
                continue
            else:
                x += 1
                continue

        if inst=="L":

            if y==0 or array[(x)][y-1]==0:          # as above with left hand edge
                continue
            else:
                y -= 1
                continue

        if inst=="R":

            if y==4 or array[(x)][y+1]==0:                  # as above with right hand edge
                continue
            else:
                y += 1
                continue
    print (array[x][y])
