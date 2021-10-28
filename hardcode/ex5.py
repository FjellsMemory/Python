name = "Dustin L. Gould"
age = 45  # not a lie
height = 72  # inches
weight = 170  # lbs
eye_color = "green"
teeth_color = "white"
hair_color = "red"

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall.")
print(f"He's {weight} pounds heavy.")
print(f"Incidentally, that's {int(height) * 2.54} centimeters")
print(f"As well as {int(weight) * 0.453592} kilograms.")
print(f"Actually that's not too heavy.")
print(f"He's got {eye_color} eyes and {hair_color} hair.")
print(f"His teeth are usually {teeth_color} depending on the coffee.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight}, I get {total}")
