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
location=(x,y)
facing_list=["north","east","south","west"] # just for reference during coding
a=0                                         #indication which wasy i am facing
found=False
visited_blocks=[]
directions=myFile.read()

list_of_directions=directions.split(", ")
print(list_of_directions)

for instruction in list_of_directions:
    if found:
            break
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
    number=int(forward)
    for blocks in range(number):        # loops through each individual move until a location is visited twice
        if a==0:                        # Depending on "a" ( which way i am facing ) the loop adds or subracts from
            y += 1                      # "x" and "y" to move on to next location
        elif a==1:
            x += 1
        elif a==2:
            y -= 1
        else:
            x -= 1
        location=(x,y)
        if location in visited_blocks:      # is the cvurrent location in the visited blocks list
            print( abs(x)+abs(y))
            found=True
            break
        else:

            visited_blocks.append(location) # if not, add the current location to the list and move on

        continue




