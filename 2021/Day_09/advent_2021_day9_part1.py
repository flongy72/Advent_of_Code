#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     09/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    low_points=[]
    sum=0
    with open('advent_2021_day9.txt') as input:
        data=input.read()
        list=[[int(y) for y in x] for x in data.splitlines()]
        print(list)
        for x in range(len(list)):
            for y in range(len(list[x])):
                if x==0 and y==0:
                    if list[x][y+1]>list[x][y] and list[x+1][y]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if x==0 and y==len(list[x])-1:
                    if list[x][y-1]>list[x][y] and list[x+1][y]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if x==len(list)-1 and y==0:
                    if list[x][y+1]>list[x][y] and list[x-1][y]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if x==len(list)-1 and y==len(list[x])-1:
                    if list[x-1][y]>list[x][y] and list[x][y-1]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if x==0 and y!=0 and y!=len(list[x])-1:
                    if list[x][y+1]>list[x][y] and list[x][y-1]>list[x][y] and list[x+1][y]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if x==len(list)-1 and y!=0 and y!=len(list[x])-1:
                    if list[x][y+1]>list[x][y] and list[x][y-1]>list[x][y] and list[x-1][y]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if y==0 and x!=0 and x!=len(list)-1:
                    if list[x-1][y]>list[x][y] and list[x+1][y]>list[x][y] and list[x][y+1]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if y==len(list[x])-1 and x!=0 and x!=len(list)-1:
                    if list[x-1][y]>list[x][y] and list[x+1][y]>list[x][y] and list[x][y-1]>list[x][y]:
                        low_points.append(list[x][y]+1)
                if x!=0 and y!=0 and x!=len(list)-1 and y!=len(list[x])-1:
                    if list[x+1][y]>list[x][y] and list[x-1][y]>list[x][y] and list[x][y+1]>list[x][y] and list[x][y-1]>list[x][y]:
                        low_points.append(list[x][y]+1)
        for i in low_points:
            sum += i

        print(sum)





if __name__ == '__main__':
    main()
