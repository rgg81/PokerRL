# Copyright (c) 2019 Eric Steinberger


"""
This script will start a game of 3-player No-Limit Texas Hold'em with discrete bet sizes in which you can play against
yourself.
"""

from PokerRL.game.InteractiveGameCustom import InteractiveGameCustom
from PokerRL.game.games import DiscretizedNLHoldem
from PokerRL.game import bet_sets

if __name__ == '__main__':
    playerA = 20000
    playerB = 20000

    round = 1

    while playerA > 0 and playerB > 0:

        if round % 2 == 0:

            game_cls = DiscretizedNLHoldem
            args = game_cls.ARGS_CLS(n_seats=2,
                                     starting_stack_sizes_list=[playerA,playerB],
                                     bet_sizes_list_as_frac_of_pot=bet_sets.B_5,
                                     stack_randomization_range=(0, 0,),
                                     )

            game = InteractiveGameCustom(env_cls=game_cls,
                                   env_args=args,
                                   seats_human_plays_list=[0, 1],
                                   )

            game.start_to_play()

            print(game.winnings_per_seat)
            playerA = int(playerA + game.winnings_per_seat[0])
            playerB = int(playerB + game.winnings_per_seat[1])
        else:
            game_cls = DiscretizedNLHoldem
            args = game_cls.ARGS_CLS(n_seats=2,
                                     starting_stack_sizes_list=[playerB,playerA],
                                     bet_sizes_list_as_frac_of_pot=bet_sets.B_5,
                                     stack_randomization_range=(0, 0,),
                                     )

            game = InteractiveGameCustom(env_cls=game_cls,
                                         env_args=args,
                                         seats_human_plays_list=[0, 1],
                                         )

            game.start_to_play()

            print(game.winnings_per_seat)
            playerA = int(playerA + game.winnings_per_seat[1])
            playerB = int(playerB + game.winnings_per_seat[0])
        round+=1
