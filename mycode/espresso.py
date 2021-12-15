"""Script to find out which route is cheaper in the espresso bar."""
from dataclasses import dataclass


@dataclass
class Bev():
    """Class to represent an espresso drink."""

    name: str = ""
    price: float = 0.0
    esp_num: int = 1
    ppe: float = 0.0


def total_cost(pp_drink: float, esp_in_drink: int) -> float:
    """
    Total cost calculation.

    Take price of drink and # of esp in drink, subtract off price of the free
    double earned after buying 10 of them.
    """
    total = (((pp_drink * 10 - 3.20) / esp_in_drink) / 10)
    return total


def create_bev(bev: Bev) -> Bev:
    """Add attributes to bev instance."""
    print("\nNew Drink...")
    bev.name = input("Name of drink: ")
    bev.price = float(input("It's price: "))
    bev.esp_num = int(input("Number of espressos in dis bev? "))
    return bev


if __name__ == "__main__":
    bev1, bev2 = Bev(), Bev()

    bev1 = create_bev(bev1)
    bev2 = create_bev(bev2)

    bev1.ppe = total_cost(bev1.price, bev1.esp_num)
    bev2.ppe = total_cost(bev2.price, bev2.esp_num)
    print("\n")

    print(f"Cost per esp in {bev1.name} = {bev1.ppe}")
    print(f"Cost per esp in a {bev2.name} = {bev2.ppe}")

    cheaper = min(bev1.ppe, bev2.ppe)
    if cheaper == bev1.ppe:
        cheaper_name = bev1.name
    else:
        cheaper_name = bev2.name

    print(f"Do you know what this means?  Means {cheaper_name}s are cheaper in \
the end.  And it's not even close.  I just used my prog skills and science to \
keep cash in da wallet.  D'hear dat lads.  Da wallet.  Full.")
