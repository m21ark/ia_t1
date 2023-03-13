import numpy as np
from model.sample_mazes import * 
from algorithms.algorithms import *
import random

def random_dfs(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)   # create the root node in the search tree
    stack = [root]   # initialize the queue to store the nodes

    visited = set()
    while stack:
        node = stack.pop()   # get first element in the queue
        
        if node.state in visited:
            continue

        visited.add(node.state)

        if goal_state_func(node.state):   # check goal state
            return node

        # random permutation
        l = [TreeNode(state, node)
                     for state in operators_func(node.state)]
        random.shuffle(l)

        stack.extend(l)
    
    return None

def crossover(solution_1, solution_2):
    
    intersection = set(solution_1).intersection(solution_2)

    inter_random_element = random.sample(intersection, 1)[0]
    child_1 = []
    child_2 = []
    cut_point_2 = solution_2.index(inter_random_element)
    cut_point_1 = solution_1.index(inter_random_element)

    child_1.extend(solution_1[:cut_point_1])
    child_1.extend(solution_2[cut_point_2:])
    
    child_2.extend(solution_2[:cut_point_2])
    child_2.extend(solution_1[cut_point_1:])

    return child_1, child_2

def evaluate_solution(solution):
    
    if goal_block_state(solution[-1]):
        return -len(solution)

    return -(len(solution) + 1000)
    

def generate_random_solution():
    st = BlockState(3,3,3,3, maze_1)
    s = random_dfs(st, goal_block_state, child_block_states)
    solution = s.get_path()
    return solution


def generate_population(population_size):
    solutions = []
    for i in range(population_size):
        solutions.append(generate_random_solution())
    return solutions

def print_population(population):
    for i in range(len(population)):
        print(f"Solution {i}: {population[i]}, {evaluate_solution(population[i])}")
    
def tournament_select(population, tournament_size):    
    
    tournament = random.sample(population, tournament_size)
    best_solution = max(tournament, key=evaluate_solution)

    
    return best_solution

def get_greatest_fit(population):
    best_solution = population[0]
    best_score = evaluate_solution(population[0])
    for i in range(1, len(population)):
        score = evaluate_solution(population[i])
        if score > best_score:
            best_score = score
            best_solution = population[i]
    return best_solution, best_score

def replace_least_fittest(population, offspring):
    least_fittest_index = 0
    least_fittest_value = evaluate_solution(population[0])
    for i in range(1, len(population)):
        score = evaluate_solution(population[i])
        if score < least_fittest_value:
            least_fittest_value = score
            least_fittest_index = i
    population[least_fittest_index] = offspring

def roulette_select(population):
    
    #Your Code Here
    total_fitness = sum([evaluate_solution(solution) for solution in population])
    pick = np.random.uniform(0, total_fitness)
    current = 0
    for solution in population:
        current += evaluate_solution(solution)
        if current > pick:
            return solution
        
    return population[-1]


def mutate(solution):

    index = np.random.randint(0, len(solution))
 
    sol = solution[:index]

    dfs_from_index = random_dfs(solution[index], goal_block_state, child_block_states)

    sol.extend(dfs_from_index.get_path())

    return sol
       

def genetic_algorithm(num_iterations, population_size, crossover_func, mutation_func, log=False):
    population = generate_population(population_size)
    
    
    best_solution = population[0] # Initial solution
    best_score = evaluate_solution(population[0])
    best_solution_generation = 0 # Generation on which the best solution was found
    
    generation_no = 0
    
    # print(f"Initial solution: {best_solution}, score: {best_score}")
    
    while(num_iterations > 0):
        new_population = []
        generation_no += 1
        yield best_solution, best_solution_generation # Yield the best solution found so far

        # Restores the population to its original solution ... to find optimal generational solutions
        best_solution = population[0] # Initial solution
        best_score = evaluate_solution(population[0]) 
        # Selection
        for i in range(0, population_size):
            tournment_winner_sol = tournament_select(population, 3)
            roulette_winner_sol = roulette_select(population)
            
            # Next generation Crossover and Mutation
            
            # Crossover
            child_1, child_2 = crossover_func(tournment_winner_sol, roulette_winner_sol)
    
            # Mutation ... TODO... add random probability
            if (np.random.rand() < 0.10): child_1 = mutation_func(child_1)
            if (np.random.rand() < 0.10): child_2 = mutation_func(child_2)
    
            new_population.append(child_1)
            new_population.append(child_2)

        population = new_population
        # REPLACE LEAST FIT ????
        # Checking the greatest fit among the current population
        greatest_fit, greatest_fit_score = get_greatest_fit(population)
        if greatest_fit_score > best_score:
            best_solution = greatest_fit
            best_score = greatest_fit_score
            best_solution_generation = generation_no
            if log:
                print(f"\nGeneration: {generation_no }")
                print(f"Solution: {best_solution}, score: {best_score}")
                print_population(population)
            print(f"score: {best_score}")
        else:
            num_iterations -= 1
    while True:
        yield None, None


