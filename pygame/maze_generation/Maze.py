import pygame
from random import randint, choice
import math
from Cell import Cell

class Maze:
    TOP = 0
    LEFT = 1
    BOTTOM = 2
    RIGHT = 3

    def __init__(self, width, height, cell_size, color):
        self.NR_CELLS_X = math.floor(width / cell_size)
        self.NR_CELLS_Y = math.floor(height / cell_size)
        self.cell_size = cell_size
        self.color = color
        self.cells = []        
        self.visited_cells = []
        self.current_pos_x = randint(0,self.NR_CELLS_X - 1)
        self.current_pos_y = randint(0,self.NR_CELLS_Y - 1)
        
        self.__initialize_array()

        self.cells[((self.current_pos_y+1) * self.NR_CELLS_Y) -  self.NR_CELLS_X + self.current_pos_x ].set_visited(True, color)
        self.visited_cells.append(self.cells[((self.current_pos_y+1) * self.NR_CELLS_Y) -  self.NR_CELLS_X + self.current_pos_x ])
        
        while len(self.visited_cells) > 0:
            self.__moveVisitor()

    def draw(self, screen):
        for i in range(self.NR_CELLS_X * self.NR_CELLS_Y):
            cell = self.cells[i]        
            cell.draw(screen, self.cell_size)

    def __initialize_array(self):
        index = 0
        for i in range(self.NR_CELLS_Y):
            for j in range(self.NR_CELLS_X):
                self.cells.append( Cell(j,i, (255,255,255),index))
                index = index + 1

    def __moveVisitor(self):
        idx = ((self.current_pos_y+1) * self.NR_CELLS_Y) -  self.NR_CELLS_X + self.current_pos_x  
        
        non_visited_neighbors = []
        
        if self.current_pos_x  > 0:
            if not self.cells[idx - 1].visited:
                non_visited_neighbors.append((idx - 1, Maze.LEFT))
        if self.current_pos_x < self.NR_CELLS_X -1:        
            if not self.cells[idx + 1].visited:
                non_visited_neighbors.append((idx + 1, Maze.RIGHT))
        if self.current_pos_y < self.NR_CELLS_Y -1:        
            if not self.cells[idx + self.NR_CELLS_Y].visited:
                non_visited_neighbors.append((idx + self.NR_CELLS_Y, Maze.BOTTOM))
        if self.current_pos_y > 0:        
            if not self.cells[idx - self.NR_CELLS_Y].visited:
                non_visited_neighbors.append((idx -self. NR_CELLS_Y, Maze.TOP))
        if not len(non_visited_neighbors) > 0:
            visited_cell = self.visited_cells.pop()
            self.current_pos_x = visited_cell.x
            self.current_pos_y = visited_cell.y
            return
        ch = choice(non_visited_neighbors)
    
        if ch[1] == Maze.TOP:
            self.cells[ch[0]].remove_wall(Maze.BOTTOM)
            self.cells[idx].remove_wall(Maze.TOP)
        elif ch[1] == Maze.BOTTOM:
            self.cells[ch[0]].remove_wall(Maze.TOP)
            self.cells[idx].remove_wall(Maze.BOTTOM)    
        elif ch[1] == Maze.RIGHT:
            self.cells[ch[0]].remove_wall(Maze.LEFT)
            self.cells[idx].remove_wall(Maze.RIGHT)
        else:        
            self.cells[ch[0]].remove_wall(Maze.RIGHT)
            self.cells[idx].remove_wall(Maze.LEFT)

        self.cells[ch[0]].set_visited(True, self.color)
        self.visited_cells.append(self.cells[ch[0]])
        self.current_pos_x = self.cells[ch[0]].x
        self.current_pos_y = self.cells[ch[0]].y