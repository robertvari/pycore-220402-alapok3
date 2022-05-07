from game_assets.assets import Deck, Player, AIPlayer


class Blackjack:
    def __init__(self):
        self._intro()

        # create players
        self.player = Player()
        self.player.create()

        self.ai_player = AIPlayer()
        self.ai_player.create()

        # create deck and store credits
        self.deck = None
        self.table_credits = 0

        self._default_bet = 10

        # start game
        self._play_game()

    def _play_game(self):
        self.deck = Deck()

        # setup player hands
        self.ai_player.init_hand(self.deck)
        self.player.init_hand(self.deck)

        # give bet
        self.table_credits += self.ai_player.give_bet(self._default_bet)
        self.table_credits += self.player.give_bet(self._default_bet)

        pass

    def _intro(self):
        print("-"*50, "BLACKJACK", "-"*50)


Blackjack()