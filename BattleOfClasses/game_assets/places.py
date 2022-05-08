class PlaceBase:
    def __init__(self, name):
        self.name = name
        self.player = None

    def enter(self, player):
        print(f"Wellcome in the {self.name} {player}")
        self.player = player

        self.main_menu()

    def main_menu(self):
        print("PlaceBase.main_menu: This method is not implemented!")


class Arena(PlaceBase):
    pass


class Tavern(PlaceBase):
    pass