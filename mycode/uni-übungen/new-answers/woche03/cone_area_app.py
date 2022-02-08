"""This script is to run the funcs in  cone_area_lib.py."""

from cone_area_lib import cone_area


# if __name__ == "__main__":  # not necessary since script contains no defs

radius = float(input("Radius: "))
height = float(input("Höhe: "))
print(cone_area(radius, height))
