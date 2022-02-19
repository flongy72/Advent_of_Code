#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     25/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():
    total=0
    checksum_list=[]
    sector_id_list=[]
    dict_list=[]
    room_list=[]
    filename = "advent_2016_day4.txt"
    accessMode = "r"
    my_file = open(filename, accessMode)
    data=my_file.read()
    list=data.split("\n")
    for room in list:                                       # break the data string into 3 lists
        checksum=""
        sector_id=""
        room_string=""
        bracket1=room.index("[")
        bracket2=room.index("]")
        for i in range(bracket1+1,bracket2):
            checksum += room[i]
        checksum_list.append(checksum)                      # checksum list
        for i in range(bracket1-3,bracket1):
            sector_id += room[i]
        sector_id=int(sector_id)
        sector_id_list.append(sector_id)                    # sector_id list
        for i in range(0,bracket1-4):
            room_string += room[i]
            new_room_string=room_string.replace("-","")
        room_list.append(new_room_string)                   # room list
    dummy=[]

    for room in room_list:                                      # create a list of dictionaries
        dict_list=[]                                            # which can be ordered and stil keep
        for letter in room:                                     # the same data linked together
            count=room.count(letter)
            count=int(count)
            dummy.append(count)
            if {"letter":letter,"count":count} in dict_list:
                continue
            dict_list.append({"letter":letter,"count":count})

        dict_list.sort(key=dict_sort_count)

        v=len(dummy)                                            # this part was an afterthought
        equal=True                                              # to avoid an anomoly if every count was equal
        for numbers in range(v):                                # and the dictionary automatically
            if numbers>0:                                       # put the order alphabetically
                if dummy[numbers]!=dummy[numbers-1]:            # and so i needed to create
                    equal=False                                 #
        if equal:                                               #
            dict_list.reverse()                                 # an extra reverse

        dict_list.reverse()

        letters=""
        counts=[]
        for i in range(len(dict_list)):                         # split the ordered dictionary
            letter=dict_list[i]
            letters += letter["letter"]                         # into letters
            counts.append(letter["count"])                      # and counts of each letter

        len2 = len(counts)
        re_order_list=[]
        re_order_string=""
        new_string=""
        number=0
        p=0
        for i in range(len2):                                               # arranging the letters list
            if i < p:
                continue
            if i<(len2-1):                                                  # into high count to low count
                if counts[i]==counts[i+1] :
                    number=counts.count(counts[i])                          # and putting into alphabetical
                    p=i+number
                    re_order_string=""                                      # order if several letters had the
                    re_order_list=[]
                    new_string=""
                    for j in range(number):                                 # same count
                        if (i+j)<(len2):
                            re_order_list.append(letters[i+j])
                            re_order_string += letters[i+j]
                    re_order_list.sort()
                    for q in re_order_list:
                        new_string += q
                    letters=letters.replace(re_order_string,new_string)

        x=room_list.index(room)
        checksum=checksum_list[x]
        if letters.startswith(checksum):
            total += sector_id_list[x]
            continue

    print (total)



def dict_sort_count(e):
    return e["count"]





if __name__ == '__main__':
    main()