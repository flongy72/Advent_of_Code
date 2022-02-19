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
filename = "advent_2016_day1.txt"
accessMode = "r"
myFile = open(filename, accessMode)
x,y=0,0

facing_list=["north","east","south","west"] # just for reference during coding
a=0                                         #indication which wasy i am facing


directions=myFile.read()

list_of_directions=directions.split(", ")

for instruction in list_of_directions:

    turn=instruction[0]                  # this takes the first letter "L" or "R" from each instruction

    if turn == "R" and a < 3:            #this if...else is to determine which way i am to turn to face
        a += 1
    elif turn == "R" and a==3:
        a = 0
    elif turn =="L" and a > 0:
        a -= 1
    else:
        a = 3

    forward=instruction[1:]             # this takes the rest of the instruction for the number of steps forward

    if a==0:
        y += int(forward)
    elif a==1:
        x += int(forward)
    elif a==2:
        y -= int(forward)
    else:
        x -= int(forward)



    continue

print ( abs(x) + abs(y))






















