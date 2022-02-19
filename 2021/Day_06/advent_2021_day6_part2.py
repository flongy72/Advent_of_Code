#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     06/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    list=[3,4,3,1,2]
    highest_initial_number=4
    initial_number_of_fish=len(list)
    number_of_days=float(17)
    i=0
    part_total1=0
    part_total2=0
    while i<number_of_days:

        j=i-(highest_initial_number+1)
        if j%7==0:
            part_total1 += initial_number_of_fish*(2**(int(j/7)))
        if j%9==0:
            part_total2 = initial_number_of_fish*(2**(int(j/9)))


        total=int(part_total1+part_total2+(number_of_days-j))


    print (total)
if __name__ == '__main__':
    main()
