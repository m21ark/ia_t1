import pygame_menu


class OptionsMenu:

    def __init__(self, window):
        self.__options_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Options Menu',
            theme=pygame_menu.themes.THEME_DARK
        )
        self.__options_menu.add.button('Something', self.__back)

    @property
    def options_menu(self):
        return self.__options_menu

    def __back(self):
        self.__options_menu.disable()
