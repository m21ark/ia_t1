import pygame
import datetime
from math import sqrt
from collections import deque
from view.view_const import *
from model.sample_mazes import *
from algorithms.block_state import BlockState
from menu.main_menu import MainMenu


# ==========================================================================================================================

# def play_again(window, font, display_text):
# 
#     # Render text
#     text = font.render(display_text, True, WHITE)
# 
#     # Get text rect
#     text_rect = text.get_rect(center=(screen_width // 2, screen_height // 2))
# 
#     # Set up buttons
#     play_again_button = pygame.Rect(
#         screen_width // 2 - 100, screen_height // 2 + 50, 200, 50)
#     play_again_text = font.render("Play Again", True, BLACK)
#     play_again_text_rect = play_again_text.get_rect(
#         center=play_again_button.center)
# 
#     quit_button = pygame.Rect(screen_width // 2 - 100,
#                               screen_height // 2 + 110, 200, 50)
#     quit_text = font.render("Quit", True, BLACK)
#     quit_text_rect = quit_text.get_rect(center=quit_button.center)
# 
#     # Game loop
#     while True:
#         # Handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 if play_again_button.collidepoint(mouse_pos):
# 
#                     # Play again
#                     return True
# 
#                 elif quit_button.collidepoint(mouse_pos):
#                     # Quit the game
#                     pygame.quit()
#                     quit()
# 
#         # Clear the screen
#         window.fill(BLACK)
# 
#         # Draw text and buttons
#         window.blit(text, text_rect)
#         pygame.draw.rect(window, WHITE, play_again_button)
#         window.blit(play_again_text, play_again_text_rect)
#         pygame.draw.rect(window, WHITE, quit_button)
#         window.blit(quit_text, quit_text_rect)
# 
#         # Update the display
#         pygame.display.update()
# 
# 
# def title_screen():
# 
#     # Initialize Pygame
#     pygame.init()
# 
#     screen = pygame.display.set_mode((screen_width, screen_height))
# 
#     # Create font object
#     font = pygame.font.Font(None, 64)
# 
#     # Render title text
#     title_text = font.render(title, True, WHITE)
#     title_rect = title_text.get_rect()
# 
#     # Center title text on screen
#     title_rect.centerx = screen.get_rect().centerx
#     title_rect.centery = screen.get_rect().centery - 100
# 
#     # Set up buttons
#     play_again_button = pygame.Rect(
#         screen_width // 2 - 140, screen_height // 2 + 50, 280, 50)
#     play_again_text = font.render("Play", True, BLACK)
#     play_again_text_rect = play_again_text.get_rect(
#         center=play_again_button.center)
# 
#     quit_button = pygame.Rect(screen_width // 2 - 140,
#                               screen_height // 2 + 110, 280, 50)
#     quit_text = font.render("Quit", True, BLACK)
#     quit_text_rect = quit_text.get_rect(center=quit_button.center)
# 
#     # Game loop
#     while True:
#         # Handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 quit()
#             elif event.type == pygame.MOUSEBUTTONDOWN:
#                 mouse_pos = pygame.mouse.get_pos()
#                 if play_again_button.collidepoint(mouse_pos):
# 
#                     # Start game
#                     return True
# 
#                 elif quit_button.collidepoint(mouse_pos):
#                     # Quit the game
#                     pygame.quit()
#                     quit()
# 
#         # Clear the screen
#         screen.fill((0, 0, 0))
# 
#         # Draw title text
#         screen.blit(title_text, title_rect)
# 
#         pygame.draw.rect(screen, WHITE, play_again_button)
#         screen.blit(play_again_text, play_again_text_rect)
#         pygame.draw.rect(screen, WHITE, quit_button)
#         screen.blit(quit_text, quit_text_rect)
# 
#         # Update the display
#         pygame.display.update()
# 
# 
# def game():
# 
#     # Initialize Pygame
#     pygame.init()
# 
#     FONT = pygame.font.Font(None, 48)
# 
#     # Create the window
#     window = pygame.display.set_mode(WINDOW_SIZE)
#     pygame.display.set_caption(title)
# 
#     # Create a dictionary to keep track of which keys are currently pressed
#     keys_pressed = {}
# 
#     clock = pygame.time.Clock()
# 
#     # Get current time
#     start_time = datetime.datetime.now()
# 
#     # Main game loop
#     running = True
#     while running:
#         # Handle events
#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 running = False
#             elif event.type == pygame.KEYDOWN:
#                 keys_pressed[event.key] = True
#             elif event.type == pygame.KEYUP:
#                 keys_pressed[event.key] = False
# 
#         # Check for key presses
#         if keys_pressed.get(pygame.K_a):
#             # print("A pressed")
#             p.moveLeft()
#         if keys_pressed.get(pygame.K_w):
#             # print("W pressed")
#             p.moveUp()
#         if keys_pressed.get(pygame.K_s):
#             # print("S pressed")
#             p.moveDown()
#         if keys_pressed.get(pygame.K_d):
#             # print("D pressed")
#             p.moveRight()
#         if keys_pressed.get(pygame.K_RETURN):
#             # print("Enter pressed")
# 
#             # Display the confirmation prompt and wait for a response
#             text = FONT.render(
#                 "Go back to title screen? (Y/N)", True, (255, 255, 255))
#             window.blit(text, (10, 10))
#             pygame.display.update()
# 
#             curr = datetime.datetime.now()
# 
#             # Wait for a response from the user
#             response = None
#             while response is None:
#                 for event in pygame.event.get():
#                     if event.type == pygame.KEYDOWN:
#                         key_name = pygame.key.name(event.key)
#                         if key_name == "y":
#                             response = True
#                         elif key_name == "n":
#                             response = False
#                             keys_pressed[pygame.K_RETURN] = False
# 
#                             # To stop the timer correctly
#                             start_time -= curr
# 
#             # Quit the game if the user confirmed
#             if response:
#                 running = False
# 
#         else:
#             pass
#             # print("Nothing pressed!\n")
# 
#         ret = False
#         if (p.checkSpecialNodes(END_NODE)):
#             print("You have reached the end!")
#             ret = play_again(window, FONT, "You win!")
# 
#         elif (p.checkSpecialNodes(EMPTY_NODE)):
#             print("You have fallen!")
#             ret = play_again(window, FONT, "You lose!")
# 
#         elif (p.checkSpecialNodes(KILLER_NODE)):
#             print("You have been killed!")
#             ret = play_again(window, FONT, "You died!")
# 
#         if (ret):
#             game_map = p.get_restart_map()
#             ret = False
#             keys_pressed = {}
#             start_time = datetime.datetime.now()
# 
#             print_map()
#         else:
#             game_map = p.get_new_map()
# 
#         # Draw the blocks
#         for row in range(MATRIX_ROW):
#             for col in range(MATRIX_COL):
#                 x = row * BLOCK_SIZE
#                 y = col * BLOCK_SIZE
#                 color = get_color(game_map, row, col)
#                 pygame.draw.rect(window, color, (x, y, BLOCK_SIZE, BLOCK_SIZE))
# 
#         # Calculate time elapsed
#         time_elapsed = datetime.datetime.now() - start_time
#         time_elapsed_str = "Time: " + str(time_elapsed.seconds) + "s"
# 
#         # Render time elapsed text
#         time_elapsed_text = FONT.render(time_elapsed_str, True, WHITE)
#         time_elapsed_rect = time_elapsed_text.get_rect()
#         time_elapsed_rect.topright = (screen_width - 5, 10)
# 
#         # Draw time elapsed text
#         window.blit(time_elapsed_text, time_elapsed_rect)
# 
#         # Update the display
#         pygame.display.update()
# 
#         # Limit the game speed to 10 frames per second
#         clock.tick(10)
# 
#         #print(f"{p.x} | {p.y} : {p.x2} | {p.y2}")
# 
#     # Quit Pygame
#     pygame.quit()
# 
# 
# # ==========================================================================================================================
# 
# 
# def get_node(x, y):
#     return game_map[x + y * MATRIX_COL]
# 
# 
# def set_node(x, y, value):
#     game_map[x + y * MATRIX_COL] = value
# 
# 
# def get_color(array, x, y):
#     node = array[x + MATRIX_COL * y]
#     if node == EMPTY_NODE:
#         return GREY
#     elif node == START_NODE:
#         return WHITE
#     elif node == END_NODE:
#         return RED
#     elif node == PATH_NODE:
#         return GREEN
#     elif node == PLAYER_NODE_A:
#         return BLUE
#     elif node == PLAYER_NODE_B:
#         return BLUE
#     elif node == BLOCK_NODE:
#         return YELLOW
#     elif node == KILLER_NODE:
#         return PURPLE
#     else:
#         return BLACK
# 
# 
# def get_node_type(x, y):
#     node = get_node(x, y)
#     if node == EMPTY_NODE:
#         return "O"
#     elif node == START_NODE:
#         return "S"
#     elif node == END_NODE:
#         return "E"
#     elif node == PATH_NODE:
#         return "P"
#     elif node == PLAYER_NODE_A:
#         return "X"
#     elif node == PLAYER_NODE_B:
#         return "Y"
#     elif node == BLOCK_NODE:
#         return "B"
#     elif node == KILLER_NODE:
#         return "K"
#     else:
#         return "?"
# 
# 
# def print_map():
#     for y in range(MATRIX_COL):
#         for x in range(MATRIX_ROW):
#             print(get_node_type(x, y), end=" ")
#         print()
# 
# 
# def find_start_end_nodes():
#     for y in range(MATRIX_COL):
#         for x in range(MATRIX_ROW):
#             if get_node(x, y) == START_NODE:
#                 start_x = x
#                 start_y = y
#                 break
#     # print("Start node found at", start_x, start_y)
# 
#     for y in range(MATRIX_COL):
#         for x in range(MATRIX_ROW):
#             if get_node(x, y) == END_NODE:
#                 end_x = x
#                 end_y = y
#                 break
#     # print("End node found at", end_x, end_y)
# 
#     return start_x, start_y, end_x, end_y
# 
# 
# class Player:
#     def __init__(self, game_map, x, y):
#         self.game_map = game_map
#         self.x = x
#         self.y = y
#         self.x2 = x
#         self.y2 = y
# 
#         self.xs, self.ys = x, y  # store the start position
#         self.old_board = game_map.copy()
# 
#     def get_restart_map(self):
#         self.x = self.xs
#         self.y = self.ys
#         self.x2 = self.xs
#         self.y2 = self.ys
#         return self.old_board
# 
#     def isYtopX(self):  # Y is on top of X
#         return self.x == self.x2 and self.y2 < self.y
# 
#     def isXtopY(self):  # X is on top of Y
#         return self.x == self.x2 and self.y2 > self.y
# 
#     def isYrightX(self):  # Y is on right of X
#         return self.y == self.y2 and self.x2 > self.x
# 
#     def isXrightY(self):  # X is on right of Y
#         return self.y == self.y2 and self.x2 < self.x
# 
#     def isStanding(self):
#         return self.x == self.x2 and self.y == self.y2
# 
#     def checkSpecialNodes(self, node):
#         a = self.game_map[self.x + self.y * MATRIX_COL] == node
#         b = self.game_map[self.x2 + self.y2 * MATRIX_COL] == node
#         return a or b
# 
#     def get_new_map(self):
#         self.game_map[self.x2 + self.y2 * MATRIX_COL] = PLAYER_NODE_B
#         self.game_map[self.x + self.y * MATRIX_COL] = PLAYER_NODE_A
#         return self.game_map
# 
#     def clearPosition(self, x, y):
#         self.game_map[x + y * MATRIX_COL] = PATH_NODE
# 
#     # currently not used
#     def checkIfCanMove(self):
# 
#         if self.x > MATRIX_ROW-1 or self.x < 0 or self.y > MATRIX_COL-1 or self.y < 0:
#             return False  # out of bounds
# 
#         if self.x2 > MATRIX_ROW-1 or self.x2 < 0 or self.y2 > MATRIX_COL-1 or self.y2 < 0:
#             return False  # out of bounds
# 
#         a = self.game_map[self.x + self.y * MATRIX_COL] not in INVALID_NODES
#         b = self.game_map[self.x2 + self.y2 * MATRIX_COL] not in INVALID_NODES
#         return a and b
# 
#     def get_position(self):
#         return self.x, self.y, self.x2, self.y2
# 

# if __name__ == "__main__":
#     start_x, start_y, end_x, end_y = find_start_end_nodes()
#     p = Player(game_map, start_x, start_y)
#     set_node(start_x, start_y, PLAYER_NODE_A)
# 
#      # path = bfs(game_map, (start_x, start_y), (end_x, end_y))
#  # 
#      # # print(f"{start_x}, {start_y}, {end_x}, {end_y}")
#      # print(path)
#     # print_map()
# 
#  
#     # When quitting the game, go back to the title screen
#     while (title_screen()):
#         game()
# 


def main():
    pygame.init()

    main_menu = MainMenu(WINDOW_SIZE).main_menu

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
        
        main_menu.update(events)
        main_menu.draw(WINDOW)

        pygame.display.update()

if __name__ == "__main__":
    main()
                
