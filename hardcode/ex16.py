from sys import argv

script, filename = argv

print("")
print("")
print("")

input("?")

print("Opening the file...")
target = open (filename, "w")

print("Truncating the file.  See ya!")
target.truncate()
