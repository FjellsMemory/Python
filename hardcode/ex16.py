from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, "w")

# print("Truncating the file.  See ya!")
# target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line1:  ")
line2 = input("line2:  ")
line3 = input("line3:  ")

print("I'm going to write these to the file.")
'''
###
i'm now going to attempt to rewrite the lines below, which came from the
exercise, with my own understanding of a WITH statement for text file editing
###
target.write(f"{line1}\n{line2}\n{line3}\n")

print("And finally, we close it.")
target.close()
'''

with open(filename, "w") as txt:
    txt.write(f"{line1}\n{line2}\n{line3}\n")
