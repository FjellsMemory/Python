from sys import argv

script, text_file, new_text = argv

#txt = open(text_file)

with open(text_file, "r") as edit:
    print(f"okay pal, i'm gonna open the file {text_file} for you.")
    print("here are the contents:  ")
    print(edit.read())
