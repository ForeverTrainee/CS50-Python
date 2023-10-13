"""
Unpacking examples
"""

#first, _ = input("What`s your name? ").split(" ")


def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]
"""
List unpacking 
Instead of using:
print(total(coins[0], coins[1], coins[2]), "Knuts")
or
print(total(galleons=100 , sickles=50, knuts=25), "Knuts")

we use as below.
"""
print(total(*coins), "Knuts(List)")

"""
Dictionary unpacking
Instead of using:
print(total(
            coins_dictionary["galleons"],
            coins_dictionary["sickles"],
            coins_dictionary["knuts"]),
            "Knuts(Dictionary)"
            )
We can use as below.
"""


coins_dictionary = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins_dictionary), "Knuts(Dictionary)")


def named(*args,**kwargs):
    print("Named: ", kwargs)

named(galleons=100, sickles=50, knuts=25)

def positional(*args, **kwargs):
    print("Possitional:", args)

positional(100,50,25)
