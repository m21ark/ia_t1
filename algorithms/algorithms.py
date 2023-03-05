## returns path between start and end points (x,y) in a matrix
#def bfs(matrix, start, end):
#    # Define the dimensions of the matrix
#    rows = int(sqrt(len(matrix)))
#    cols = rows
#
#    # Define a queue for BFS and a visited set to keep track of visited nodes
#    queue = deque()
#    visited = set()
#
#    # Define a dictionary to store the path from each node to the start point
#    path = {}
#    path[start] = None
#
#    # Add the starting point to the queue and mark it as visited
#    queue.append(start)
#    visited.add(start)
#
#    # Loop until the queue is empty
#    while queue:
#        # Get the next node from the queue
#        current = queue.popleft()
#
#        # Check if the current node is the end point
#        if current == end:
#            # Build the path by following the parent pointers from the end point
#            result = []
#            while current is not None:
#                result.append(current)
#                current = path[current]
#            result.reverse()
#            return result
#
#        # Get the row and column indices of the current node
#        row, col = current
#
#        # Check the neighbors of the current node
#        for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
#            # Compute the row and column indices of the neighbor
#            neighbor_row = row + dr
#            neighbor_col = col + dc
#
#            # Check if the neighbor is within the bounds of the matrix
#            if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
#                # Check if the neighbor has not been visited and is a path node
#                if matrix[neighbor_row + neighbor_col*MATRIX_COL] in [START_NODE, PATH_NODE, END_NODE] and (neighbor_row, neighbor_col) not in visited:
#                    # Add the neighbor to the queue and mark it as visited
#                    queue.append((neighbor_row, neighbor_col))
#                    visited.add((neighbor_row, neighbor_col))
#                    # Store the path from the current node to the neighbor
#                    path[(neighbor_row, neighbor_col)] = current
#
#    # If we reach this point, the end point is not reachable from the start point
#    return None


# A generic definition of a tree node holding a state of the problem
class TreeNode:
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent
        self.children = []
        if self.parent is None:
            self.depth = 0
        else:
            self.depth = self.parent.depth + 1

    def add_child(self, child_node):
        self.children.append(child_node)
        child_node.parent = self

from collections import deque

def breadth_first_search(initial_state, goal_state_func, operators_func):
    root = TreeNode(initial_state)   # create the root node in the search tree
    queue = deque([root])   # initialize the queue to store the nodes
    
    while queue:
        node = queue.popleft()   # get first element in the queue
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
        
        stack.extend([TreeNode(state, node) for state in operators_func(node.state)])
    return None


def depth_limited_search(initial_state, goal_state_func, operators_func, depth_limit):
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

        if node.depth < depth_limit:
            stack.extend([TreeNode(state, node) for state in operators_func(node.state)])
    return None




def iterative_deepening_search(initial_state, goal_state_func, operators_func, depth_limit):

    for depth in range(depth_limit):
        goal = depth_limited_search(initial_state, goal_state_func, operators_func, depth)
        if goal:
            return goal
    return None


def greedy_search(initial_state, goal_state_func, operators_func, heuristic_func):
    # your code here
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

        queue.extend([TreeNode(state, node) for state in operators_func(node.state)])
        queue.sort(key=lambda node: heuristic_func(node)) # IS THIS THE BEST SOLUTION IN TERMS OF TIME COMPLEXITY
    return None
    


def a_star_search(initial_state, goal_state_func, operators_func, heuristic):
    # your code here
    
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

        queue.extend([TreeNode(state, node) for state in operators_func(node.state)])
        queue.sort(key=lambda node: node.depth + heuristic(node))
    return None




from algorithms.block_state import *



def moveUp(self):
    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        y2 -= 2
        y -= 1
    else:
        if (self.isYtopX()):
            x = self.x2
            y2 -= 1
            y = self.y2
        elif (self.isXtopY()):
            x2 = self.x
            y -= 1
            y2 = self.y
        else:  # X and Y are on the same row
            y -= 1
            y2 -= 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st

def moveDown(self):
    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        y2 += 2
        y += 1
    else:
        if (self.isXtopY()):
            x = self.x2
            y2 += 1
            y = self.y2
        elif (self.isYtopX()):
            x2 = self.x
            y += 1
            y2 = self.y
        else:  # X and Y are on the same row
            y += 1
            y2 += 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st

def moveLeft(self):
    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        x2 -= 1
        x -= 2
    else:   
        if (self.isXrightY()):
            y = self.y2
            x2 -= 1
            x = self.x2
        elif (self.isYrightX()):
            y2 = self.y
            x -= 1
            x2 = self.x
        else:  # X and Y are on the same col
            x -= 1
            x2 -= 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st

def moveRight(self):
    # save current position
    x, y, x2, y2 = self.x, self.y, self.x2, self.y2
    if (self.isStanding()):
        x2 += 1
        x += 2
    else:
        if (self.isYrightX()):
            y = self.y2
            x2 += 1
            x = self.x2
        elif (self.isXrightY()):
            y2 = self.y
            x += 1
            x2 = self.x
        else:  # X and Y are on the same col
            x += 1
            x2 += 1
    # check if new position is valid.
    new_st = BlockState(x, y, x2, y2, self.maze)
    if (not new_st.checkIfCanMove()):
        return None
    return new_st
