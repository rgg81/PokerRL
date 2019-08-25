# Copyright (c) 2019 Eric Steinberger


import unittest
from unittest import TestCase

import numpy as np

from PokerRL.game._.cpp_wrappers.CppHandeval import CppHandeval


class TestCppLib(TestCase):

    def test_get_hand_rank_52_holdem(self):
        cpp_poker = CppHandeval()
        b = np.array([[12,0], [3,0], [6,1], [0,1], [9,0]], dtype=np.int8)
        # h = np.array([[1,3], [1,1]], dtype=np.int8)
        # h2 = np.array([[11,1], [10,2]], dtype=np.int8)

        h = np.array([[1,3], [1,1]], dtype=np.int8)
        h2 = np.array([[11,1], [10,2]], dtype=np.int8)

        print(cpp_poker.get_hand_rank_52_holdem(hand_2d=h, board_2d=b))
        print(cpp_poker.get_hand_rank_52_holdem(hand_2d=h2, board_2d=b))
        assert isinstance(cpp_poker.get_hand_rank_52_holdem(hand_2d=h, board_2d=b), int)


if __name__ == '__main__':
    unittest.main()
