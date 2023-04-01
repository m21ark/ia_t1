from math import sqrt
import pygame

'''
This file contains the constants used in the game.
'''

# Define the nodes codes
EMPTY_NODE = 0
START_NODE = 1
END_NODE = 2
PATH_NODE = 3
PLAYER_NODE_A = 4
PLAYER_NODE_B = 5
BLOCK_NODE = 6
KILLER_NODE = 7

# Define the maze size
TILE_SIZE = 28
ROW = 30
COL = 30

# Define the tileset
tileset_image = pygame.image.load('assets/tileset.png')
tile_positions = [(1, 1),  # EmptyNode
                  (15, 7),  # StartNode
                  (13, 6),  # EndNode
                  (15, 0),  # PathNode
                  (0, 8),  # PlayerNode
                  (0, 8),  # PlayerNode
                  (5, 0),  # BlockNode
                  (9, 9)]  # KillerNode


# Define the window size and block size
screen_width = TILE_SIZE * COL
screen_height = TILE_SIZE * ROW
WINDOW_SIZE = (screen_width, screen_height)


# Create title string
title = "Space Block"

BLACK = (0, 0, 0)

# Define the colors to use for the blocks
GREY = (30, 30, 30)  # EmptyNode
WHITE = (255, 255, 255)  # StartNode
RED = (255, 0, 0)  # EndNode
GREEN = (0, 255, 0)  # PathNode
BLUE = (0, 0, 255)  # PlayerNode
YELLOW = (255, 255, 0)  # BlockNode
PURPLE = (255, 0, 255)  # KillerNode
LIGHT_BLUE = (133, 201, 232)  # PlayerNode
BG_COLOR = (40, 41, 35)

INVALID_NODES = [BLOCK_NODE, KILLER_NODE, EMPTY_NODE]

WINDOW = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption(title)