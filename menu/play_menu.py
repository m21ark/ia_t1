import pygame_menu
from controller.game_controller import *
from model.game_model import *
from model.sample_mazes import *

class PlayGroundMenu:

    def __init__(self, window):
        self.__playground_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Playground Menu',
            theme=pygame_menu.themes.THEME_DARK,
            mouse_motion_selection=True,
            mouse_visible=True,
            mouse_enabled=True
        )
        self.__selections()
        self.maze = 0
        self.algorithm = 0

    @property
    def playground_menu(self):
        return self.__playground_menu
    
    def __on_maze_change(self, value, extra):
        self.maze = value

    def __on_algorithm_change(self, value, extra):
        self.algorithm = value


    def __selections(self):
        self.maze_sel = self.__playground_menu.add.selector(
            'Maze',
            [('Maze 1', 1), ('Maze 2', 2), ('Maze 3', 3)], # ilustrative
            onchange=self.__on_maze_change,
        )

        self.__algorithm_sel = self.__playground_menu.add.dropselect(
            'Algorithm',
            [('Algorithm 1', 1), ('Algorithm 2', 2), ('Algorithm 3', 3)], # ilustrative
            onchange=self.__on_algorithm_change,
        )

        self.__playground_menu.add.button('Play', GameController(GameModel(game_map), WINDOW).start)
    