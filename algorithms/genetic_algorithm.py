import numpy as np
from model.sample_mazes import * 
from algorithms.algorithms import *
import random

def crossover(solution_1, solution_2):
    
    intersection = set(solution_1).intersection(solution_2)

    inter_random_element = random.sample(intersection, 1)[0]
    child_1 = []
    child_2 = []

    inter = False
    for i in range(len(solution_1)):
        if not inter and solution_1[i] == inter_random_element:
            child_1.append(solution_1[i])
            inter = True
        else:
            try:
                child_1.append(solution_2[i])
            except:
                break
    
    inter = False
    for i in range(len(solution_2)):
        if not inter and solution_2[i] == inter_random_element:
            child_2.append(solution_2[i])
            inter = True
        else:
            try:
                child_2.append(solution_1[i])
            except:
                break

    return child_1, child_2

def evaluate_solution(solution):
    # num_incompatibilities = 0
    # # TODO: USAR HEURISTICA
    # dic = {}
    # for i in range(len(solution)):
    #     if solution[i] not in dic:
    #         dic[solution[i]] = 0
    #     else:
    #         dic[solution[i]] += 1
# 
    # for key in dic:
    #     if dic[key] > 1:
    #         num_incompatibilities += dic[key]
    # 
    # contais_end = False
    # for i in range(len(solution)):
    #     if goal_block_state(solution[i]):
    #         contais_end = True
    #         break
    # 
    # if not contais_end:
    #     num_incompatibilities += 1000
    # 
    # return -num_incompatibilities
    return -len(solution)
    

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


#def mutate_solution_1(solution):
#    index_1 = np.random.randint(0, len(solution))
#    index_2 = (index_1 + np.random.randint(0, len(solution))) % (len(solution) - 1) # Efficient way to generate a non-repeated index
#    solution[index_1], solution[index_2] = solution[index_2], solution[index_1]
#    return solution
#
#def mutate_solution_2(solution):
#    index = np.random.randint(0, len(solution))
#    solution[index] = np.random.randint(1, slots + 1)
#    return solution

# def mutate_solution_3(solution):
#     return (get_neighbor_solution3(solution))
# 

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
        
        # Selection
        for i in range(0, population_size):
            tournment_winner_sol = tournament_select(population, 4)
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
        
    print(f"  Final solution: {best_solution}, score: {best_score}")
    print(f"  Found on generation {best_solution_generation}")
    
    return best_solution

