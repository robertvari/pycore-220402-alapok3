class CharacterBase:
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