def solution():
    mylist = [2,2,3,4,4,4,5,6,7,7,8,9]
    length_of_list = len(mylist)
    vallycount = 0
    hillcount = 0
    sublist1 = mylist[:2]
    if sublist1[0] == sublist1[1]:
        vallycount += 1
    else:
        hillcount += 1
    sublist2 = mylist[2:4]
    if sublist2[0] == sublist2[1]:
        vallycount += 1
    else:
        hillcount += 1
    sublist3 = mylist[4:6]
    if sublist3[0] == sublist3[1]:
        vallycount += 1
    else:
        hillcount += 1
    sublist4 = mylist[6:8]
    if sublist4[0] == sublist4[1]:
        vallycount += 1
    else:
        hillcount += 1
        sublist5 = mylist[8:10]
    if sublist5[0] == sublist5[1]:
        vallycount += 1
    else:
        hillcount += 1
    sublist6 = mylist[10:12]
    if sublist6[0] == sublist6[1]:
        vallycount += 1
    else:
        hillcount += 1
    print("there will be ",hillcount,"castle on hills")
    print("there will be",vallycount,"castle on vally")

solution()

    

