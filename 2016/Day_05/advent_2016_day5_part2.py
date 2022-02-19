#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     23/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import hashlib

def main():
    i=0
    x=0
    dict_list=[]
    position_list=[]
    password=""
    while x<8:
        i=str(i)
        user = ("wtnhxymk" + i)
        h = hashlib.md5(user.encode())
        h2 = h.hexdigest()
        if h2.startswith("00000"):
            print (i)
            position=h2[5]
            character=h2[6]
            if position.isdigit() and int(position)<8 and int(position) not in position_list:
                position=int(position)
                dict_list.append({"position":position,"character":character})
                position_list.append(position)
                x += 1
                print(position_list)

            i = int(i)
            i += 1
            continue
        i=int(i)
        i += 1

    dict_list.sort(key=my_func)
    print (dict_list)

    for i in dict_list:

        password += i["character"]
    print (password)

def my_func(e):
    return e["position"]

if __name__ == '__main__':
    main()

