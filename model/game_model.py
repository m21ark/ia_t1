from algorithms.block_state import BlockState

class GameModel:   
    def __init__(self, maze):
        self.maze = maze
        self.block = BlockState(3, 3, 3, 3, maze)

    @property
    def get_maze(self):
        return self.maze
    

    @property
    def get_block(self):
        return self.block
    
    def set_block(self, block):
        self.block = block

    