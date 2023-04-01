from view.view_const import *
from model.sample_mazes import *
import pygame
import pygame_menu
from algorithms.algorithms import BlockState


class GameView:
    """
    Represents the view of the game.
    It is responsible for the visual representation of the game.
    
    Attributes:
        surface (WINDOW): The surface of the game, in this case pygame surface windows.
        model (GameModel): The model of the game. Responsible for the game logic.

    """
    def __init__(self, surface, model):
        """
        Parameters
        ----------
        surface : WINDOW variable
            The surface of the game, in this case pygame surface windows.
        model : GameModel
            The model of the game. Responsible for the game logic.
        """
        self.surface = surface
        self.model = model

    def draw_time(self, time):
        """
        Draws the time elapsed on the screen. 
        The time is calculated by subtracting the current time from the start time.
        When the time is up, the game ends.
        """
        font = pygame.font.SysFont('Arial Bold', 30)
        time_elapsed_str = "Time: " + \
            str(65-time.seconds) + " s"
        time_elapsed_text = font.render(
            time_elapsed_str, False, (255, 255, 255))
        time_elapsed_rect = time_elapsed_text.get_rect()
        time_elapsed_rect.topright = (screen_width - 10, 8)
        self.surface.blit(time_elapsed_text, time_elapsed_rect)

    def get_color(array, x, y, show=False):
        """
        Returns the color of the node.
        If the node is empty, it returns the background color.
        If the node is the start node, it returns white.
        If the node is the end node, it returns red.
        If the node is the path node, it returns green.
        If the node is the player node, it returns blue.
        If the node is the block node, it returns yellow.
        If the node is the killer node, it returns purple.
        If the node is the wall node, it returns black.
        """
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
        """
        Draws the maze on the screen.
        """
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
        """
        Draws the number of moves on the screen.
        """
        self.draw_text("Moves: " + str(self.model.get_nr_moves), 30, (255, 255, 255), 10, 40)

    def draw_text(self, text, fontSize, color, x, y):
        """
        Draws the text on the screen.

        Parameters
        ----------
        text : str
            The text to be drawn.
        fontSize : int
            The size of the font.
        color : tuple
            The color of the text.
        x : int
            The x coordinate of the text.
        y : int
            The y coordinate of the text.
        """
        font = pygame.font.SysFont('Arial Bold', fontSize)
        nr_moves_text = font.render(text, False, color)
        nr_moves_rect = nr_moves_text.get_rect()
        nr_moves_rect.topright = (screen_width - x, y)
        self.surface.blit(nr_moves_text, nr_moves_rect)

    @staticmethod
    def draw_showoff(maze):
        """
        Draws the maze currently selected on the screen menu.
        This is a preview of the maze.

        Parameters
        ----------
        maze : list
            The maze to be drawn.
        """
        for x in range(MATRIX_COL):
            for y in range(MATRIX_ROW):
                pygame.draw.rect(WINDOW, GameView.get_color(maze, x, y), (x * BLOCK_SIZE/3 + WINDOW_SIZE[0]/2 - MATRIX_COL/2 * BLOCK_SIZE/3,
                                                                          y * BLOCK_SIZE/3 + WINDOW_SIZE[1]/18, BLOCK_SIZE/3, BLOCK_SIZE/3))

    def draw_block(self):
        """
        Draws the block on the screen.
        With the block texture.
        """
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
        """
        Draws the Node on the screen.
        Used to show the path of the ia agent.
        """
        if node.isStanding():
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x * BLOCK_SIZE,
                             node.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
        else:
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x * BLOCK_SIZE,
                             node.y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
            pygame.draw.rect(self.surface, LIGHT_BLUE, (node.x2 * BLOCK_SIZE,
                             node.y2 * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))

    def game_over(self, new_block):
        """
        Draws the game over screen.

        Parameters
        ----------
        new_block : BlockState
            The block state at the end of the game.
        """
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
