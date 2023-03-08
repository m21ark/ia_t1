from collections import deque
from algorithms.block_state import *


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

    def get_path(self):
        path = []
        node = self
        while node is not None:
            path.append(node.state)
            node = node.parent
        path.reverse()
        return path
    
    def __eq__(self, other):
        if isinstance(other, TreeNode):
            return self.state == other.state and self.depth == other.depth
        return False

    def __hash__(self):
        return hash((self.state, self.depth))


def breadth_first_search(initial_state, goal_state_func, operators_func):
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

    for depth in range(depth_limit):
        goal = depth_limited_search(
            initial_state, goal_state_func, operators_func, depth)
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

        queue.extend([TreeNode(state, node)
                     for state in operators_func(node.state)])
        # IS THIS THE BEST SOLUTION IN TERMS OF TIME COMPLEXITY
        queue.sort(key=lambda node: heuristic_func(node))
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

        queue.extend([TreeNode(state, node)
                     for state in operators_func(node.state)])
        queue.sort(key=lambda node: node.depth + heuristic(node))
    return None


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


def hint_call(alg, blockSt: BlockState):
    hint_call.dic = {
        depth_first_search: lambda: depth_first_search(blockSt, goal_block_state, child_block_states),
        breadth_first_search: lambda: breadth_first_search(blockSt, goal_block_state, child_block_states),
        iterative_deepening_search: lambda:  iterative_deepening_search(blockSt, goal_block_state, child_block_states, 300),
    }

    return hint_call.dic[alg]


def goal_block_state(self):  # TODO: a mesma questão de ser or ou and
    return self.maze[self.x + self.y * MATRIX_COL] == END_NODE or self.maze[self.x2 + self.y2 * MATRIX_COL] == END_NODE


def child_block_states(state):
    return [x for x in [moveUp(state), moveDown(state), moveLeft(state), moveRight(state)] if x is not None]
