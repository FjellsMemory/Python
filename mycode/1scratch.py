
"""
list = [2, 3, 4, 5]
newlist = list[:]
list.reverse()
print(list)
print(newlist)
print("tadaaaaa!!!")
list.remove(3)
print(list)


var = "homeboi is a {}"
print(var.format("king"))
"""
'''
def strictly_positive(x):
    """Bitch, i'm a bus, comparing x to zero."""
    if x > 0 and x < 100:
        print(inp, "is strictly positive AND less than 100")


if __name__ == "__main__":
    inp = input("enter a number:  ")
    strictly_positive(float(inp))
'''

def check_for_3(tup: tuple) -> tuple:
    """Take tuple and return tuple only with mod 3 values."""
    tup_of_3s = []
    for n in tup:
        if n % 3 == 0:
            tup_of_3s = tup_of_3s + [n]
    return tuple(tup_of_3s)
