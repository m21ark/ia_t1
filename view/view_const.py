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

# Define the window size and block size
screen_width = 900  # 800
screen_height = 900  # 800
WINDOW_SIZE = (screen_width, screen_height)


# Create title string
title = "My Awesome Game"

BLACK = (0, 0, 0)

# Define the colors to use for the blocks
GREY = (30, 30, 30)  # EmptyNode
WHITE = (255, 255, 255)  # StartNode
RED = (255, 0, 0)  # EndNode
GREEN = (0, 255, 0)  # PathNode
BLUE = (0, 0, 255)  # PlayerNode
YELLOW = (255, 255, 0)  # BlockNode
PURPLE = (255, 0, 255)  # KillerNode

INVALID_NODES = [BLOCK_NODE, KILLER_NODE, EMPTY_NODE]

WINDOW = pygame.display.set_mode(WINDOW_SIZE)
