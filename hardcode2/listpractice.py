usrstr = input("gimme some txt, boi:  ")
strlist = [x for x in usrstr]  # convert txt to list of single chars
strlist.sort()  # group single letters together in list

usrletter = input(f"here's your text in a list.\n{strlist}\n\
pick a letter from it:  ")

if usrletter in strlist:
    loopnum = 1
    while True:
        if usrletter in strlist:
            print("removal loop number " + str(loopnum))
            indx = strlist.index(usrletter)
            strlist.pop(indx)
            loopnum += 1
        else:
            break
else:
    pass

print("list after removing your selection:\n", strlist)