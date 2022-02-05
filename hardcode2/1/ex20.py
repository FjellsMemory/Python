from io import TextIOWrapper
from sys import argv

script, input_file = argv

def print_all(f: TextIOWrapper):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(f):
    print(f.readline(), end="") # file object is read one \n at a time (cursor)

current_file = open(input_file)

print("First let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")  # cursor moved via print_all()

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_file)

current_line += 1
print_a_line(current_file)

current_line += 1
print_a_line(current_file)