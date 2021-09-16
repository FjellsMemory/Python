from sys import argv
# read the WYSS section for how to run this
script, height, weight, age, likes = argv

print("the script is called", script, "so input your name:", end= " ")
input1 = input()
print("Your first variable is:", (height))
print("Your second variable is:", weight)
print("Your third variable is:", age)
print("Your fourth variable is:", likes)
print(f"great stuff, {input1}.")
