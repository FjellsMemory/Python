path = "c:\\Users\\fjell\\Documents\\Python\\hardcode2\\ex12.txt"

with open(path, 'r') as x:
    print(x.read())

with open(path, 'a') as x:
    x.write("\n" + input("Add more txt to da effin file: > "))

print("Your txt has been added... look:")
with open(path, 'r') as x:
    print(x.read())

ans = input("\nNow da real question:  do ya wanna delete this file? (y or n) ")
if ans.lower() == "y":
    with open(path, 'w')\
            as x:
        x.truncate()
else:
    pass
