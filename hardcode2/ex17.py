from sys import argv, orig_argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how?
indata = open(from_file).read()

print(f"The input file is {len(indata)} bytes long")

print(f"Does the output file exist? {exists(to_file)}")
input("Ready, hit RETURN to continue, CTRL-C to abort. >")

with open(to_file, 'w') as out_file:
    out_file.write(indata)

print("Alright, all done.")