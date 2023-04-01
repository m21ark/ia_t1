import pygame_menu
from controller.game_controller import *
from model.game_model import *
from model.sample_mazes import *
from algorithms.genetic_algorithm import *


paths_n = 0
def random_end(self):
    """function to check if the random DFS has generated 200 paths"""

    global paths_n
    paths_n += 1
    return paths_n == 200

def generate_random_maze():
    """function to generate a random maze using random DFS algorithm"""

    global paths_n
    paths_n = 0
    x, y = GameModel.find_start_end_nodes(maze_1)
    blockSt = BlockState(x, y, x, y, maze_1)
    r = random_dfs(blockSt, random_end, child_block_states)
    maze = []
    for i in range(30*30):
        maze.append(0)
    pat = r.get_path()
    for i in pat:
        maze[i.x + i.y * 30] = 3
        maze[i.x2 + i.y2 * 30] = 3

    maze[x + y * 30] = 1
    if pat[-1].isStanding():
        maze[pat[-1].x + pat[-1].y * 30] = 2
    else:
        maze[pat[-2].x + pat[-2].y * 30] = 2
    return maze

class PlayGroundMenu:

    def __init__(self, window):
        """
        Create a Pygame menu object

        Parameters:
        window: tuple of integers representing the window dimensions
        """

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
                     ('Greedy (manhattan)', lambda: greedy_search(self.initial_pos,
                      goal_block_state, child_block_states, manhattan_distance_heuristic), greedy_search),
                     ('A* (manhattan)', lambda:  a_star_search(self.initial_pos, goal_block_state,
                      child_block_states, manhattan_distance_heuristic), a_star_search),
                     ('A* W=1.5 (manhattan)', lambda: a_star_weighted_search(self.initial_pos, goal_block_state,
                      child_block_states, manhattan_distance_heuristic), a_star_weighted_search),
                     ('Greedy (chebyshev)', lambda: greedy_search(self.initial_pos,
                      goal_block_state, child_block_states, chebyshev_distance_heuristic), greedy_search),
                     ('A* (chebyshev)', lambda:  a_star_search(self.initial_pos, goal_block_state,
                      child_block_states, chebyshev_distance_heuristic), a_star_search),
                     ('A* W=1.5 (chebyshev)', lambda:  a_star_weighted_search(self.initial_pos, goal_block_state,
                      child_block_states, chebyshev_distance_heuristic), a_star_weighted_search),
                     ('Greedy (euclidean)', lambda: greedy_search(self.initial_pos,
                      goal_block_state, child_block_states, euclidean_distance_heuristic), greedy_search),
                     ('A* (euclidean)', lambda:  a_star_search(self.initial_pos, goal_block_state,
                      child_block_states, euclidean_distance_heuristic), a_star_search),
                     ('A* W=1.5 (euclidean)', lambda:  a_star_weighted_search(self.initial_pos, goal_block_state,
                      child_block_states, euclidean_distance_heuristic), a_star_weighted_search),
                     ('Genetic', lambda: genetic_algorithm(self.initial_pos,
                      1000, 50, crossover, mutate, False), genetic_algorithm),
                     ('Random DFS', lambda: random_dfs(self.initial_pos, goal_block_state, child_block_states), random_dfs)]

        self.__selections()

    @property
    def playground_menu(self):
        return self.__playground_menu



    def __on_maze_change(self, value, extra):
        """
        function to change the maze when the user selects a different one
        
        Parameters:
        value: tuple of strings representing the maze name and the maze
        extra: extra parameter
        """
        self.maze = value[1]


        if game_maps[self.maze][0] == 'Random Maze':
            maze = generate_random_maze()
            GameModel.sel_maze = maze
            game_maps.pop()
            game_maps.append(('Random Maze',maze))
        else:
            GameModel.sel_maze = game_maps[self.maze][1]

        x, y = GameModel.find_start_end_nodes(game_maps[self.maze][1])
        self.initial_pos = BlockState(x, y, x, y, game_maps[self.maze][1])

        self.play.update_callback(GameController(
            GameModel(game_maps[self.maze][1]), WINDOW).start(self.algs[self.algorithm]))
        self.ai.update_callback(GameController(GameModel(
            game_maps[self.maze][1]), WINDOW).ia_solver_start(self.algs[self.algorithm]))

    def __on_algorithm_change(self, value, extra, extra_):
        """ Update the algorithm selection
        
        Parameters:
        value: tuple of the selected algorithm
        extra: extra parameter
        extra_: extra parameter
        """

        self.algorithm = value[1]
        self.play.update_callback(GameController(
            GameModel(game_maps[self.maze][1]), WINDOW).start(self.algs[self.algorithm]))
        self.ai.update_callback(GameController(GameModel(
            game_maps[self.maze][1]), WINDOW).ia_solver_start(self.algs[self.algorithm]))

    def __selections(self):
        """ Create the menu selections"""

        self.maze_sel = self.__playground_menu.add.selector(
            'Maze',
            game_maps,
            onchange=self.__on_maze_change,
            default=self.maze,
        )

        self.__algorithm_sel = self.__playground_menu.add.dropselect(
            'Algorithm',
            self.algs,
            onchange=self.__on_algorithm_change,
            default=self.algorithm,
            selection_box_width=350,
        )

        self.ai = self.__playground_menu.add.button('AI-Solver', GameController(GameModel(
            game_maps[self.maze][1]), WINDOW).ia_solver_start(self.algs[self.algorithm])) 
        self.play = self.__playground_menu.add.button('Play', GameController(
            GameModel(game_maps[self.maze][1]), WINDOW).start(self.algs[self.algorithm]))
