import os
from game_assets.places import Arena, Tavern


class BattleOfClasses:
    def __init__(self):
        self.arena = Arena()
        self.tavern = Tavern()

        self._intro()

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")

    def _intro(self):
        self.clear_screen()
        print("-"*50, "BATTLE OF CLASSES", "-"*50)


BattleOfClasses()

