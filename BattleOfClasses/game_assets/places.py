class PlaceBase:
    def __init__(self, name, game):
        self.name = name
        self.game = game
        self.player = None

    def enter(self, player):
        print(f"Wellcome in the {self.name} {player}")
        self.player = player

        self.main_menu()

    def main_menu(self):
        print("PlaceBase.main_menu: This method is not implemented!")


class Arena(PlaceBase):
    def main_menu(self):
        print("1. Fight")
        print("2. Go back to the street")

        player_input = input()

        if player_input == "2":
            self.game.main_menu()
        else:
            self.start_fight()

    def start_fight(self):
        print("Fight!!!")


class Tavern(PlaceBase):
    def main_menu(self):
        print("1. Buy something")
        print("2. Go back to the street")

        player_input = input()

        if player_input == "2":
            self.game.main_menu()
        else:
            self.shop_menu()

    def shop_menu(self):
        print("Shopping list...")