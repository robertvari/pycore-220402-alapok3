import random


class Card:
    def __init__(self, name, value):
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value

    def __repr__(self):
        return f"{self.name}"


class Deck:
    def __init__(self):
        self._cards = []
        self.create()

    def create(self):
        cards = [
            ["2", 2],
            ["3", 3],
            ["4", 4],
            ["5", 5],
            ["6", 6],
            ["7", 7],
            ["8", 8],
            ["9", 9],
            ["10", 10],
            ["King", 10],
            ["Queen", 10],
            ["Jack", 10],
            ["Ace", 11]
        ]

        names = ["Heart", "Club", "Diamond", "Spade"]

        for name in names:
            for card in cards:
                new_card = Card(f"{name} {card[0]}", card[1])
                self._cards.append(new_card)

        # shuffle deck
        random.shuffle(self._cards)

    @property
    def cards(self):
        return self._cards

    def draw(self):
        new_card = self._cards[0]
        self._cards.remove(new_card)
        return new_card


class PlayerBase:
    def __init__(self):
        self._name = None
        self._hand = []
        self._credits = random.randint(10, 100)

    def create(self):
        first_names = ["Brittney", "Curtis", "Lucas", "Chip", "Simon"]
        last_names = ["Moriah", "Tristin", "Troy", "Gale", "Lynn"]
        self._name = f"{random.choice(first_names)} {random.choice(last_names)}"

    def report(self):
        print(f"Name: {self._name}")
        print(f"Hand: {self._hand} Hand value: {self.count_hand()}")
        print(f"Credits: {self._credits}")

    def draw_card(self, deck):
        hand_value = self.count_hand()

        while hand_value < 16:
            self._hand.append(deck.draw())
            hand_value = self.count_hand()

        print(f"{self._name} finished drawing")

    def count_hand(self):
        return sum([card.value for card in self._hand])


class Player(PlayerBase):
    def create(self):
        self._name = input("What is your name?")

    def draw_card(self, deck):
        print(f"This is your turn {self._name}")
        self._show_hand()

        user_input = input("Do you want to draw a card? (y/n)")

        while user_input == "y":
            self._hand.append(deck.draw())
            self._show_hand()

            user_input = input("Do you want to draw a card? (y/n)")

    def _show_hand(self):
        print(f"Your cards: {self._hand}")
        print(f"Your hand value: {self.count_hand()}")


class AIPlayer(PlayerBase):
    pass


if __name__ == "__main__":
    deck = Deck()

    player = Player()
    player.create()
    player.draw_card(deck)

    player.report()