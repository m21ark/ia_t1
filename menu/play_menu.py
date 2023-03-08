import pygame_menu
from controller.game_controller import *
from model.game_model import *
from model.sample_mazes import *


class PlayGroundMenu:

    # algorithm = 0 ############################### NOTA::::::AQUI EM BAIXO TEM O GAME_MAP mas o mapa pode mudar, secalhar passar pelo x ?
    def __init__(self, window):
        self.__playground_menu = pygame_menu.Menu(
            height=window[1],
            width=window[0],
            title='Play Menu',
            theme=pygame_menu.themes.THEME_DARK,
            mouse_motion_selection=True,
            mouse_visible=True,
            mouse_enabled=True
        )

        self.maze = 0
        self.algorithm = 0

        x, y = GameModel.find_start_end_nodes(game_maps[self.maze][1])
        self.initial_pos = BlockState(x, y, x, y, game_maps[self.maze][1])

        self.algs = [('DFS', lambda: depth_first_search(self.initial_pos, goal_block_state, child_block_states), depth_first_search),
                     ('BFS', lambda: breadth_first_search(self.initial_pos,
                      goal_block_state, child_block_states), breadth_first_search),
                     ('Iterative deepening', lambda: iterative_deepening_search(
                         self.initial_pos, goal_block_state, child_block_states, 200), iterative_deepening_search),
                     ('Greedy Search', lambda: greedy_search(self.initial_pos,
                      goal_block_state, child_block_states, self.initial_pos.heuristic), greedy_search),
                     ('A* Search', lambda:  a_star_search(self.initial_pos, goal_block_state, child_block_states, self.initial_pos.heuristic), a_star_search)]  # ilustrative

        self.__selections()

    @property
    def playground_menu(self):
        return self.__playground_menu

    def __on_maze_change(self, value, extra):
        self.maze = value[1]

        GameModel.sel_maze = game_maps[self.maze][1]

        x, y = GameModel.find_start_end_nodes(game_maps[self.maze][1])
        self.initial_pos = BlockState(x, y, x, y, game_maps[self.maze][1])

        self.play.update_callback(GameController(
            GameModel(game_maps[self.maze][1]), WINDOW).start(self.algs[self.algorithm]))
        self.ai.update_callback(GameController(GameModel(
            game_maps[self.maze][1]), WINDOW).ia_solver_start(self.algs[self.algorithm]))

    def __on_algorithm_change(self, value, extra, extra_):
        self.algorithm = value[1]
        self.play.update_callback(GameController(
            GameModel(game_maps[self.maze][1]), WINDOW).start(self.algs[self.algorithm]))
        self.ai.update_callback(GameController(GameModel(
            game_maps[self.maze][1]), WINDOW).ia_solver_start(self.algs[self.algorithm]))

    def __selections(self):
        self.maze_sel = self.__playground_menu.add.dropselect(
            'Maze',
            game_maps,  # ilustrative
            onchange=self.__on_maze_change,
            default=self.maze,
            selection_box_width=300,
        )

        self.__algorithm_sel = self.__playground_menu.add.dropselect(
            'Algorithm',
            self.algs,
            onchange=self.__on_algorithm_change,
            default=self.algorithm,
            selection_box_width=350,
        )

        self.ai = self.__playground_menu.add.button('AI-Solver', GameController(GameModel(
            game_maps[self.maze][1]), WINDOW).ia_solver_start(self.algs[self.algorithm]))  # ilustrative ... change map
        self.play = self.__playground_menu.add.button('Play', GameController(
            GameModel(game_maps[self.maze][1]), WINDOW).start(self.algs[self.algorithm]))
