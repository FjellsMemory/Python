from math import isclose

def average(mylist: list[float]) -> float:
    sum = 0
    k = 0
    for x in mylist:
        sum = sum + x
        k = k + 1
    return sum/k #  don't forget len() and sum()!!!  :)

def reverse(mylist: list) -> list:
    revlist = []
    k = len(mylist)
    for x in mylist:
        revlist = revlist + [mylist[k-1]]
        k -= 1
    return revlist



dislist = [float(i) for i in range(0, 51, 5)]
print(dislist)
print(average(dislist))
print(reverse(dislist))
