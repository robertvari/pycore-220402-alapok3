import random


class Person:
    def __init__(self, name, age, address=None, email=None):
        self.name = name
        self.address = address
        self.age = age
        self.email = email

    # instance method
    def say_hello(self):
        print(f"My name is: {self.name}")
        print(f"My age is: {self.age}")
        print(f"My address: {self.address}")
        print(f"My email: {self.email}")

    def jump(self):
        print(f"{self.name} does a jump")


class Dice:
    def __init__(self, color, sides):
        self.color = color
        self.sides = sides
        self.current_number = 1

    def roll(self):
        self.current_number = random.randint(1, self.sides)

    def report(self):
        print(f"Color: {self.color} Sides: {self.sides} Current Number: {self.current_number}")


dice6 = Dice("White", 6)
dice10 = Dice("Red", 10)

dice6.roll()
dice10.roll()

dice6.report()
dice10.report()



# robert = Person("Robert Vari", 38)
# csaba = Person("Kiss Csaba", 40, "Budapest", "csaba@gmail.com")
#
# robert.say_hello()
# robert.jump()
#
# csaba.say_hello()
# csaba.jump()