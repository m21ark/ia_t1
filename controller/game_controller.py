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
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()
            self.game_view.draw_maze()
            self.game_view.draw_block()
            pygame.display.update()
            
            keys = [(pygame.K_LEFT, moveLeft), (pygame.K_RIGHT, moveRight),
                     (pygame.K_UP, moveUp), (pygame.K_DOWN, moveDown)]

            for key, func in keys:
                if pygame.key.get_pressed()[key]:
                    
                    new_block = func(self.game_model.get_block)
                    if (new_block):
                        self.game_model.set_block(new_block)
                        print(self.game_model.get_block.x, self.game_model.get_block.y)
                    else:
                        running = False
                        # game is lost
                        

                    #self.game_model.get_block.move(key)
                    #self.game_view.draw_maze()
                    pygame.display.update()
            
            clock.tick(10)


    #def update(self):
        #self.game_model.update()
        #self.game_view.update()

    #def end(self):
    #    self.game_view.end()