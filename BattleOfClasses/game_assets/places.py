class PlaceBase:
    def __init__(self):
        self.player = None

    def enter(self, player):
        self.player = player


class Arena(PlaceBase):
    pass


class Tavern(PlaceBase):
    pass