"""Keepin up with Thiemann.

def test_result(
    max_points: int,
    percentage: int,
        points: int) -> str:
    passed = (points >= max_points * percentage / 100)
    if passed:
        return "pass"
    else:
        return "fail"


assert(test_result(100, 50, 50) == "pass")
assert(test_result(100, 50, 30) == "fail")
assert(test_result(100, 50, 70) == "pass")


num = 4.0
strnum = (str(num) + "00")
print(len(str(num)))
print(strnum)

"""

mylist = (3, 4, 5, 6)
crazy = "boom"
ziplist = (list(zip(mylist, crazy)))
for i in ziplist:
    ind = ziplist.index(i)
    ziplist[ind] = list(i)
print(ziplist)

mytup = (3, 'b')
print(mytup)
print(list(mytup))