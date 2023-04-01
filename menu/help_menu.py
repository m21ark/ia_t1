import pygame_menu


class HelpMenu:
    """Help Menu class"""

    def __init__(self, window):
        """
        New Pygame menu with the specified window dimensions, title, and theme
        
        Parameters:
        window: tuple of integers representing the window dimensions

        """

        self.__help_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Help Menu',
            theme=pygame_menu.themes.THEME_DARK
            
        )

        """Add labels to the menu to display game instructions"""
        self.__help_menu.add.label('Game Rules:', font_size=33)
        self.__help_menu.add.label('')
        self.__help_menu.add.label('1. Your goal is to place the block vertically in the exit', wordwrap=True, font_size=25)
        self.__help_menu.add.label('portal before the timer ends', wordwrap=True, font_size=25)
        self.__help_menu.add.label('\t 2. Use the arrow keys to move the block in the selected direction', wordwrap=True, font_size=25)
        self.__help_menu.add.label('3. The block has to be placed on the solid ground or it will fall', wordwrap=True, font_size=25)
        self.__help_menu.add.label('and you lose', wordwrap=True, font_size=25, )
        self.__help_menu.add.label('\t 4. Watch out for obstacles', wordwrap=True, font_size=25)
        self.__help_menu.add.label('\t 5. Use \'H\' to have hints. And \'Q\' follow by a key to leave.', wordwrap=True, font_size=25)
        self.__help_menu.add.label('')
        self.__help_menu.add.label('Good luck and have fun!', font_size=30)
        

    @property
    def help_menu(self):
        """getter for the pygame menu object"""

        return self.__help_menu


    def __back(self):
        """method for returning to the previous menu"""
        
        print('Back')
        
