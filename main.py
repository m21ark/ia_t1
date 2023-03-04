import pygame
import datetime
from math import sqrt
from collections import deque


# ==========================================================================================================================



class BlockState:
	
	def __init__(self, x, y, x2, y2):
		self.x = x
		self.y = y
		self.x2 = x2
		self.y2 = y2
		
	def __eq__(self, other):
		if isinstance(other, self.__class__):
			return self.__dict__ == other.__dict__
		return False

	def __ne__(self, other):
		return not self.__eq__(other)
		
	def __hash__(self):
		return hash((x,y,x2,y2))
		
	def __str__(self):
		return f"{self.x} , {self.y} : {self.x2} , {self.y2}"
		








# ==========================================================================================================================


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

INVALID_NODES = [BLOCK_NODE]

game_map = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
            0, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 3, 3, 0,
            0, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0, 0, 0, 0, 0, 0, 0, 3, 3, 3, 3, 6, 3, 0,
            0, 3, 3, 1, 3, 3, 3, 3, 6, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0,
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


# ==========================================================================================================================

# returns path between start and end points (x,y) in a matrix
def bfs(matrix, start, end):
    # Define the dimensions of the matrix
    rows = int(sqrt(len(matrix)))
    cols = rows

    # Define a queue for BFS and a visited set to keep track of visited nodes
    queue = deque()
    visited = set()

    # Define a dictionary to store the path from each node to the start point
    path = {}
    path[start] = None

    # Add the starting point to the queue and mark it as visited
    queue.append(start)
    visited.add(start)

    # Loop until the queue is empty
    while queue:
        # Get the next node from the queue
        current = queue.popleft()

        # Check if the current node is the end point
        if current == end:
            # Build the path by following the parent pointers from the end point
            result = []
            while current is not None:
                result.append(current)
                current = path[current]
            result.reverse()
            return result

        # Get the row and column indices of the current node
        row, col = current

        # Check the neighbors of the current node
        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            # Compute the row and column indices of the neighbor
            neighbor_row = row + dr
            neighbor_col = col + dc

            # Check if the neighbor is within the bounds of the matrix
            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                # Check if the neighbor has not been visited and is a path node
                if matrix[neighbor_row + neighbor_col*MATRIX_COL] in [START_NODE, PATH_NODE, END_NODE] and (neighbor_row, neighbor_col) not in visited:
                    # Add the neighbor to the queue and mark it as visited
                    queue.append((neighbor_row, neighbor_col))
                    visited.add((neighbor_row, neighbor_col))
                    # Store the path from the current node to the neighbor
                    path[(neighbor_row, neighbor_col)] = current

    # If we reach this point, the end point is not reachable from the start point
    return None


# ==========================================================================================================================

def play_again(window, font, display_text):

    # Render text
    text = font.render(display_text, True, WHITE)

    # Get text rect
    text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))

    # Set up buttons
    play_again_button = pygame.Rect(
        screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
    play_again_text = font.render("Play Again", True, BLACK)
    play_again_text_rect = play_again_text.get_rect(
        center=play_again_button.center)

    quit_button = pygame.Rect(screen_width // 2 - 100,
                              screen_height // 2 + 110, 200, 50)
    quit_text = font.render("Quit", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_button.collidepoint(mouse_pos):

                    # Play again
                    return True

                elif quit_button.collidepoint(mouse_pos):
                    # Quit the game
                    pygame.quit()
                    quit()

        # Clear the screen
        window.fill(BLACK)

        # Draw text and buttons
        window.blit(text, text_rect)
        pygame.draw.rect(window, WHITE, play_again_button)
        window.blit(play_again_text, play_again_text_rect)
        pygame.draw.rect(window, WHITE, quit_button)
        window.blit(quit_text, quit_text_rect)

        # Update the display
        pygame.display.update()


def title_screen():

    # Initialize Pygame
    pygame.init()

    screen = pygame.display.set_mode((screen_width, screen_height))

    # Create font object
    font = pygame.font.Font(None, 64)

    # Render title text
    title_text = font.render(title, True, WHITE)
    title_rect = title_text.get_rect()

    # Center title text on screen
    title_rect.centerx = screen.get_rect().centerx
    title_rect.centery = screen.get_rect().centery - 100

    # Set up buttons
    play_again_button = pygame.Rect(
        screen_width // 2 - 140, screen_height // 2 + 50, 280, 50)
    play_again_text = font.render("Play", True, BLACK)
    play_again_text_rect = play_again_text.get_rect(
        center=play_again_button.center)

    quit_button = pygame.Rect(screen_width // 2 - 140,
                              screen_height // 2 + 110, 280, 50)
    quit_text = font.render("Quit", True, BLACK)
    quit_text_rect = quit_text.get_rect(center=quit_button.center)

    # Game loop
    while True:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if play_again_button.collidepoint(mouse_pos):

                    # Start game
                    return True

                elif quit_button.collidepoint(mouse_pos):
                    # Quit the game
                    pygame.quit()
                    quit()

        # Clear the screen
        screen.fill((0, 0, 0))

        # Draw title text
        screen.blit(title_text, title_rect)

        pygame.draw.rect(screen, WHITE, play_again_button)
        screen.blit(play_again_text, play_again_text_rect)
        pygame.draw.rect(screen, WHITE, quit_button)
        screen.blit(quit_text, quit_text_rect)

        # Update the display
        pygame.display.update()


def game():

    # Initialize Pygame
    pygame.init()

    FONT = pygame.font.Font(None, 48)

    # Create the window
    window = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption(title)

    # Create a dictionary to keep track of which keys are currently pressed
    keys_pressed = {}

    clock = pygame.time.Clock()

    # Get current time
    start_time = datetime.datetime.now()

    # Main game loop
    running = True
    while running:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                keys_pressed[event.key] = True
            elif event.type == pygame.KEYUP:
                keys_pressed[event.key] = False

        # Check for key presses
        if keys_pressed.get(pygame.K_a):
            # print("A pressed")
            p.moveLeft()
        if keys_pressed.get(pygame.K_w):
            # print("W pressed")
            p.moveUp()
        if keys_pressed.get(pygame.K_s):
            # print("S pressed")
            p.moveDown()
        if keys_pressed.get(pygame.K_d):
            # print("D pressed")
            p.moveRight()
        if keys_pressed.get(pygame.K_RETURN):
            # print("Enter pressed")

            # Display the confirmation prompt and wait for a response
            text = FONT.render(
                "Go back to title screen? (Y/N)", True, (255, 255, 255))
            window.blit(text, (10, 10))
            pygame.display.update()

            curr = datetime.datetime.now()

            # Wait for a response from the user
            response = None
            while response is None:
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        key_name = pygame.key.name(event.key)
                        if key_name == "y":
                            response = True
                        elif key_name == "n":
                            response = False
                            keys_pressed[pygame.K_RETURN] = False

                            # To stop the timer correctly
                            start_time -= curr

            # Quit the game if the user confirmed
            if response:
                running = False

        else:
            pass
            # print("Nothing pressed!\n")

        ret = False
        if (p.checkSpecialNodes(END_NODE)):
            print("You have reached the end!")
            ret = play_again(window, FONT, "You win!")

        elif (p.checkSpecialNodes(EMPTY_NODE)):
            print("You have fallen!")
            ret = play_again(window, FONT, "You lose!")

        elif (p.checkSpecialNodes(KILLER_NODE)):
            print("You have been killed!")
            ret = play_again(window, FONT, "You died!")

        if (ret):
            game_map = p.get_restart_map()
            ret = False
            keys_pressed = {}
            start_time = datetime.datetime.now()

            print_map()
        else:
            game_map = p.get_new_map()

        # Draw the blocks
        for row in range(MATRIX_ROW):
            for col in range(MATRIX_COL):
                x = row * BLOCK_SIZE
                y = col * BLOCK_SIZE
                color = get_color(game_map, row, col)
                pygame.draw.rect(window, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))

        # Calculate time elapsed
        time_elapsed = datetime.datetime.now() - start_time
        time_elapsed_str = "Time: " + str(time_elapsed.seconds) + "s"

        # Render time elapsed text
        time_elapsed_text = FONT.render(time_elapsed_str, True, WHITE)
        time_elapsed_rect = time_elapsed_text.get_rect()
        time_elapsed_rect.topright = (screen_width - 5, 10)

        # Draw time elapsed text
        window.blit(time_elapsed_text, time_elapsed_rect)

        # Update the display
        pygame.display.update()

        # Limit the game speed to 10 frames per second
        clock.tick(10)

        #print(f"{p.x} | {p.y} : {p.x2} | {p.y2}")

    # Quit Pygame
    pygame.quit()


# ==========================================================================================================================


def get_node(x, y):
    return game_map[x + y * MATRIX_COL]


def set_node(x, y, value):
    game_map[x + y * MATRIX_COL] = value


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


def get_node_type(x, y):
    node = get_node(x, y)
    if node == EMPTY_NODE:
        return "O"
    elif node == START_NODE:
        return "S"
    elif node == END_NODE:
        return "E"
    elif node == PATH_NODE:
        return "P"
    elif node == PLAYER_NODE_A:
        return "X"
    elif node == PLAYER_NODE_B:
        return "Y"
    elif node == BLOCK_NODE:
        return "B"
    elif node == KILLER_NODE:
        return "K"
    else:
        return "?"


def print_map():
    for y in range(MATRIX_COL):
        for x in range(MATRIX_ROW):
            print(get_node_type(x, y), end=" ")
        print()


def find_start_end_nodes():
    for y in range(MATRIX_COL):
        for x in range(MATRIX_ROW):
            if get_node(x, y) == START_NODE:
                start_x = x
                start_y = y
                break
    # print("Start node found at", start_x, start_y)

    for y in range(MATRIX_COL):
        for x in range(MATRIX_ROW):
            if get_node(x, y) == END_NODE:
                end_x = x
                end_y = y
                break
    # print("End node found at", end_x, end_y)

    return start_x, start_y, end_x, end_y


class Player:
    def __init__(self, game_map, x, y):
        self.game_map = game_map
        self.x = x
        self.y = y
        self.x2 = x
        self.y2 = y

        self.xs, self.ys = x, y  # store the start position
        self.old_board = game_map.copy()

    def get_restart_map(self):
        self.x = self.xs
        self.y = self.ys
        self.x2 = self.xs
        self.y2 = self.ys
        return self.old_board

    def isYtopX(self):  # Y is on top of X
        return self.x == self.x2 and self.y2 < self.y

    def isXtopY(self):  # X is on top of Y
        return self.x == self.x2 and self.y2 > self.y

    def isYrightX(self):  # Y is on right of X
        return self.y == self.y2 and self.x2 > self.x

    def isXrightY(self):  # X is on right of Y
        return self.y == self.y2 and self.x2 < self.x

    def isStanding(self):
        return self.x == self.x2 and self.y == self.y2

    def checkSpecialNodes(self, node):
        a = self.game_map[self.x + self.y * MATRIX_COL] == node
        b = self.game_map[self.x2 + self.y2 * MATRIX_COL] == node
        return a or b

    def get_new_map(self):
        self.game_map[self.x2 + self.y2 * MATRIX_COL] = PLAYER_NODE_B
        self.game_map[self.x + self.y * MATRIX_COL] = PLAYER_NODE_A
        return self.game_map

    def clearPosition(self, x, y):
        self.game_map[x + y * MATRIX_COL] = PATH_NODE

    # currently not used
    def checkIfCanMove(self):

        if self.x > MATRIX_ROW-1 or self.x < 0 or self.y > MATRIX_COL-1 or self.y < 0:
            return False  # out of bounds

        if self.x2 > MATRIX_ROW-1 or self.x2 < 0 or self.y2 > MATRIX_COL-1 or self.y2 < 0:
            return False  # out of bounds

        a = self.game_map[self.x + self.y * MATRIX_COL] not in INVALID_NODES
        b = self.game_map[self.x2 + self.y2 * MATRIX_COL] not in INVALID_NODES
        return a and b

    def moveUp(self):

        # save current position
        a, b, c, d = self.x, self.y, self.x2, self.y2

        if (self.isStanding()):
            self.clearPosition(self.x, self.y)
            self.y2 -= 2
            self.y -= 1

        else:

            self.clearPosition(self.x, self.y)
            self.clearPosition(self.x2, self.y2)

            if (self.isYtopX()):
                self.x = self.x2
                self.y2 -= 1
                self.y = self.y2

            elif (self.isXtopY()):
                self.x2 = self.x
                self.y -= 1
                self.y2 = self.y

            else:  # X and Y are on the same row
                self.y -= 1
                self.y2 -= 1

        # check if new position is valid. If not, revert to old position
        if (not self.checkIfCanMove()):
            self.x, self.y, self.x2, self.y2 = a, b, c, d
            return False

        return True

    def moveDown(self):

        # save current position
        a, b, c, d = self.x, self.y, self.x2, self.y2

        if (self.isStanding()):
            self.clearPosition(self.x, self.y)
            self.y2 += 2
            self.y += 1

        else:

            self.clearPosition(self.x, self.y)
            self.clearPosition(self.x2, self.y2)

            if (self.isXtopY()):
                self.x = self.x2
                self.y2 += 1
                self.y = self.y2

            elif (self.isYtopX()):
                self.x2 = self.x
                self.y += 1
                self.y2 = self.y

            else:  # X and Y are on the same row
                self.y += 1
                self.y2 += 1

        # check if new position is valid. If not, revert to old position
        if (not self.checkIfCanMove()):
            self.x, self.y, self.x2, self.y2 = a, b, c, d
            return False
        return True

    def moveLeft(self):

        # save current position
        a, b, c, d = self.x, self.y, self.x2, self.y2

        if (self.isStanding()):
            self.clearPosition(self.x, self.y)
            self.x2 -= 1
            self.x -= 2

        else:
            self.clearPosition(self.x, self.y)
            self.clearPosition(self.x2, self.y2)
            
            if (self.isXrightY()):
                self.y = self.y2
                self.x2 -= 1
                self.x = self.x2

            elif (self.isYrightX()):
                self.y2 = self.y
                self.x -= 1
                self.x2 = self.x

            else:  # X and Y are on the same col
                self.x -= 1
                self.x2 -= 1

        # check if new position is valid. If not, revert to old position
        if (not self.checkIfCanMove()):
            self.x, self.y, self.x2, self.y2 = a, b, c, d
            return False
        return True

    def moveRight(self):

        # save current position
        a, b, c, d = self.x, self.y, self.x2, self.y2

        if (self.isStanding()):
            self.clearPosition(self.x, self.y)
            self.x2 += 1
            self.x += 2

        else:
            self.clearPosition(self.x, self.y)
            self.clearPosition(self.x2, self.y2)

            if (self.isYrightX()):
                self.y = self.y2
                self.x2 += 1
                self.x = self.x2

            elif (self.isXrightY()):
                self.y2 = self.y
                self.x += 1
                self.x2 = self.x

            else:  # X and Y are on the same col
                self.x += 1
                self.x2 += 1

        # check if new position is valid. If not, revert to old position
        if (not self.checkIfCanMove()):
            self.x, self.y, self.x2, self.y2 = a, b, c, d
            return False
        return True

    def get_position(self):
        return self.x, self.y, self.x2, self.y2


if __name__ == "__main__":
    start_x, start_y, end_x, end_y = find_start_end_nodes()
    p = Player(game_map, start_x, start_y)
    set_node(start_x, start_y, PLAYER_NODE_A)

    path = bfs(game_map, (start_x, start_y), (end_x, end_y))

    # print(f"{start_x}, {start_y}, {end_x}, {end_y}")
    # print(path)
    # print_map()

 
    # When quitting the game, go back to the title screen
    while (title_screen()):
        game()
