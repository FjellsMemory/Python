"""Do random shit."""
from math import isclose
nums = int | float

def average(mylist: list[nums]) -> nums:
    """Do bullshit."""
    sum = 0
    k = 0
    for x in mylist:
        sum = sum + x
        k = k + 1
    return sum / k  # don't forget len() and sum()!!!  :)


def reverse(mylist: list[nums]) -> list:
    """Do more bullshit."""
    revlist = []
    k = len(mylist)
    for x in mylist:
        revlist = revlist + [mylist[k - 1]]
        k -= 1
    return revlist


def only_positive(mylist: list[nums]) -> list[int]:
    """Do more bullshit."""
    poslist = []
    for x in mylist:
        if x > 0:
            poslist = poslist + [x]
    return poslist


dislist = [float(i) for i in range(-50, 51, 5)]
print(dislist)
print(average(dislist))
print(reverse(dislist))
print(only_positive([x for x in dislist]))
