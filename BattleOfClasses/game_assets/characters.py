import random


class CharacterBase:
    races = {
        "human": {"strength": 50, "max_HP": 100, "max_weight": 50},
        "ork": {"strength": 130, "max_HP": 200, "max_weight": 100},
        "elf": {"strength": 60, "max_HP": 100, "max_weight": 60},
        "dwarf": {"strength": 130, "max_HP": 230, "max_weight": 150},
    }

    def __init__(self):
        self.name = None
        self.race = None
        self.golds = random.randint(0, 100)
        self.max_weight = 0
        self.inventory = []

        self.strength = 0
        self.max_HP = 0
        self.current_HP = 0
        self.current_level = 1

        self.right_hand = None
        self.left_hand = None

        self._create()

    def _create(self):
        self.name = self.get_fantasy_name()
        self.race = random.choice(list(self.races))
        self._setup_stats()

    def _setup_stats(self):
        self.strength = self.races[self.race]["strength"]
        self.max_HP = self.races[self.race]["max_HP"]
        self.current_HP = self.max_HP
        self.max_weight = self.races[self.race]["max_weight"]

    @staticmethod
    def get_fantasy_name():
        FIRST = ['A', 'Ag', 'Ar', 'Ara', 'Anu', 'Bal', 'Bil', 'Boro', 'Bern', 'Bra', 'Cas', 'Cere', 'Co', 'Con',
                 'Cor', 'Dag', 'Doo', 'Elen', 'El', 'En', 'Eo', 'Faf', 'Fan', 'Fara', 'Fre', 'Fro', 'Ga', 'Gala', 'Has',
                 'He', 'Heim', 'Ho', 'Isil', 'In', 'Ini', 'Is', 'Ka', 'Kuo', 'Lance', 'Lo', 'Ma', 'Mag', 'Mi', 'Mo',
                 'Moon', 'Mor', 'Mora', 'Nin', 'O', 'Obi', 'Og', 'Pelli', 'Por', 'Ran', 'Rud', 'Sam', 'She', 'Sheel',
                 'Shin', 'Shog', 'Son', 'Sur', 'Theo', 'Tho', 'Tris', 'U', 'Uh', 'Ul', 'Vap', 'Vish', 'Ya', 'Yo', 'Yyr']

        SECOND = ['ba', 'bis', 'bo', 'bus', 'da', 'dal', 'dagz', 'den', 'di', 'dil', 'din', 'do', 'dor', 'dra',
                  'dur', 'gi', 'gauble', 'gen', 'glum', 'go', 'gorn', 'goth', 'had', 'hard', 'is', 'ki', 'koon', 'ku',
                  'lad', 'ler', 'li', 'lot', 'ma', 'man', 'mir', 'mus', 'nan', 'ni', 'nor', 'nu', 'pian', 'ra', 'rak',
                  'ric', 'rin', 'rum', 'rus', 'rut', 'sek', 'sha', 'thos', 'thur', 'toa', 'tu', 'tur', 'tred', 'varl',
                  'wain', 'wan', 'win', 'wise', 'ya']

        return f"{random.choice(FIRST)}{random.choice(SECOND)}"

    def show_stats(self):
        print("-"*50)
        print(f"Name: {self.name}")
        print(f"Race: {self.race}")
        print(f"Golds: {self.golds}")
        print(f"max_weight: {self.max_weight}")
        print(f"inventory: {self.inventory}")
        print(f"strength: {self.strength}")
        print(f"max_HP: {self.max_HP}")
        print(f"current_HP: {self.current_HP}")
        print(f"current_level: {self.current_level}")
        print(f"right_hand: {self.right_hand}")
        print(f"left_hand: {self.left_hand}")
        print("-" * 50)


class Player(CharacterBase):
    def _create(self):
        self.name = input("What is your name?")
        self.race = input(f"What is your race {list(self.races)}")

        while self.race.lower() not in self.races:
            self.race = input(f"What is your race {list(self.races)}")

        self._setup_stats()


class Enemy(CharacterBase):
    pass


class NPC(CharacterBase):
    pass


if __name__ == "__main__":
    enemy = Enemy()
    bartender = NPC()
    player = Player()

    enemy.show_stats()
    bartender.show_stats()
    player.show_stats()