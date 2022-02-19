#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     26/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    filename = "advent_2016_day6.txt"
    accessMode = "r"
    my_file = open(filename, accessMode)
    data=my_file.read()
    list=data.split("\n")
    new_list=[[],[],[],[],[],[],[],[]]
    password=""
    for line in list:
        length=len(line)
        for i in range(length):
            new_list[i] += line[i]
    for new_line in new_list:
        dict_list=[]
        letter_list=[]

        for letter in new_line:
            if letter in letter_list:
                continue
            count=new_line.count(letter)
            dict_list.append({"letter":letter,"count":count})
            letter_list.append(letter)
        dict_list.sort(key=my_func)
                                     # this is removed for part 2
        password += dict_list[0]["letter"]
    print (password)

def my_func(e):
    return e["count"]

if __name__ == '__main__':
    main()

