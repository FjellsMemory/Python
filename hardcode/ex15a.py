'''
This is my own variation on the ex15.py exercise, where I replace the text file's contents both via argv AND user input.
'''

from sys import argv

script, text_file, new_text = argv

txt = open(text_file)
print(f"okay pal, i'm gonna open the file {text_file} for you.")
print("here are the contents:  ")
print("  ->", txt.read())
print("now... the text you gave via command line was:")
print("  -> ", new_text,"\n", "i'm now gonna write that to the file.")

with open(text_file, "w") as edit:
    edit.write(f"{new_text}")

txt = open(text_file)
print(f"changes made.  reopening {text_file} for you.")
print("here are the contents now:  ")
print("  ->", txt.read())

input1 = input("last effin step - input your own text here: -> ")
with open(text_file, "w") as edit:
    edit.write(f"{input1}")

txt = open(text_file)
print(f"changes made.  {text_file} now reads:")
print("  ->", txt.read())
