from sys import argv
# read the WYSS section for how to run this
homey, these, are, my, variables = argv

print("The script is called: ", homey, "so input your name:", end= " ")
input1 = input()
print("Your first variable is:", int(these))
print("Your second variable is:", are)
print("Your third variable is:", my)
print("Your fourth variable is:", variables)
print(type(these))
