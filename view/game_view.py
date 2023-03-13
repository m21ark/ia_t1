from view.view_const import *
from model.sample_mazes import *
import pygame
import pygame_menu
from algorithms.algorithms import BlockState


class GameView:
    def __init__(self, surface, model):
        self.surface = surface
        self.model = model

    def draw_time(self, time):
        font = pygame.font.SysFont('Arial Bold', 30)
        time_elapsed_str = "Time: " + \
            str(65-time.seconds) + " s"
        time_elapsed_text = font.render(
            time_elapsed_str, False, (255, 255, 255))
        time_elapsed_rect = time_elapsed_text.get_rect()
        time_elapsed_rect.topright = (screen_width - 10, 8)
        self.surface.blit(time_elapsed_text, time_elapsed_rect)

    def get_color(array, x, y, show=False):
        node = array[x + MATRIX_COL * y]
        if node == EMPTY_NODE:
            return GREY if show else BG_COLOR
        elif node == START_NODE:
            return WHITE
        elif node == END_NODE:
            return RED
        elif node == PATH_NODE:
            return GREEN
        elif node == PLAYER_NODE_A:
            return BLUE
        elif node == PLAYER_NODE_B:
            return BLUE
        elif node == BLOCK_NODE:
            return YELLOW
        elif node == KILLER_NODE:
            return PURPLE
        else:
            return BLACK

    def draw_maze(self):
        
        for row in range(MATRIX_ROW):
            for col in range(MATRIX_COL):
                # Get the tile position for the current cell
                tile_position = tile_positions[self.model.get_maze[row + col * MATRIX_COL]]
                # Extract the tile from the tileset image
                tile = tileset_image.subsurface(pygame.Rect(
                    tile_position[0] * TILE_SIZE, tile_position[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))
                # Draw the scaled tile on the screen
                self.surface.blit(
                    tile, (row * TILE_SIZE, col * TILE_SIZE))

    def draw_nr_moves(self):
        font = pygame.font.SysFont('Arial Bold', 30)
        nr_moves_str = "Moves: " + str(self.model.get_nr_moves)
        nr_moves_text = font.render(
            nr_moves_str, False, (255, 255, 255))
        nr_moves_rect = nr_moves_text.get_rect()
        nr_moves_rect.topright = (screen_width - 10, 40)
        self.surface.blit(nr_moves_text, nr_moves_rect)

    @staticmethod
    def draw_showoff(maze):
        for x in range(MATRIX_COL):
            for y in range(MATRIX_ROW):
                pygame.draw.rect(WINDOW, GameView.get_color(maze, x, y), (x * BLOCK_SIZE/3 + WINDOW_SIZE[0]/2 - MATRIX_COL/2 * BLOCK_SIZE/3,
                                                                          y * BLOCK_SIZE/3 + WINDOW_SIZE[1]/18, BLOCK_SIZE/3, BLOCK_SIZE/3))

    def draw_block(self):
        tile_position = tile_positions[BLOCK_NODE-1]

        # Extract the tile from the tileset image
        tile = tileset_image.subsurface(pygame.Rect(
            tile_position[0] * TILE_SIZE, tile_position[1] * TILE_SIZE, TILE_SIZE, TILE_SIZE))

        if self.model.get_block.isStanding():
            self.surface.blit(tile, (self.model.get_block.x *
                              TILE_SIZE, self.model.get_block.y * TILE_SIZE))
        else:
            self.surface.blit(tile, (self.model.get_block.x *
                              TILE_SIZE, self.model.get_block.y * TILE_SIZE))
            self.surface.blit(tile, (self.model.get_block.x2 *
                              TILE_SIZE, self.model.get_block.y2 * TILE_SIZE))

    def draw_node(self, node: BlockState):
        if node.isStanding():
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x * BLOCK_SIZE,
                             node.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x * BLOCK_SIZE,
                             node.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x2 * BLOCK_SIZE,
                             node.y2 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def game_over(self, new_block):
        menu = pygame_menu.Menu(
            height=WINDOW_SIZE[1],
            width=WINDOW_SIZE[0],
            title='Game Over',
            theme=pygame_menu.themes.THEME_DARK
        )

        run = True

        def print_r():
            print(run)

        pygame.mixer.init()

        b = menu.add.button('GAME OVER', print_r)
        if new_block != None and new_block.checkIfGoal():
            wining_sound = pygame.mixer.Sound('assets/winning_sound.wav')
            wining_sound.play()
            a = menu.add.label('You Win!!')
        else:
            losing_sound = pygame.mixer.Sound('assets/losing_sound.wav')
            losing_sound.play()
            a = menu.add.label('You Lost!!')

        while run:

            events = pygame.event.get()
            for event in events:
                if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
                    run = False

            if a.is_selected():
                run = False

            menu.update(events)
            menu.draw(self.surface)
            pygame.display.update()
