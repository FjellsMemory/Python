from sys import argv

script, input_file = argv

def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

# i was confused about the following function
# but now i get it, line_count is just an int, passed explicitly
# and readline() just prints a line from a file object - wherever the
# "cursor" just happens to be.  in this case, f.seek(0) was called
# beforehand, and so the cursor was at line 1
def print_a_line(line_count, f):
    print(line_count, f.readline(), end = "")

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind, kind of like a tape.")

rewind(current_file)

print("Let's print three lines.")

current_line = 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)

current_line += 1
print_a_line(current_line, current_file)
