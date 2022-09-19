path = "c:\\Users\\fjell\\Documents\\Python\\hardcode2\\ex12.txt"

with open(path, 'r') as x:
    print(x.read())

with open(path, 'a') as x:
    while True:
        usrtxt = (input("Add more txt to da file: (or type 'quit')> "))
        if usrtxt != "quit":
            x.write("\n" + usrtxt)
        else:
            break

print("Your txt has been added... look:")
with open(path, 'r') as x:
    print(x.read())

ans = input("\n" + "Now da real question:  wanna delete this file? (y or n) ")
if ans.lower() == "y":
    with open(path, 'w') as x:
        x.truncate()
else:
    pass
