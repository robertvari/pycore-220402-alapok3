import os
from game_assets.places import Arena, Tavern
from game_assets.characters import Player


class BattleOfClasses:
    def __init__(self):
        self._intro()
        self.player = Player()

        self.arena = Arena("Arena", self)
        self.tavern = Tavern("Black Horse Tavern", self)

        self.main_menu()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def main_menu(self):
        self.clear_screen()

        print(f"Wellcome in this small town {self.player}")
        print("There is a tavern on the right and an arena on the left.")
        print("Where do you want to go?")
        print("1. Tavern")
        print("2. Arena")
        print("3. Exit Game")

        player_input = input()

        if player_input == "1":
            self.tavern.enter(self.player)
        elif player_input == "2":
            self.arena.enter(self.player)
        else:
            self.clear_screen()
            exit()

    def _intro(self):
        self.clear_screen()
        print("-"*50, "BATTLE OF CLASSES", "-"*50)


BattleOfClasses()

