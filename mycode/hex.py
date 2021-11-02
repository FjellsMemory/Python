"""Should take a number and convert it to hexadecimal."""


def crunch(danum: int) -> list:
    """Turn base-10 int into a base-16 int list."""
    qlist = []
    while danum != 0:
        qlist.insert(0, danum % 16)
        danum //= 16
    return qlist


def translate(alist: list) -> str:
    """Turn base-16 int list into a proper hex str."""
    for elem in alist:
        if elem == 10:
            alist[alist.index(elem)] = "a"
        elif elem == 11:
            alist[alist.index(elem)] = "b"
        elif elem == 12:
            alist[alist.index(elem)] = "c"
        elif elem == 13:
            alist[alist.index(elem)] = "d"
        elif elem == 14:
            alist[alist.index(elem)] = "e"
        elif elem == 15:
            alist[alist.index(elem)] = "f"
        else:
            pass
    hexstr = "".join(str(x) for x in alist)
    return hexstr


usrint = int(input("Enter a natural number:  "))
print("0x" + translate(crunch(usrint)))
print(hex(usrint))
