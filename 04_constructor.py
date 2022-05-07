class Dice:
    # constructor
    def __init__(self, color, sides):
        print(f"A dice was born. Color: {color} Sides: {sides}")

        # instance attribute
        self.color = color
        self.sides = sides


my_dice1 = Dice("white", 6)
my_dice2 = Dice("red", 10)
my_dice3 = Dice("blue", 20)

print(my_dice1.color, my_dice1.sides)
print(my_dice2.color, my_dice2.sides)