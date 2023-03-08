from algorithms.block_state import BlockState
from math import sqrt
from model.sample_mazes import *


class GameModel:
    sel_maze = game_maps[0][1]

    def __init__(self, maze):
        self.maze = maze
        start_x, start_y = self.find_start_end_nodes(maze)
        self.block = BlockState(start_x, start_y, start_x, start_y, maze)
        self.nr_moves = 0

    @staticmethod
    def find_start_end_nodes(maze):

        # hardcoded values :( to change later
        MATRIX_ROW = round(sqrt(len(maze)))
        MATRIX_COL = MATRIX_ROW
        START_NODE = 1
        END_NODE = 2

        def get_node(x, y):
            return maze[x + y * MATRIX_COL]

        for y in range(MATRIX_COL):
            for x in range(MATRIX_ROW):
                if get_node(x, y) == START_NODE:
                    return x, y

    @property
    def get_maze(self):
        return self.maze

    @property
    def get_block(self):
        return self.block

    def set_block(self, block):
        self.block = block

    def reset_block(self):
        start_x, start_y = self.find_start_end_nodes(self.block.maze)
        self.block = BlockState(
            start_x, start_y, start_x, start_y, self.block.maze)

    @property
    def get_nr_moves(self):
        return self.nr_moves

    def increment_nr_moves(self):
        self.nr_moves += 1

    def reset_nr_moves(self):
        self.nr_moves = 0
