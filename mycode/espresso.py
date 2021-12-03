"""Script to find out which route is cheaper in the espresso bar."""


def total_cost(pp_drink: float, esp_in_drink: int) -> float:
    """
    Take price of drink and # of esp in drink, subtract off price of the free
    double earned after buying 10 of them.
    """
    total = (pp_drink / esp_in_drink) - (0.32 / esp_in_drink)
    return total


if __name__ == "__main__":
    single_cost = total_cost(1.80, 1)
    double_cost = total_cost(3.60, 2)
    print(f"Cost per esp in a single = {single_cost}")
    print(f"Cost per esp in a double = {double_cost}")
    print("Do you know what this means?  Means singles are cheaper in the \
end.  And it's not even close.  I just used my prog skills and science to \
keep cash in da wallet.  D'hear dat lads.  Da wallet.  Full.")
