"""K, this script is supposed to create new files."""


print("K, this script is supposed to create new files.")
while True:
    filename = input("Create file (name):  ")
    if filename.lower() == "quit":
        break
    open(f"c:\\Users\\fjell\\Documents\\Python\\hardcode2\\{filename}", 'x')

# in this short script i see the benefit of creating the variable on which a
# while loop will break or continue INSIDE the while True loop.