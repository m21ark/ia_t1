from view.game_view import *

class GameController:
    def __init__(self, game_model, surface):
        self.game_model = game_model
        self.surface = surface
        self.game_view = GameView(surface, game_model)

    def start(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    quit()
            self.game_view.draw_maze()
            self.game_view.draw_block()
            pygame.display.update()
            
            keys = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]

            for key in keys:
                if pygame.key.get_pressed()[key]:
                    print(key)
                    #self.game_model.get_block.move(key)
                    #self.game_view.draw_maze()
                    pygame.display.update()


    #def update(self):
        #self.game_model.update()
        #self.game_view.update()

    #def end(self):
    #    self.game_view.end()