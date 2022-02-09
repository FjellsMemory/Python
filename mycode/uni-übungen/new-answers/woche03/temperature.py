"""Script for converting temperatures."""


def celsius_to_fahrenheit(cel_temp: float) -> float:
    """Convert cel_temp to fahr_temp."""
    return cel_temp * 9 / 5 + 32


def fahrenheit_to_celsius(fahr_temp: float) -> float:
    """Convert fahr_temp to cel_temp."""
    return (fahr_temp - 32) * 5 / 9


def celsius_to_kelvin(cel_temp: float) -> float:
    """Convert cel_temp to kel_temp."""
    return cel_temp - 273.15


def kelvin_to_celsius(kel_temp: float) -> float:
    """Convert kel_temp to cel_temp."""
    return kel_temp + 273.15


def fahrenheit_to_kelvin(fahr_temp: float) -> float:
    """Convert fahr_temp to kel_temp."""
    return celsius_to_kelvin(fahrenheit_to_celsius(fahr_temp))


def kelvin_to_fahrenheit(kel_temp: float) -> float:
    """Convert kel_temp to fahr_temp."""
    return celsius_to_fahrenheit(kelvin_to_celsius(kel_temp))


if __name__ == "__main__":
    usr_unit = input("Enter source unit [C / F / K]: ")
    usr_temp = float(input("Enter source value: "))
    conv_unit = input("Enter target unit [C / F / K]: ")
    conv_temp = "undefined"
    if usr_unit == "C":
        if conv_unit == "F":
            conv_temp = celsius_to_fahrenheit(usr_temp)
        elif conv_unit == "K":
            conv_temp = celsius_to_kelvin(usr_temp)

    if usr_unit == "F":
        if conv_unit == "C":
            conv_temp = fahrenheit_to_celsius(usr_temp)
        elif conv_unit == "K":
            conv_temp = fahrenheit_to_kelvin(usr_temp)

    if usr_unit == "K":
        if conv_unit == "C":
            conv_temp = kelvin_to_celsius(usr_temp)
        elif conv_unit == "F":
            conv_temp = kelvin_to_fahrenheit(usr_temp)

    print(f"{usr_temp} {usr_unit} corresponds to {round((float(conv_temp)), 2)}\
 {conv_unit}.")