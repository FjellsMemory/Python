from sys import argv

filename, x, y = argv

tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

print(f"btw, the name of this file is {filename}")
print("{} this shit out. the meaning of life is {}".format(x, y),
      end=".")

mylist = [x for x in range(0, 12)]
mylist.sort(reverse=True)
print(mylist)