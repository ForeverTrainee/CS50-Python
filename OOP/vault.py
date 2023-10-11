#Operator Overloading
class Vault:
    def __init__(self, galleons=0, sticles=0, knuts=0):
        self.galleons = galleons
        self.stickles = sticles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.stickles} Stickles, {self.knuts} Knuts"

    def __add__(self, other):
        galleons = self.galleons + other.galleons
        stickles = self.stickles + other.stickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, stickles, knuts)



potter = Vault(100,50,25)
print(potter)

weasley = Vault(25, 50,100)
print(weasley)

#galleons = potter.galleons + weasley.galleons
#stickles = potter.stickles + weasley.stickles
#knuts = potter.knuts + weasley.knuts
#total = Vault(galleons, stickles, knuts)

total = potter + weasley
print(total)