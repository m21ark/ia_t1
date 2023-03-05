from view.view_const import *
from model.sample_mazes import *
import pygame

class GameView:
    def __init__(self, surface, model):
        self.surface = surface
        self.model = model
    
    def get_color(array, x, y):
        node = array[x + MATRIX_COL * y]
        if node == EMPTY_NODE:
            return GREY
        elif node == START_NODE:
            return WHITE
        elif node == END_NODE:
            return RED
        elif node == PATH_NODE:
            return GREEN
        elif node == PLAYER_NODE_A:
            return BLUE
        elif node == PLAYER_NODE_B:
            return BLUE
        elif node == BLOCK_NODE:
            return YELLOW
        elif node == KILLER_NODE:
            return PURPLE
        else:
            return BLACK
   
    def draw_maze(self):
        for x in range(MATRIX_COL):
            for y in range(MATRIX_ROW):
                pygame.draw.rect(self.surface, GameView.get_color(self.model.get_maze, x, y), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_block(self):
        if self.model.get_block.isStanding():
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x * BLOCK_SIZE, self.model.get_block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x * BLOCK_SIZE, self.model.get_block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x2 * BLOCK_SIZE, self.model.get_block.y2 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
