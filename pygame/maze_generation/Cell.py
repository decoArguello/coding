import pygame
class Cell:
    def __init__(self, x, y, color, index):
        self.index = index
        self.x = x
        self.y = y
        self.visited = False
        self.walls = [True,True,True,True]
        self.color = color
        self.TOP = 0
        self.LEFT = 1
        self.BOTTOM = 2
        self.RIGHT = 3

    def set_visited (self, visited):
        self.visited = visited
        self.color = (200,200,200)

    def remove_wall (self, wall_index):
        self.walls[wall_index] = False
    
    def draw(self, screen, size):
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x *size, self.y * size, 1 * size, 1 * size))
        if self.walls[self.TOP]:
            pygame.draw.line(screen, pygame.Color(0,0,0), (self.x * size, self.y * size),( self.x * size + size, self.y * size))
        if self.walls[self.BOTTOM]:
            pygame.draw.line(screen, pygame.Color(0,0,0), (self.x * size, self.y * size + size),( self.x * size+ size, self.y * size+ size))
        if self.walls[self.LEFT]:
            pygame.draw.line(screen, pygame.Color(0,0,0), (self.x * size, self.y * size),(self.x * size, self.y * size+ size))  
        if self.walls[self.RIGHT]:
            pygame.draw.line(screen, pygame.Color(0,0,0), (self.x * size+ size, self.y * size),(self.x * size+ size, self.y * size+ size))
    
    def to_string(self):
        print(f'({self.x}, {self.y}) [{self.index}] | walls: TOP:{self.walls[self.TOP]} BOTTOM:{self.walls[self.BOTTOM]} LEFT:{self.walls[self.LEFT]} RIGHT:{self.walls[self.RIGHT]} | visited: {self.visited}')