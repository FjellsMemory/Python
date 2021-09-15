"""
This code got written a few times, like 3 different ways to do same thing, so
it's a bit of a mess.  Suffice to say I learned a lot while doing it.
1) Solution long-hand all globally
2) Outsourced main swap to a function item_replace()
3) Nixed the use of the function to test out converting whole list to a list of
    strings and then testing them against 'match' explicitly
"""

def item_replace(new_entry: str, find_me: str, in_dis_list: list) -> list:
    for i in range(len(in_dis_list)):
        if str(in_dis_list[i]) == find_me:
            in_dis_list[i] = new_entry
    return in_dis_list
    # rewrote the "replace in list" code as function like boss

mylist = [True, 20, "Yo", 9/4]
print("\n")
countme = "".join(str(x)for x in mylist)
starz_num = len(countme)
print((13 * "*") + ("*" * starz_num))
print("*" + " " + " | ".join(str(x)for x in mylist), "*")
print((13 * "*") + ("*" * starz_num), "\n")

print("Above is a list of 4 items.")
u_choose = input("Add one more item to the list:  ")
print(f"Legend.  You picked '{u_choose}'.")
match = input(f"Now pick one of the original 4 for {u_choose} to replace:  ")

str_list = list(str(x)for x in mylist)
while match not in str_list:
    print(f"{match} wasn't on the goddam list.  Retype exactly one from below.")
    print(" | ".join(str(x)for x in mylist))
    match = input("Choose now:  ")

str_list = list(str(x)for x in mylist)
indexo = str_list.index(match)
mylist[indexo] = u_choose
updated_list = mylist
#updated_list = item_replace(u_choose, match, mylist)

countme = "".join(str(x)for x in updated_list) # turn finished outputable list into a single unbroken string for counting up.
starz_num = len(countme) # base number of asterisks to print on countme + 9
print("Here ya go bitches.  Peace out. \n")
print((13 * "*") + ("*" * starz_num))
print("*" + " " + " | ".join(str(x)for x in updated_list), "*")
print((13 * "*") + ("*" * starz_num), "\n")

# Ta daaaaaaa!!!  :)
