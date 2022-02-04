# myType = int or float or str or bool

def remove_letter(mylist: list, myletter: str) -> list:
    """Remove an element from a list."""
    try:
        while True:
            print(myletter in mylist)
            mylist.remove(myletter)
            print("i'm in da removing block")
    except ValueError:
        pass
    return mylist


usrstr = input("gimme some txt, boi:  ")
strlist = [x for x in usrstr]  # convert txt to list of single chars
strlist.sort()  # group single letters together in list

usrletter = input(f"here's your text in a list.\n{strlist}\n\
pick a letter from it:  ")

strlist = remove_letter(strlist, usrletter)

print("list after removing your selection:\n", strlist)