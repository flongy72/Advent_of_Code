#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     03/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    gamma_rate=""
    epsilon_rate=""
    with open('advent_2021_day3.txt') as input:
        data=input.read()
        list = ["" for _ in range(12)]
        for line in data.splitlines():
            for digit in range(len(line)):
                list[digit] +=(line[digit])
        for string in list:
            ones=string.count("1")
            zeros=string.count("0")
            if ones>zeros:
                gamma_rate += "1"
                epsilon_rate += "0"
            else:
                gamma_rate += "0"
                epsilon_rate += "1"
        dec_gamma=int(gamma_rate,2)
        dec_eps=int(epsilon_rate,2)
        answer = dec_gamma*dec_eps
        print(answer)




if __name__ == '__main__':
    main()
