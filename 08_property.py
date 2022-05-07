class Dice:
    # class attribute
    allowed_colors = ["red", "white", "blue"]

    def __init__(self, color, sides):
        # private instance attribute
        self.__color = color
        self.__sides = sides

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, new_color):
        assert isinstance(new_color, str), "color must be of type string"
        assert new_color in self.allowed_colors, f"Allowed colors: {self.allowed_colors}"

        self.__color = new_color

    @property
    def sides(self):
        return self.__sides


my_dice = Dice("White", 6)
print(my_dice.color)
my_dice.color = "blue"
print(my_dice.color)

print(my_dice.sides)