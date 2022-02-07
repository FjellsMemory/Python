"""Application script, calculates Mantelfläche of a cone."""
from cone_area_lib import cone_area

rad = float(input("Radius: "))
ht = float(input("Höhe: "))

print("Mantelfläche:", (cone_area(rad, ht)))
