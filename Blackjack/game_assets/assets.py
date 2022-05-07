class Card:
    def __init__(self, name, value):
        print("Card created", name, value)
        self._name = name
        self._value = value

    @property
    def name(self):
        return self._name

    @property
    def value(self):
        return self._value


if __name__ == "__main__":
    card = Card("Club 2", 2)
