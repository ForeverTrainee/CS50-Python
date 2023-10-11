import random


class Hat:

    houses = ["Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"]

    def sort(cls, name):
        print(name, "is in", random.choice(cls.houses))


hat = Hat()
hat.sort("Harry")