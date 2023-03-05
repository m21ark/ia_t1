from view.view_const import *
from model.sample_mazes import *
import pygame
import pygame_menu


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
                pygame.draw.rect(self.surface, GameView.get_color(
                    self.model.get_maze, x, y), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def draw_block(self):
        if self.model.get_block.isStanding():
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x * BLOCK_SIZE,
                             self.model.get_block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x * BLOCK_SIZE,
                             self.model.get_block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x2 * BLOCK_SIZE,
                             self.model.get_block.y2 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def game_over(self, new_block):
        menu = pygame_menu.Menu(
            height=WINDOW_SIZE[1],
            width=WINDOW_SIZE[0],
            title='Game Over',
            theme=pygame_menu.themes.THEME_DARK
        )

        run = True

        def print_r():
            print(run)

        b = menu.add.button('GAME OVER', print_r)
        if new_block != None and new_block.checkIfGoal():
            a = menu.add.button('You Win!!', print_r)
        else:
            # adicionar o fallen se interesar
            a = menu.add.button('You Lost!!', print_r)

        while run:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    run = False

            if a.is_selected():
                run = False

            menu.update(events)
            menu.draw(self.surface)
            pygame.display.update()
