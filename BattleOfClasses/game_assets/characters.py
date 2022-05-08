class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100, "max_weight": 50},
        "ork": {"strength": 130, "max_HP": 200, "max_weight": 100},
        "elf": {"strength": 60, "max_HP": 100, "max_weight": 60},
        "dwarf": {"strength": 130, "max_HP": 230, "max_weight": 150},
    }

    def __init__(self):
        pass


class Player(CharacterBase):
    pass


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == "__main__":
    enemy = Enemy()
    bartender = NPC()

    print(enemy)
    print(bartender)