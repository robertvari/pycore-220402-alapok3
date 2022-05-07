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

if __name__ == "__main__":
    deck = Deck()
    deck.create()
    print(deck.cards)

    # drew few cards from deck
    card1 = deck.draw()
    card2 = deck.draw()
    card3 = deck.draw()

    print(card1, card2, card3)

    print(deck.cards)
