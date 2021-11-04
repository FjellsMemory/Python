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
"""

num = 4.0
strnum = (str(num) + "00")
print(len(str(num)))
print(strnum)