import pygame_menu
from menu.help_menu import HelpMenu
from menu.options_menu import OptionsMenu
from menu.play_menu import PlayGroundMenu
from model.sample_mazes import *


class MainMenu:

    def __init__(self, window):
        self.__main_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Main Menu',
            theme=pygame_menu.themes.THEME_DARK
        )
        self._play_ground = self.__main_menu.add.button(
            'Play', PlayGroundMenu(window).playground_menu)
        self.__main_menu.add.button(
            'Options', OptionsMenu(window).options_menu)
        self.__main_menu.add.button('Help', HelpMenu(window).help_menu)
        self.__main_menu.add.button('Quit', pygame_menu.events.EXIT)

    @property
    def main_menu(self):
        return self.__main_menu

    @property
    def play_ground(self):
        return self._play_ground
