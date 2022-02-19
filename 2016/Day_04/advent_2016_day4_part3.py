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
    total=0

    checksum_list=[]
    sector_id_list=[]
    dict_list=[]
    room_list=[]
    decrypted_list=[]
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

        room_list.append(room_string)                   # room list



    for room in room_list:
        decrypted=""
        index=room_list.index(room)
        forward=sector_id_list[index]
        forward=float(forward)
        x=forward/26
        x=int(x)
        move = forward % 26
        move=int(move)

        for letter in room:
            if letter=="-":
                decrypted += " "
                continue

            new_letter=shift(letter,move)
            decrypted += new_letter
        decrypted_list.append(decrypted)

        if decrypted=="northpole object storage":
            print (forward)



def shift(x,y):
    alphabet="abcdefghijklmnopqrstuvwxyz"
    position=alphabet.index(x)
    if y==0:
        return x
    position=alphabet.index(x)
    new_position=(position +y) % len(alphabet)

    return alphabet[new_position]


if __name__ == '__main__':
    main()
