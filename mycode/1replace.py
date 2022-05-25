"""
THIS WAS A FUCKING RIGHTEOUS VICTORY IN SELF-STYLED INGENUITY.

Basically, I challenged myself, using what I'd just learned of creating lists
from DataCamp, to replace an element in a mixed list with something of a user's
own choosing.  To up the difficulty, I created a list with ints, floats, bools,
strings, and concantenated strings.
"""

##########

a, b, c, d, e = 16, 45.7, True, "Spencer Davis", "e" * 3
mylist3 = [a, b, c, d, e]  # initial list creation

###########

print("Okay, homeboy, here's a list with 5 elements")
print(" | ".join(str(x) for x in mylist3))  # present list WITHOUT BRACKETS!!

# NOT ONLY DID I PRESENT THE LIST WITHOUT BRACKETS, BUT ALSO BEING SEPARATED
# BY A DASH (|) WITH SPACES ON BOTH SIDES.  THIS WAS DONE WITH THE string.join
# METHOD AS FOLLOWS:  print(" | ".join(str(x) for x in mylist3))

input1 = input("Go ahead and type a new element:  ")  # replacement input
mod_text = "{}???  Can't believe you chose {}!"  # elite use of format text
print(mod_text.format(input1, input1))  # further elite usage with .format method
match = input(f"Now pick one of the five originals to replace with {input1}:  ")

''' here's where the magic starts.  i realized the input from the user was
automatically a string.  but some elements in my list were ints, floats, bools.
so i was stumped how to test the string against a list of mixed types.  then it
hit me:  convert the list to strings, then compare the input string against
the converted list of strings.  then if a match was found, use the index
number of the match to replace the element at that index in the original list
with the input string.  the first section below ensures that the user's input
matches something in the original list EXACTLY vis a vis spelling.  the next
section in one fell swoop does the comparing and replacing in 3 lines, 44-46.
it's parsimonious as fuck.  the range() and len() functions nested as they
are i indeed found online, but it is the least interesting part of the second
section.  Annnnnd now all that's moot cause i rewrote the iteration process.
It's not worlds apart, but uses a for loop to go through mylist3 item by item,
converting each one to a string as it does, compare it to user input, and if
a match, grabs the items index number and replaces it then and there via it.
'''

while match not in str(mylist3):
    print(f"Boy, '{match}' ain't on that goddamn list. Type EXACTLY as shown.")
    print(" | ".join(str(x) for x in mylist3))
    match = input("Try again:  ")

"""
for i in range(len(mylist3)):
    if str(mylist3[i]) == match:
        mylist3[i] = input1
        print("I just made the change - check this shit... \n")
"""
# rewriting above loop just for practice - boss move, works.  list.index(item)

for i in mylist3:
    if str(i) == match:
        ind = mylist3.index(i)
        mylist3[ind] = input1
        print("I just made the change - check this shit... \n")

print(" | ".join(str(x) for x in mylist3))
