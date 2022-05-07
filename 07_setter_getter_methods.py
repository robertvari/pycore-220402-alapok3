class Dice:
    def __init__(self, color, sides):
        # private instance attribute
        self.__color = color
        self.__sides = sides

        # public attribute
        self.name = "Robert"

    def roll(self):
        pass

    # getter methods
    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    # setter methods
    def set_sides(self, new_sides):
        assert isinstance(new_sides, int), "Side must be of type integer"
        self.__sides = new_sides

    def set_color(self, new_color):
        assert isinstance(new_color, str), "Color must be of type string"
        self.__color = new_color


my_dice = Dice("white", 6)

my_dice.set_sides("Robert")
my_dice.get_color()