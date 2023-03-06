from view.view_const import *
from model.sample_mazes import *
import pygame
import pygame_menu
from algorithms.algorithms import BlockState

class GameView:
    def __init__(self, surface, model):
        self.surface = surface
        self.model = model

    def get_color(array, x, y, show=False):
        node = array[x + MATRIX_COL * y]
        if node == EMPTY_NODE:
            return GREY if show else BG_COLOR
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
                
    @staticmethod
    def draw_showoff(maze):
        for x in range(MATRIX_COL):
            for y in range(MATRIX_ROW):
                pygame.draw.rect(WINDOW, GameView.get_color(maze, x, y), ( x * BLOCK_SIZE/3 + WINDOW_SIZE[0]/2 - MATRIX_COL/2 * BLOCK_SIZE/3,
                                                                           y * BLOCK_SIZE/3 + WINDOW_SIZE[1]/18 
                                                                          , BLOCK_SIZE/3, BLOCK_SIZE/3))

    def draw_block(self):
        if self.model.get_block.isStanding():
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x * BLOCK_SIZE,
                             self.model.get_block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x * BLOCK_SIZE,
                             self.model.get_block.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, BLUE, (self.model.get_block.x2 * BLOCK_SIZE,
                             self.model.get_block.y2 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            
    def draw_node(self, node : BlockState):
        if node.isStanding():
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x * BLOCK_SIZE,
                             node.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x * BLOCK_SIZE,
                             node.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x2 * BLOCK_SIZE,
                             node.y2 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            
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
