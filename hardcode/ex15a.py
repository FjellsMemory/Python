from sys import argv

script, text_file, new_text = argv

txt = open(text_file)
print(f"okay pal, i'm gonna open the file {text_file} for you.")
print("here are the contents:  ")
print("\t", txt.read())
print(f"now... the text you gave via command line was:\n")
print(new_text, "i'm now gonna write that to the file.")

with open(text_file, "w") as edit:
    edit.write(f"{new_text}")

txt = open(text_file)
print(f"changes made.  reopening {text_file} for you.")
print("here are the contents now:  ")
print("\t", txt.read())
