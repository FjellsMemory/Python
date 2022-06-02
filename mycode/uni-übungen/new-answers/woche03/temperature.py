"""This script converts Celsius/Fahrenheit/Kelvin temperatures."""


def celsius_to_fahrenheit(wert: float) -> float:
    return wert * 9 / 5 + 32


def fahrenheit_to_celsius(wert: float) -> float:
    return (wert - 32) * (5 / 9)


def celsius_to_kelvin(wert: float) -> float:
    return wert + 273.15


def kelvin_to_celsius(wert: float) -> float:
    return wert - 273.15


def fahrenheit_to_kelvin(wert: float):
    return celsius_to_kelvin(fahrenheit_to_celsius(wert))


def kelvin_to_fahrenheit(wert: float):
    return celsius_to_fahrenheit(kelvin_to_celsius(wert))


if __name__ == "__main__":
    SU = input("Enter source unit [C / F / K]: ")
    SV = float(input("Enter source value: "))
    TU = input("Enter target unit [C / F / K]: ")
    EV = 0.0

    if SU == "C" and TU == "F":
        EV = celsius_to_fahrenheit(SV)
    elif SU == "C" and TU == "K":
        EV = celsius_to_kelvin(SV)
    elif SU == "F" and TU == "C":
        EV = fahrenheit_to_celsius(SV)
    elif SU == "F" and TU == "K":
        EV = fahrenheit_to_kelvin(SV)
    elif SU == "K" and TU == "C":
        EV = kelvin_to_celsius(SV)
    elif SU == "K" and TU == "F":
        EV = kelvin_to_fahrenheit(SV)

    print(f"{SV} {SU} corresponds to {EV} {TU}.")