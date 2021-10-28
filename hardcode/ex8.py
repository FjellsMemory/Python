formatter = "{}{}{}{}"

print(formatter)
print(formatter.format(1, 2, 3, 4))
form = formatter.format(1, 2, 3, 4)
print(type(form))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

input1 = "fuck yeah"
print("F-string test is {}".format(input1))

print("test on the fly with {}".format("Christ"))
