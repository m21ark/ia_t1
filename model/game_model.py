from algorithms.block_state import BlockState
from math import sqrt
from model.sample_mazes import *


class GameModel:
    """
    The model of the game. It contains the maze and the blockStates.
    Responsible for the game logic.

    Attributes:
        maze (list): The maze of the game.
        block (BlockState): The block of the game.
        nr_moves (int): The number of moves the player has made.
    """
    sel_maze = game_maps[0][1]
    GOAL = (0,0)
    def __init__(self, maze):
        """
        The constructor for GameModel class.

        Parameters
        ----------
        maze : list
            The maze of the game.
        
        """
        self.maze = maze
        start_x, start_y = self.find_start_end_nodes(maze)
        self.block = BlockState(start_x, start_y, start_x, start_y, maze)
        self.nr_moves = 0

    @staticmethod
    def find_start_end_nodes(maze):
        """
        Finds the start and end nodes of the maze.

        Parameters
        ----------
        maze : list
            The maze of the game.

        Returns
        -------
        tuple
            The start (x, y) nodes of the maze.
        """

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
                elif get_node(x, y) == END_NODE:
                    GameModel.GOAL = (x,y)

    @property
    def get_maze(self):
        """
        Returns the maze of the game.
        """
        return self.maze

    @property
    def get_block(self):
        """
        Returns the block state of the game.
        """
        return self.block

    def set_block(self, block):
        """
        Sets the block state of the game.
        """
        self.block = block

    def reset_block(self):
        """ 
        Resets the block state of the game. Puts the block back to the start position.
        """
        start_x, start_y = self.find_start_end_nodes(self.block.maze)
        self.block = BlockState(
            start_x, start_y, start_x, start_y, self.block.maze)

    @property
    def get_nr_moves(self):
        """
        Returns the number of moves the player has made.
        """
        return self.nr_moves

    def increment_nr_moves(self):
        """
        Increments the number of moves the player has made.
        """
        self.nr_moves += 1

    def reset_nr_moves(self):
        """
        Resets the number of moves the player has made.
        """
        self.nr_moves = 0
