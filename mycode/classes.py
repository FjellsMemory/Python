class Homeboi:
    def __init__(self, name, powerlevel):
        self.name = name
        self.powerlevel = powerlevel

    def pltest(self):
        if self.powerlevel > 9000:
            print("His power level is over 9000!")
        else:
            print(f"His power level is only {self.poewerlevel}")

Jeff = Homeboi("Jeff", 9001)
inst = 'Jeff = Homeboi("Jeff", 9001)'

print(f"Creating a Homboi 'Jeff' as follows: '{inst}'")
print("Performing powerlevel test on Jeff...")
Jeff.pltest()
