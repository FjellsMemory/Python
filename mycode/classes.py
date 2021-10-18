class Cheetah:
    def __init__(self, name, powerlevel):
        self.name = name
        self.powerlevel = powerlevel

    def get_atts(self) -> str:
        selflist = []
        selflist = [self.name, self.powerlevel]
        return " | ".join(str(x) for x in selflist)

    def pltest(self):
        if self.powerlevel > 9000:
            print(f"Fuck me!  {self.name}'s power level is over 9000!")
        else:
            print(f"{self.name}'s power level is only {self.powerlevel}")

    def set_pl(self, pl):
        self.powerlevel = pl

class Homeboi(Cheetah):
    def __init__(self, name, powerlevel, sweetnesslvl):
        super().__init__(name, powerlevel)
        self.sweetnesslvl = sweetnesslvl

    def swltest(self):
        return self.sweetnesslvl

    def get_atts(self) -> str:
        selflist = [self.name, self.powerlevel, self.sweetnesslvl]
        return " | ".join(str(x) for x in selflist)


Jeff = Homeboi("Jeff", 9001, 3560)


print(f"Creating a Homboi 'Jeff' as follows: {Jeff.get_atts()}\n")
print(f"And now just his Cheetah attributes: {Cheetah.get_atts(Jeff)}")
print("Performing powerlevel test on Jeff...\n")
Jeff.pltest()

print("\nNow create your own Homeboi...")
tempname = input("Give your Homeboi a name:  ")
temppl = int(input("Annnnnd a power level:  "))
tempswlvl = int(input("Annnnnd a sweetness level:  "))
userobj = Homeboi(tempname, temppl, tempswlvl)

yesno = input(f"Want to check {tempname}'s powerlevel? (y/n?): ")
if yesno.lower() == "y":
    userobj.pltest()
else:
    pass
yesno = input(f"Want to tweak {tempname}'s powerlevel? (y/n?): ")
if yesno.lower() == "y":
    userobj.set_pl(int(input("New powerlevel?:  ")))
    # above i wanted to get user input into the object without the creation
    # of new variables.  i did it by nesting -> function((()))
    userobj.pltest()
else:
    pass
print(userobj.name, userobj.powerlevel, userobj.sweetnesslvl)

Jeff.get_atts()
