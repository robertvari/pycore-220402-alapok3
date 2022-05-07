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
        self.table_credits = 0

        # setup player hands
        self.ai_player.init_hand(self.deck)
        self.player.init_hand(self.deck)

        # give bet
        self.table_credits += self.ai_player.give_bet(self._default_bet)
        self.table_credits += self.player.give_bet(self._default_bet)

        self.ai_player.draw_card(self.deck)
        self.player.draw_card(self.deck)

        self._get_winner()

    def _get_winner(self):
        player_list = [self.player, self.ai_player]
        winner_list = [i for i in player_list if i.count_hand() <= 21]

        if not winner_list:
            print("Nobody winds this time :(")
        else:
            winner_list = sorted(winner_list, key=lambda p: p.count_hand())
            winner = winner_list[-1]

            print(f"The winner is: {winner}")
            print(f"Who wins {self.table_credits}")
            winner.give_credits(self.table_credits)

        user_input = input("Do you want to play again? (y/n)")
        if user_input == "y":
            self._play_game()

    def _intro(self):
        print("-"*50, "BLACKJACK", "-"*50)


Blackjack()