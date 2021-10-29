"""Concantenating strings with * and +."""

print("Mary had a little lamb.")  # prints str
print("It's fleece was white as {}.".format('snow'))  # same
print("And everywhere that Mary went.")  # same
print("." * 10)  # concanted the str 10 times

print("So the .format method is a function of the string class that adds new \
    text to the {} after the string is written.")

mystr = "This is the most badass {}."
print(mystr.format('Fuck Nugget'))

end1 = "C"  # str variables all the way down
end2 = "h"
end3 = "e"
end4 = "e"  # triple cheeese
end5 = "e"
end6 = "s"
end7 = "e"
end8 = "B"
end9 = "u"
end10 = "r"
end11 = "g"
end12 = "e"
end13 = "r"

# watch that comma at the end.  try removing it see what happens

cheeselist = [x for x in "MattKelly"]
print(cheeselist)
print("|".join(x for x in "Matt Kelly"))
print(end1 + end2 + end3 + end4 + end5 + end6 + end7, end=" ")
# concants all the disaparate letters, ends with a space, tho i never saw
# that b4
print(end8 + end9 + end10 + end11 + end12 + end13)

print(end1, end2, end3, end4, end5, end6, end7)
