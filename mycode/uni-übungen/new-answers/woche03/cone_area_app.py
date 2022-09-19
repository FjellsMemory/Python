"""This script contains the application of cone_area."""

from cone_area_lib import cone_area
if __name__ == "__main__":
    r = float(input("Radius: "))
    h = float(input("Höhe: "))
    print(f"Mantelfläche: {cone_area(r, h)}")