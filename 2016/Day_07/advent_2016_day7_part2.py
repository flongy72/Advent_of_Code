#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      furlo
#
# Created:     27/11/2021
# Copyright:   (c) furlo 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------

def main():

    filename="advent_2016_day7.txt"
    my_file=open(filename,"r")
    data=my_file.read()
    list=data.split("\n")
    supports_ssl=0

    for line in list:
        outside=True
        outside_aba=False
        inside_bab=False

        aba_list=[]
        bab_list=[]
        i=0
        x=len(line)
        while i<x-2:
            aba=""
            bab=""
            if line[i]==line[i+2] and line[i+1]!=line[i] and outside:
                aba += line[i] + line[i+1] + line[i+2]
                if "[" not in aba and "]" not in aba:
                    aba_list.append(aba)
                if aba in bab_list:
                    outside_aba=True

            if line[i]==line[i+2] and line[i+1]!=line[i] and not outside:
                bab += line[i+1] + line[i] + line[i+1]
                if "[" not in bab and "]" not in bab:
                    bab_list.append(bab)
                if bab in aba_list:
                    inside_bab=True

            if line[i]=="[":
                outside=False
                i += 1
                continue

            if line[i]=="]":
                outside=True
                i += 1
                continue
            i += 1
        if inside_bab | outside_aba:
            supports_ssl += 1
    print (supports_ssl)


if __name__ == '__main__':
    main()
