import random
from Cell import *

class Enviroment(object):
    def __init__(self, enviroment_width, enviroment_height, cell_size):
        self.cell_size = cell_size
        self.enviroment_width = (enviroment_width // self.cell_size)
        self.enviroment_height = (enviroment_height // self.cell_size)
        self.cells = self.init_cells()        

    def init_cells(self):
        return [[Cell(i * self.cell_size, j * self.cell_size, random.choice([True, False, False, False]), self.cell_size) for i in range(self.enviroment_width)] for j in range(self.enviroment_height)]

    def update(self):
        for i in range(self.enviroment_height):
            for j in range(self.enviroment_width):
                neighbors = self.count_neighbors(i, j)
                
                if self.cells[i][j].is_alive:
                    if neighbors < 2 or neighbors > 3:
                        self.cells[i][j].is_alive = False
                else:
                    if neighbors == 3:
                        self.cells[i][j].is_alive = True
                
                self.cells[i][j].update()
                    
    def count_neighbors(self, row, col):
        count = 0
        for i in range(row - 1, row + 2):
            for j in range(col - 1, col + 2):
                if (i >= 0 and i < self.enviroment_height) and (j >= 0 and j < self.enviroment_width):
                    if self.cells[i][j].is_alive:
                        count += 1
        
        if self.cells[row][col].is_alive:
            count -= 1
            
        return count
