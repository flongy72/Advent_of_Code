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
filename = "advent_2016_day3.txt"
accessMode = "r"
my_File = open(filename, accessMode)
data=my_File.read()
x=0
new_list=[]

new_list1=[]
triangles=data.splitlines()                         # whole program is for reading data in colums of 3 instead of line by line
for each_triangle in triangles:
    dimens=each_triangle.split()
    new_list.append(dimens)

for i in range(3):
    for each in new_list:
        new_list1.append(int(each[i]))

b=0
num=len(new_list1)

real_num=int(num/3)

for a in range(real_num):                           # iterating through the new list in groups of 3

    if (new_list1[b])<(new_list1[b+1])+(new_list1[b+2]) and (new_list1[b+1])<(new_list1[b])+(new_list1[b+2]) and (new_list1[b+2])<(new_list1[b])+(new_list1[b+1]):
        x +=1
        b +=3
    else:
        b +=3

print (x)







