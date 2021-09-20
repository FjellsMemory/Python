# importing argv from sys first step
from sys import argv

# define argv variables, script always being the first
script, filename = argv

# def var txt, which receives .txt file from open()
txt = open(filename)

# fstring prints .txt file's name, a string var - not the file itself!!!
print(f"Here's your file {filename}:")
# .read() method of file class (i guess) "reads" contents of txt filename
# print() of course explicitly prints those contents out
print(txt.read())

'''
here we go through the whole process all over again, this time however
we don't have the filename from an argv argument but from a user prompt pass
'''

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())
