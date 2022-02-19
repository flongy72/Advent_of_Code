#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     07/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    with open('advent_2021_day7.txt') as input:
        data=input.read()
        list=data.split(",")
        list.sort()
        max=int(list[-1])
        results_list=[]
        for i in range(max):
            total=0
            for j in list:
                total += abs(int(j)-i)
            results_list.append(total)
        copy=results_list.copy()
        copy.sort()
        print (results_list.index(copy[0]))
        print (copy[0])



if __name__ == '__main__':
    main()
