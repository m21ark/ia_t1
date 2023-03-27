import pygame
from view.view_const import *
from model.sample_mazes import *
from menu.main_menu import MainMenu
from view.game_view import GameView
from model.game_model import *
from algorithms.genetic_algorithm import *
import sys

def main():

    pygame.init()

    obj_main_menu = MainMenu(WINDOW_SIZE)
    main_menu = obj_main_menu.main_menu

    running = True
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                pygame.quit()
                running = False

        main_menu.update(events)
        main_menu.draw(WINDOW)

        if obj_main_menu._play_ground.is_selected():
            GameView.draw_showoff(GameModel.sel_maze)

        pygame.display.update()


if __name__ == "__main__":
    if '--statistics' in sys.argv:
        from algorithms.statistics import *
        functions = [depth, breadth, greedy, a_star, greedy_chebyshev, a_star_chebyshev, greedy_euclidean, a_star_euclidean, genetic, dfs_random]
        mazes = [x[1] for x in game_maps]
        solver = MazeSolver(functions, mazes)
        solver.execute_functions()
    else:
        main()
        