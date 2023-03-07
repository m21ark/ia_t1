from math import sqrt
import pygame

EMPTY_NODE = 0
START_NODE = 1
END_NODE = 2
PATH_NODE = 3
PLAYER_NODE_A = 4
PLAYER_NODE_B = 5
BLOCK_NODE = 6
KILLER_NODE = 7


TILE_SIZE = 32

"""
xs - 32
s - 40
m - 64
l - 128
"""

tileset_image = pygame.image.load('assets/tileset_s_new.png')
ROW = 30
COL = 30

tile_positions = [(1, 9),  # EmptyNode
                  (12, 6),  # StartNode
                  (12, 9),  # EndNode
                  (15, 0),  # PathNode
                  (0, 8),  # PlayerNode
                  (0, 8),  # PlayerNode
                  (11, 9),  # BlockNode
                  (3, 9)]  # KillerNode


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

INVALID_NODES = [KILLER_NODE, EMPTY_NODE]

WINDOW = pygame.display.set_mode(WINDOW_SIZE, pygame.RESIZABLE)
pygame.display.set_caption(title)
