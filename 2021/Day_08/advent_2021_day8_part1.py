#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     08/12/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
     with open('advent_2021_day8.txt') as input:
        data = input.read()
        numbs = {2, 3, 4, 7}
        count = 0
        for line in data.splitlines():
            x, y = line.split(" | ")
            for letters in y.split(" "):
                if len(letters) in numbs:
                    count += 1
        print(count)

if __name__ == '__main__':
    main()
