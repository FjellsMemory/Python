types_of_people = 10   # the binary joke in full right here
x = f"There are {types_of_people} types of people."  # f string stored in var x

binary = "binary"   # strings packed in variables
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."  # fstring calling vars

print(x)  # printing the fstrings by their var names
print(y)

print(f"I said: {x}")  # double nested fstring calls
print(f"I also said: '{y}'")

hilarious = False  # bool
joke_evaluation = "Isn't that joke so funny?! {}"  # string w empty {} for l8er

print(joke_evaluation.format(hilarious))  # homeboy's .format() introduction

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)  # concantenated string
