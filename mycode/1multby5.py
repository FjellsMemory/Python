"""This script takes user input and mults it by 5 via a function."""


def multby5(inp):
    """Mult the passed argument by 5."""
    print(f"Okay, bro, your number times 5 is {int(inp) * 5}")
    return


myVar = input("Yo, bro, input a number: ")
multby5(myVar)
