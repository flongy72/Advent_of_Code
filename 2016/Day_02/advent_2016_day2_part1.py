#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     16/11/2021
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
line_list=[]
x=5

lines=myFile.read()
new_list=lines.split("\n")
for line in new_list:
    for inst in line:

        if inst=="U":
            if x in (4,5,6,7,8,9):
                x -= 3
                continue
        if inst=="D":
            if x in (1,2,3,4,5,6):
                x += 3
            continue
        if inst=="R":
            if x in (1,2,4,5,7,8):
                x += 1
            continue
        if inst=="L":
            if x in (2,3,5,6,8,9):
                x -= 1
            continue
    print(x)




