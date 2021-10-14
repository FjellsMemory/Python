class Homeboi:
    def __init__(self, name, powerlevel):
        self.name = name
        self.powerlevel = powerlevel

    def pltest(self):
        if self.powerlevel > 9000:
            print(f"{self.name}'s power level is over 9000!")
        else:
            print(f"{self.name}'s power level is only {self.powerlevel}")

    def set_pl(self, pl):
        self.powerlevel = pl


Jeff = Homeboi("Jeff", 9001)
inst = 'Jeff = Homeboi("Jeff", 9001)'

print(f"Creating a Homboi 'Jeff' as follows: '{inst}'")
print("Performing powerlevel test on Jeff...\n")
Jeff.pltest()

print("\nNow create your own Homeboi...")
tempname = input("Give your Homeboi a name:  ")
temppl = int(input("Annnnnd a power level:  "))
userobj = Homeboi(tempname, temppl)

yesno = input(f"Want to check {tempname}'s powerlevel? (y/n?): ")
if yesno.lower() == "y":
    userobj.pltest()
else:
    pass
yesno = input(f"Want to tweak {tempname}'s powerlevel? (y/n?): ")
if yesno.lower() == "y":
    userobj.set_pl(int(input("New powerlevel?:  ")))
    userobj.pltest()
else:
    pass
print(userobj.name, userobj.powerlevel)
