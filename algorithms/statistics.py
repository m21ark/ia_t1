import pandas as pd
import matplotlib.pyplot as plt
import time
from model.sample_mazes import *
from algorithms.block_state import BlockState
from algorithms.algorithms import *
from algorithms.genetic_algorithm import *
from model.game_model import GameModel

class MazeSolver:
    def __init__(self, functions, mazes):
        self.functions = functions
        self.mazes = mazes

    def execute_functions(self):
        results = []
        for function in self.functions:
            func_results = []
            for maze in self.mazes:
                start_time = time.time()
                function(maze)
                end_time = time.time()
                exec_time = end_time - start_time
                func_results.append(exec_time)
            results.append(func_results)
        df = pd.DataFrame(results).T
        df.columns = [function.__name__ for function in self.functions]
        df.index = ['Maze {}'.format(i+1) for i in range(len(self.mazes))]

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('results.xlsx', engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Sheet1', index=True)

        # Access the XlsxWriter workbook and worksheet objects from the dataframe.
        workbook  = writer.book
        worksheet = writer.sheets['Sheet1']

        # Create a chart object.
        chart = workbook.add_chart({'type': 'line'})

        # Configure the series of the chart from the dataframe data.
        for col_num in range(1, len(self.functions)+1):
            chart.add_series({
                'name':       ['Sheet1', 0, col_num],
                'categories': ['Sheet1', 1, 0, len(self.mazes), 0],
                'values':     ['Sheet1', 1, col_num, len(self.mazes), col_num],
            })

        # Insert the chart into the worksheet.
        worksheet.insert_chart('D2', chart)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

# Example usage
def depth(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return depth_first_search(blockSt, goal_block_state, child_block_states)

def breadth(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return breadth_first_search(blockSt, goal_block_state, child_block_states)

def iterative(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return iterative_deepening_search(blockSt, goal_block_state, child_block_states, 200)

def greedy(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return greedy_search(blockSt, goal_block_state, child_block_states, manhattan_distance_heuristic)

def a_star(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return a_star_search(blockSt, goal_block_state, child_block_states, manhattan_distance_heuristic)

def a_w_m_star(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return a_star_weighted_search(blockSt, goal_block_state, child_block_states, manhattan_distance_heuristic)


def greedy_chebyshev(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return greedy_search(blockSt, goal_block_state, child_block_states, chebyshev_distance_heuristic)

def a_star_chebyshev(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return a_star_search(blockSt, goal_block_state, child_block_states, chebyshev_distance_heuristic)

def a_star_w_chebyshev(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return a_star_weighted_search(blockSt, goal_block_state, child_block_states, chebyshev_distance_heuristic)

def greedy_euclidean(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return greedy_search(blockSt, goal_block_state, child_block_states, euclidean_distance_heuristic)

def a_star_euclidean(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return a_star_search(blockSt, goal_block_state, child_block_states, euclidean_distance_heuristic)

def a_star_w_euclidean(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return a_star_weighted_search(blockSt, goal_block_state, child_block_states, euclidean_distance_heuristic)

def genetic(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return genetic_algorithm(blockSt,1000, 50, crossover, mutate, False)

def dfs_random(maze):
    x, y = GameModel.find_start_end_nodes(maze)
    blockSt = BlockState(x, y, x, y, maze)
    return random_dfs(blockSt, goal_block_state, child_block_states)
