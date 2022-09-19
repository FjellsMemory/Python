def add(a: float, b: float):
    print(f"returning {a} + {b}")
    return a + b

def subtract(a: float, b: float):
    print(f"returning {a} - {b}")
    return a - b

def multiply(a: float, b: float):
    print(f"returning {a} * {b}")
    return a * b

def divide(a: float, b: float):
    print(f"returning {a} / {b}")
    return a / b


print("Let's do some math with just functions!")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")


# A puzzle for the extra credit, type it in anyway.
print("Here is a puzzle.")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print("That becomes (feet): ", what, "\nCan you do it by hand?")