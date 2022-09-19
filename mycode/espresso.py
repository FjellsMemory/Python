"""Script to find out which drink is ultimately cheapest in the espresso bar."""
from dataclasses import dataclass


@dataclass
class Bev():
    """Class to represent an espresso drink."""

    name: str = ""
    price: float = 0.0
    esp_num: int = 0
    ppe: float = 0.0


def total_cost(pp_drink: float, esp_in_drink: int) -> float:
    """
    Total cost calculation.

    Take price of drink and # of esp in drink, subtract off price of the free
    double earned after buying 10 of them.
    """
    total = (((pp_drink * 10 - 3.20) / esp_in_drink) / 10)
    return total


def define_bev(bev: Bev) -> Bev:
    """Add attributes to bev instance."""
    print("\nNew Drink...")
    bev.name = input("Name of drink: ")
    bev.price = float(input("It's price: "))
    bev.esp_num = int(input("Number of espressos in dis bev? "))
    bev.ppe = round(total_cost(bev.price, bev.esp_num), 2)
    return bev


bev_list = []
dingo_list = [Bev(name='Esp', price=1.8, esp_num=1, ppe=1.48),
              Bev(name='Dbl Esp', price=3.2, esp_num=2, ppe=1.44),
              Bev(name='Homeboi Latte', price=4.5, esp_num=4, ppe=1.04),
              Bev(name='Gravy Train', price=5.6, esp_num=3, ppe=1.76)]


if __name__ == "__main__":

    while True:  # iterative creation of new drinks, pack into list
        ans = input("\nCreate drink ((y) or (n)):  ")
        if ans.lower() == "n":
            break
        else:
            bev = Bev()
            bev_list.append(define_bev(bev))
    ans_two = input("Import list of dranks ((y) or (n)):  ")
    if ans_two.lower() == "y":
        bev_list.extend(dingo_list)

    cheapest_drank = bev_list[0]
    for x in bev_list:
        if x.ppe < cheapest_drank.ppe:
            cheapest_drank = x
        else:
            continue

    print(f"""
Do you know what this means?  Means {cheapest_drank.name}s are cheapest in the
end.  I just used my prog skills and science to keep cash in da wallet.  D'hear
dat lads.  Da wallet.  Full.
""")