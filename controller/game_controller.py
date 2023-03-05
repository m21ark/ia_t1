from view.game_view import *
from model.game_model import *
from algorithms.algorithms import *

class GameController:
    def __init__(self, game_model : GameModel, surface):
        self.game_model = game_model
        self.surface = surface
        self.game_view = GameView(surface, game_model)

    def start(self):
        running = True
        clock = pygame.time.Clock()
        already_moved = False

        keys = [(pygame.K_LEFT, moveLeft), (pygame.K_RIGHT, moveRight),
            (pygame.K_UP, moveUp), (pygame.K_DOWN, moveDown)]

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()
                if event.type == pygame.KEYUP:
                    already_moved = False

            self.game_view.draw_maze()
            self.game_view.draw_block()
            pygame.display.update()
            


            for key, func in keys:
                if pygame.key.get_pressed()[key] and not already_moved:
                    already_moved = True
 
                    new_block = func(self.game_model.get_block)
                    if (new_block):
                        self.game_model.set_block(new_block)
                    else:
                        running = False # add menu for game finish and pass the  new_block to know the end state
                        self.game_view.game_over(new_block)

                    if new_block != None and new_block.checkIfGoal():
                        running = False # add menu for game finish and pass the new_block
                        self.game_view.game_over(new_block)

                    pygame.display.update()
            
            clock.tick(30)

    def ia_solver_start(self, algo):
        
        def ia_solver_run():
            
            print(algo[0])
            sol_node = algo[1]()
            path = sol_node.get_path()

            for node in path:
                self.game_view.draw_maze()
                self.game_model.set_block(node)
                self.game_view.draw_block()
                pygame.display.update()
            
        return ia_solver_run
            

    