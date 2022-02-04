"""Removing element from list, list comprehension, more to come..."""


def remove_letter(mylist: list, myletter: str) -> list:
    """Remove an element from a list."""
    try:
        while True:
            mylist.remove(myletter)
    except ValueError:
        pass
    return mylist


strlist = [x for x in (input("gimme some txt, boi:  "))]
strlist.sort()
usrletter = input(f"{strlist}\npick a letter from this alphabet soup:  ")
strlist = remove_letter(strlist, usrletter)

print("list after removing your selection:\n", strlist)