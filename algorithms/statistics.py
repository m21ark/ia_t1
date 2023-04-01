import pandas as pd
import matplotlib.pyplot as plt
import time
import tracemalloc
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
        time_results = []
        memory_results = []
        for function in self.functions:
            time_func_results = []
            memory_func_results = []
            for maze in self.mazes:
                tracemalloc.start()  # start tracing memory allocations
                start_time = time.time()
                function(maze)
                end_time = time.time()
                exec_time = end_time - start_time
                current, peak = tracemalloc.get_traced_memory()  # get memory usage
                tracemalloc.stop()  # stop tracing memory allocations
                time_func_results.append(exec_time)
                memory_func_results.append(peak)
            time_results.append(time_func_results)
            memory_results.append(memory_func_results)

        time_df = pd.DataFrame(time_results).T
        time_df.columns = [function.__name__ for function in self.functions]
        time_df.index = ['Maze {}'.format(i+1) for i in range(len(self.mazes))]

        memory_df = pd.DataFrame(memory_results).T
        memory_df.columns = [function.__name__ for function in self.functions]
        memory_df.index = ['Maze {}'.format(i+1) for i in range(len(self.mazes))]

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter('results.xlsx', engine='xlsxwriter')

        # Write the time and memory dataframes to separate sheets.
        time_df.to_excel(writer, sheet_name='Execution Time', index=True)
        memory_df.to_excel(writer, sheet_name='Memory Usage', index=True)

        # Access the XlsxWriter workbook and worksheet objects from the dataframes.
        workbook  = writer.book
        time_sheet = writer.sheets['Execution Time']
        memory_sheet = writer.sheets['Memory Usage']

        # Create a chart object for execution time.
        time_chart = workbook.add_chart({'type': 'line'})
        for col_num in range(1, len(self.functions)+1):
            time_chart.add_series({
                'name':       ['Execution Time', 0, col_num],
                'categories': ['Execution Time', 1, 0, len(self.mazes), 0],
                'values':     ['Execution Time', 1, col_num, len(self.mazes), col_num],
            })

        # Create a chart object for memory usage.
        memory_chart = workbook.add_chart({'type': 'line'})
        for col_num in range(1, len(self.functions)+1):
            memory_chart.add_series({
                'name':       ['Memory Usage', 0, col_num],
                'categories': ['Memory Usage', 1, 0, len(self.mazes), 0],
                'values':     ['Memory Usage', 1, col_num, len(self.mazes), col_num],
            })

        # Insert the charts into the worksheets.
        time_sheet.insert_chart('D2', time_chart)
        memory_sheet.insert_chart('D2', memory_chart)

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
