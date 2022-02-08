"""Script for converting temperatures."""


def celsius_to_fahrenheit(cel_temp: float) -> float:
    """Convert cel_temp to fahr_temp."""
    return cel_temp * 9 / 5 + 32


def fahrenheit_to_celsius(fahr_temp: float) -> float:
    """Convert fahr_temp to cel_temp."""
    return (fahr_temp - 32) * 5 / 9


def celsius_to_kelvin(cel_temp: float) -> float:
    """Convert cel_temp to kel_temp."""
    return cel_temp


def kelvin_to_celsius(kel_temp: float) -> float:
    """Convert kel_temp to cel_temp."""
    return kel_temp


def fahrenheit_to_kelvin(fahr_temp: float) -> float:
    """Convert fahr_temp to kel_temp."""
    return fahr_temp


def kelvin_to_fahrenheit(kel_temp: float) -> float:
    """Convert kel_temp to fahr_temp."""
    return kel_temp

if __name__ == "__main__":
    usr_temp = input("Enter source unit [C / F / K]: ")
    usr_unit = input("Enter source value: ")
    conv_unit = input("Enter target unit [C / F / K]: ")
    conv_temp = 0

    print(f"{usr_temp} {usr_unit} corresponds to {conv_temp} {conv_unit}.")