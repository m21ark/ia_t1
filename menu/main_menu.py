import pygame_menu
from menu.help_menu import HelpMenu
from menu.options_menu import OptionsMenu


class MainMenu:

    def __init__(self, window):
        self.__main_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Main Menu',
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__main_menu.add.button('Play', self.__play)
        self.__main_menu.add.button('Options', OptionsMenu(window).options_menu)
        self.__main_menu.add.button('Help', HelpMenu(window).help_menu)
        self.__main_menu.add.button('Quit', pygame_menu.events.EXIT)

    @property
    def main_menu(self):
        return self.__main_menu
    
    def __play(self):
        print('Play')

            