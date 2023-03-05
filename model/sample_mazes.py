from math import sqrt

game_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0,
            0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 6, 3, 0,
            0, 3, 3, 1, 3, 2, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
            0, 3, 3, 3, 3, 3, 7, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 6, 3, 3, 3, 3, 0,
            0, 3, 3, 6, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0,
            0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 6, 3, 0, 0, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 3, 3, 7, 3, 3, 3, 3, 3, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 7, 3, 7, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 3, 7, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 6, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            3, 3, 3, 3, 3, 3, 6, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0,
            0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 6, 3,
            0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 7, 3, 3, 3, 3,
            0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 7, 3, 3, 3, 3, 3,
            0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 6, 3, 2, 2, 3, 3, 3,
            0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 3, 0, 0, 0, 0, 0, 3, 7, 3, 3, 3, 3, 3, 3,
            0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 6,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3]
"""
game_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0,
            0, 0, 0, 3, 3, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 7, 6, 3, 3, 3, 3, 3, 3, 3, 0, 0,
            0, 0, 3, 3, 3, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 6, 3, 3, 0,
            0, 7, 3, 7, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 7, 3, 3, 0,
            0, 3, 3, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 3, 7, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 3, 3, 0,
            0, 3, 3, 0, 0, 0, 0, 0, 7, 7, 3, 0, 0, 0, 7, 3, 0, 0, 0, 0, 0, 0, 3, 7, 0, 0, 0, 3, 3, 0,
            0, 3, 3, 0, 0, 0, 0, 0, 0, 7, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 3, 7, 0,
            0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 3, 7, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 3, 3, 0, 0, 0, 3, 3, 3, 7, 3, 3, 0, 0, 0, 0, 0, 0, 3, 0, 3, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 3, 3, 7, 0, 0, 6, 3, 0, 3, 3, 0, 0, 0, 0, 3, 7, 0, 3, 0, 3, 3, 0, 0, 0, 0, 0, 7, 3, 0,
            0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 3, 0, 3, 3, 3, 3, 3, 3, 3, 0, 7, 3, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 3, 3, 0, 0, 0, 3, 3, 0, 0, 3, 0, 7, 3, 3, 7, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 2, 2, 3, 7, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 6, 3, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 0,
            0, 0, 7, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 7, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 6, 3, 3, 7, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 6, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 7, 3, 3, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 7, 7, 3, 3, 0, 0, 0, 0, 0, 0, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
            0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
            0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 3, 3, 7, 0, 0, 0, 0, 0, 0, 3, 7, 0,
            0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 3, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 7, 0, 0, 0, 0, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 3, 3, 6, 0, 0, 0, 0, 0, 0, 0, 3, 3, 0,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 1, 3,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3,
            0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 7]
"""


# Empty map for movement testing
"""
game_map = []

for i in range(30*30):
    game_map.append(3)

game_map[25 + 25*15] = 1
game_map[15 + 15*15] = 2
"""


MATRIX_ROW = round(sqrt(len(game_map)))
MATRIX_COL = MATRIX_ROW
BLOCK_SIZE = 900/MATRIX_ROW
