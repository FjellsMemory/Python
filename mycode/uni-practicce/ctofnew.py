"""This script converts C to F to 2 decimal places."""

ctemp = float(input("Celcius: "))
ftemp = ctemp * 9 / 5 + 32
print("Fahrenheit:", round(ftemp, 2))