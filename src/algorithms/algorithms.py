from collections import deque
from algorithms.block_state import *
from model.game_model import GameModel
import math


class TreeNode:
    '''
    A node in the search tree.
    '''

    def __init__(self, state, parent=None):
        '''
        state: the state of the node
        parent: the parent node of this node
        '''
        self.state = state
        self.parent = parent
        self.children = []
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def add_child(self, child_node):
        '''
        Add a child node to the current node.
        '''
        self.children.append(child_node)
        child_node.parent = self

    def get_path(self):
        '''
        Get the path from the root node to the current node.
        '''
        path = []
        node = self
        while node is not None:
            path.append(node.state)
            node = node.parent
        path.reverse()
        return path

    def __eq__(self, other):
        '''
        Compare two nodes.
        '''
        if isinstance(other, TreeNode):
            return self.state == other.state and self.depth == other.depth
        return False

    def __hash__(self):
        '''
        Hash the node.
        '''
        return hash((self.state, self.depth))


def breadth_first_search(initial_state, goal_state_func, operators_func):
    '''
    Breadth-first search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    '''

    root = TreeNode(initial_state)   # create the root node in the search tree
    queue = deque([root])   # initialize the queue to store the nodes

    visited = set()
    while queue:
        node = queue.popleft()   # get first element in the queue

        if node.state in visited:
            continue

        visited.add(node.state)

        if goal_state_func(node.state):   # check goal state
            return node

        for state in operators_func(node.state):   # go through next states
            # create tree node with the new state
            state_node = TreeNode(state)

            # link child node to its parent in the tree
            node.add_child(state_node)

            # enqueue the child node
            queue.append(state_node)

    return None


def depth_first_search(initial_state, goal_state_func, operators_func):
    '''
    Depth-first search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    '''
    root = TreeNode(initial_state)
    stack = [root]

    visited = set()
    while stack:
        node = stack.pop()

        if node.state in visited:
            continue

        visited.add(node.state)

        if goal_state_func(node.state):
            return node

        stack.extend([TreeNode(state, node)
                     for state in operators_func(node.state)])
    return None


def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):
    '''
    Depth-limited search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    depth_limit: the depth limit of the search
    '''
    root = TreeNode(initial_state)
    stack = [root]
    visited = set()
    while stack:
        node = stack.pop()
        if node in visited:
            continue

        visited.add(node)

        if goal_state_func(node.state):
            return node

        if node.depth < depth_limit:
            stack.extend([TreeNode(state, node)
                         for state in operators_func(node.state)])
    return None


def iterative_deepening_search(initial_state, goal_state_func, operators_func, depth_limit):
    '''
    Iterative deepening search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    '''

    for depth in range(depth_limit):
        goal = depth_limited_search(
            initial_state, goal_state_func, operators_func, depth)
        if goal:
            return goal
    return None


def greedy_search(initial_state, goal_state_func, operators_func, heuristic_func):
    '''
    Greedy search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    heuristic_func: a function that takes a node and returns the heuristic value of the node
    '''
    root = TreeNode(initial_state)
    queue = [root]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node.state in visited:
            continue

        visited.add(node.state)

        if goal_state_func(node.state):
            return node

        queue.extend([TreeNode(state, node)
                     for state in operators_func(node.state)])

        queue.sort(key=lambda node: heuristic_func(node))
    return None


def a_star_search(initial_state, goal_state_func, operators_func, heuristic):
    '''
    A* search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    heuristic: a function that takes a node and returns the heuristic value of the node
    '''

    root = TreeNode(initial_state)
    queue = [root]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node.state in visited:
            continue

        visited.add(node.state)

        if goal_state_func(node.state):
            return node

        queue.extend([TreeNode(state, node)
                     for state in operators_func(node.state)])
        queue.sort(key=lambda node: node.depth + heuristic(node))
    return None


def a_star_weighted_search(initial_state, goal_state_func, operators_func, heuristic):
    '''
    A* search algorithm.
    initial_state: the initial state of the search
    goal_state_func: a function that takes a state and returns True if the state is a goal state
    operators_func: a function that takes a state and returns a list of next states
    heuristic: a function that takes a node and returns the heuristic value of the node
    '''

    root = TreeNode(initial_state)
    queue = [root]
    visited = set()
    while queue:
        node = queue.pop(0)
        if node.state in visited:
            continue

        visited.add(node.state)

        if goal_state_func(node.state):
            return node

        queue.extend([TreeNode(state, node)
                     for state in operators_func(node.state)])
        queue.sort(key=lambda node: node.depth + 1.5*heuristic(node))
    return None


def moveUp(self):
    '''
    Move the block up.
    Returns the new state if the move is valid, otherwise returns None.
    '''

    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        y2 -= 2
        y -= 1
    else:
        if (self.isYtopX()):
            x = self.x2
            y2 -= 1
            y = y2
        elif (self.isXtopY()):
            x2 = self.x
            y -= 1
            y2 = y
        else:  # X and Y are on the same row
            y -= 1
            y2 -= 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st


def moveDown(self):
    '''
    Move the block down.
    Returns the new state if the move is valid, otherwise returns None.
    '''

    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        y2 += 2
        y += 1
    else:
        if (self.isXtopY()):
            x = self.x2
            y2 += 1
            y = y2
        elif (self.isYtopX()):
            x2 = self.x
            y += 1
            y2 = y
        else:  # X and Y are on the same row
            y += 1
            y2 += 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st


def moveLeft(self):
    '''
    Move the block left.
    Returns the new state if the move is valid, otherwise returns None.
    '''

    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        x2 -= 1
        x -= 2
    else:
        if (self.isXrightY()):
            y = self.y2
            x2 -= 1
            x = x2
        elif (self.isYrightX()):
            y2 = self.y
            x -= 1
            x2 = x
        else:  # X and Y are on the same col
            x -= 1
            x2 -= 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st


def moveRight(self):
    '''
    Move the block right.
    Returns the new state if the move is valid, otherwise returns None.
    '''

    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        x2 += 1
        x += 2
    else:
        if (self.isYrightX()):
            y = self.y2
            x2 += 1
            x = x2
        elif (self.isXrightY()):
            y2 = self.y
            x += 1
            x2 = x
        else:  # X and Y are on the same col
            x += 1
            x2 += 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st


def manhattan_distance_heuristic(node):
    '''
    Manhattan distance heuristic.
    node: a node in the search tree
    '''

    end_x, end_y = GameModel.GOAL
    # /2.0 so that the heuristic is admissible and consistent
    return abs(min(node.state.x, node.state.x2) - end_x) + abs(min(node.state.y, node.state.y2) - end_y) / 2.0


def chebyshev_distance_heuristic(node):
    '''
    Chebyshev distance heuristic.
    node: a node in the search tree
    '''

    end_x, end_y = GameModel.GOAL
    # /2.0 so that the heuristic is admissible and consistent
    return max(abs(min(node.state.x, node.state.x2) - end_x), abs(min(node.state.y, node.state.y2) - end_y)) / 2.0


def euclidean_distance_heuristic(node):
    '''
    Euclidean distance heuristic.
    node: a node in the search tree
    '''

    end_x, end_y = GameModel.GOAL
    # /2.0 so that the heuristic is admissible and consistent
    return math.sqrt((min(node.state.x, node.state.x2) - end_x) ** 2 + (min(node.state.y, node.state.y2) - end_y) ** 2) / 2.0


def hint_call(alg, blockSt: BlockState):
    ''' 
    This function is called when the user clicks on the hint button.
    It calls the algorithm that the user chose and returns the next move.
    '''

    from algorithms.genetic_algorithm import genetic_algorithm, crossover, mutate, random_dfs
    hint_call.dic = {
        'DFS': lambda: depth_first_search(blockSt, goal_block_state, child_block_states),
        'BFS': lambda: breadth_first_search(blockSt, goal_block_state, child_block_states),
        'Iterative deepening': lambda:  iterative_deepening_search(blockSt, goal_block_state, child_block_states, 200),
        'Greedy (manhattan)': lambda: greedy_search(blockSt, goal_block_state, child_block_states, manhattan_distance_heuristic),
        'A* (manhattan)': lambda: a_star_search(blockSt, goal_block_state, child_block_states, manhattan_distance_heuristic),
        'A* W=1.5 (manhattan)': lambda: a_star_weighted_search(blockSt, goal_block_state, child_block_states, manhattan_distance_heuristic),
        'Greedy (chebyshev)': lambda: greedy_search(blockSt, goal_block_state, child_block_states, chebyshev_distance_heuristic),
        'A* (chebyshev)': lambda: a_star_search(blockSt, goal_block_state, child_block_states, chebyshev_distance_heuristic),
        'A* W=1.5 (chebyshev)': lambda: a_star_weighted_search(blockSt, goal_block_state, child_block_states, chebyshev_distance_heuristic),
        'Greedy (euclidean)': lambda: greedy_search(blockSt, goal_block_state, child_block_states, euclidean_distance_heuristic),
        'A* (euclidean)': lambda: a_star_search(blockSt, goal_block_state, child_block_states, euclidean_distance_heuristic),
        'A* W=1.5 (euclidean)': lambda: a_star_weighted_search(blockSt, goal_block_state, child_block_states, euclidean_distance_heuristic),
        'Genetic': lambda: None,
        'Random DFS': lambda: random_dfs(blockSt, goal_block_state, child_block_states),
    }

    return hint_call.dic[alg]


def goal_block_state(self):
    '''
    Returns True if the block is in the goal state.
    '''

    return self.maze[self.x + self.y * MATRIX_COL] == END_NODE or self.maze[self.x2 + self.y2 * MATRIX_COL] == END_NODE


def child_block_states(state):
    '''
    Returns a list of all possible child states.
    '''
    return [x for x in [moveUp(state), moveDown(state), moveLeft(state), moveRight(state)] if x is not None]
