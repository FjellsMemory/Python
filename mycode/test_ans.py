"""The coolest recursive input-testing function I wasn't allowed to use D:."""


def test_ans(dec: str, choice: str, lna: int) -> str:
    """Ask question and test for legit answer."""
    if lna == 3:
        if dec == "A" or dec == "B" or dec == "C" or \
                dec == "a" or dec == "b" or dec == "c":
            return dec.upper()
        else:
            print("\nPlease only enter a SINGLE LETTER: A, B, or C.\n"
                  "Refer to the game's instructional first paragraph. ;)\n")
            return test_ans((input(choice)), choice, lna)
    elif lna == 2:
        if dec == "A" or dec == "B" or \
                dec == "a" or dec == "b":
            return dec.upper()
        else:
            print("\nPlease only enter a SINGLE LETTER: A or B.\n"
                  "Refer to the game's instructional first paragraph. ;)\n")
            return test_ans((input(choice)), choice, lna)
    else:
        print("Not sure how you got here! :D)")
        return ""