from view.view_const import *
from model.sample_mazes import *


class BlockState:
    '''
    This class represents a state of the block puzzle.
    It contains the x and y coordinates of the two blocks.
    It also contains the maze that the blocks are in.
    '''

    def __init__(self, x, y, x2, y2, maze):
        '''
        :param x: x coordinate of block 1
        :param y: y coordinate of block 1
        :param x2: x coordinate of block 2
        :param y2: y coordinate of block 2
        :param maze: the maze that the blocks are in
        '''

        self.x = x
        self.y = y
        self.x2 = x2
        self.y2 = y2
        self.maze = maze

    def __eq__(self, other):
        '''
        This method is used to compare two states.
        :param other: the other state
        '''
        if isinstance(other, self.__class__):
            return (self.x, self.y, self.x2, self.y2) == \
                   (other.x, other.y, other.x2, other.y2) \
                or (self.x == other.x2 and self.y == other.y2 and self.x2 == other.x and self.y2 == other.y)

        return False

    def __ne__(self, other):
        '''
        This method is used to compare two states.
        '''
        return not self.__eq__(other)

    def __hash__(self):
        '''
        This method is used to hash the state.
        '''
        x1 = min(self.x, self.x2)
        x3 = max(self.x, self.x2)
        y1 = min(self.y, self.y2)
        y3 = max(self.y, self.y2)
        return hash((x1, y1, x3, y3))

    def __str__(self):
        '''
        This method is used to print the state.
        '''
        return f"{self.x} , {self.y} : {self.x2} , {self.y2}"

    def isStanding(self):
        '''
        This method checks if the blocks are standing.
        '''
        return self.x == self.x2 and self.y == self.y2

    def isYtopX(self):  # Y is on top of X
        '''
        This method checks if block 2 is on top of block 1.
        '''
        return self.x == self.x2 and self.y2 < self.y

    def isXtopY(self):  # X is on top of Y
        ''' 
        This method checks if block 1 is on top of block 2.
        '''
        return self.x == self.x2 and self.y2 > self.y

    def isYrightX(self):  # Y is on right of X
        '''
        This method checks if block 2 is on the right of block 1.
        '''
        return self.y == self.y2 and self.x2 > self.x

    def isXrightY(self):  # X is on right of Y
        '''
        This method checks if block 1 is on the right of block 2.
        '''
        return self.y == self.y2 and self.x2 < self.x

    def checkIfCanMove(self):
        '''
        This method checks if the blocks can move.
        '''
        if self.x > MATRIX_ROW-1 or self.x < 0 or self.y > MATRIX_COL-1 or self.y < 0:
            return False  # out of bounds
        if self.x2 > MATRIX_ROW-1 or self.x2 < 0 or self.y2 > MATRIX_COL-1 or self.y2 < 0:
            return False  # out of bounds
        if self.maze[self.x + self.y * MATRIX_COL] == BLOCK_NODE or self.maze[self.x2 + self.y2 * MATRIX_COL] == BLOCK_NODE:
            return False  # blocked

        if bool(self.maze[self.x + self.y * MATRIX_COL] == END_NODE) ^ bool(self.maze[self.x2 + self.y2 * MATRIX_COL] == END_NODE):
            return False  # broken end node

        a = self.maze[self.x + self.y * MATRIX_COL] not in INVALID_NODES
        b = self.maze[self.x2 + self.y2 * MATRIX_COL] not in INVALID_NODES
        return a and b

    def checkIfGoal(self):
        '''
        This method checks if the blocks are in the goal state.
        '''
        return self.maze[self.x + self.y * MATRIX_COL] == END_NODE and self.maze[self.x2 + self.y2 * MATRIX_COL] == END_NODE
