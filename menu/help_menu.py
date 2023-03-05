import pygame_menu


class HelpMenu:

    def __init__(self, window):
        self.__help_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Help Menu',
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__help_menu.add.button('Something', self.__back)

    @property
    def help_menu(self):
        return self.__help_menu

    def __back(self):
        print('Back')
