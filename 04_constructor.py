class Dice:
    # class attribute

    # constructor
    def __init__(self, color, sides):
        # instance attribute
        self.color = color
        self.sides = sides


class Person:
    race = "human"

    def __init__(self, name, address):
        self.name = name
        self.address = address


robert = Person("Robert", "Budapest")
tamas = Person("Tamás", "Pécs")
Person.race = "animal"
print(robert.name, robert.address, robert.race)
print(tamas.name, tamas.address, tamas.race)