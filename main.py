import pygame
import datetime
from math import sqrt
from collections import deque
from view.view_const import *
from model.sample_mazes import *
from algorithms.block_state import BlockState
from menu.main_menu import MainMenu

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
