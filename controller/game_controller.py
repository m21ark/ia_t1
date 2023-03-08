from view.game_view import *
from model.game_model import *
from algorithms.algorithms import *
import pygame.mixer
from datetime import datetime


class GameController:
    def __init__(self, game_model: GameModel, surface):
        self.game_model = game_model
        self.surface = surface
        self.game_view = GameView(surface, game_model)

    def start(self, algo):

        def real_start():

            pygame.mixer.init()
            bg_music = pygame.mixer.Sound('assets/tense_music.wav')
            bg_music.play() # loops=-1
            
            running = True
            clock = pygame.time.Clock()
            already_moved = False

            keys = [(pygame.K_LEFT, moveLeft), (pygame.K_RIGHT, moveRight),
                    (pygame.K_UP, moveUp), (pygame.K_DOWN, moveDown)]

            start_time = datetime.now()
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
                        quit()
                    if event.type == pygame.KEYUP:
                        already_moved = False

                if (pygame.key.get_pressed()[pygame.K_q]):
                    running = False

                self.game_view.draw_maze()
                self.game_view.draw_block()

                if (pygame.key.get_pressed()[pygame.K_h]):
                    sol_node = hint_call(algo[2], self.game_model.block)()
                    move = sol_node.get_path()[1]
                    self.game_view.draw_node(move)

                time_elapsed = datetime.now() - start_time

                self.game_view.draw_time(time_elapsed)

                pygame.display.update()

                if time_elapsed.seconds >= 65:
                    running = False
                    self.game_view.game_over(None)

                for key, func in keys:
                    if pygame.key.get_pressed()[key] and not already_moved:
                        already_moved = True

                        new_block = func(self.game_model.get_block)
                        if (new_block):
                            self.game_model.set_block(new_block)                  
                        else:
                            running = False  # add menu for game finish and pass the  new_block to know the end state
                            bg_music.stop()
                            self.game_view.game_over(new_block)

                        if new_block != None and new_block.checkIfGoal():
                            running = False  # add menu for game finish and pass the new_block
                            bg_music.stop()
                            self.game_view.game_over(new_block)

                        pygame.display.update()

                clock.tick(30)

            self.game_model.reset_block()
            bg_music.stop()

        return real_start

    def ia_solver_start(self, algo):

        def ia_solver_run():

            sol_node = algo[1]()
            path = sol_node.get_path()

            print("Running sol", len(path))
            already_moved = []

            for node in path:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()

                if pygame.key.get_pressed()[pygame.K_q]:
                    break

                self.game_view.draw_maze()
                self.game_model.set_block(node)

                for n in already_moved:
                    self.game_view.draw_node(n)

                self.game_view.draw_block()

                already_moved.append(node)
                pygame.display.update()

                pygame.time.delay(50)

        return ia_solver_run
