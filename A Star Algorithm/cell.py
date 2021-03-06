import math


class Cell:
    TOP_WALL = 0
    LEFT_WALL = 1
    RIGHT_WALL = 2
    BOTTOM_WALL = 3

    def __init__(self, x, y, size, max_size_x, max_size_y):
        self.is_visited = False
        # * [Top wall visibility,  Left wall visibility, Right wall visibility, Bottom wall visibility]
        self.walls = [True, True, True, True]
        self.x = x
        self.y = y
        self.i = math.floor(x/size)
        self.j = math.floor(y/size)
        self.max_size_x = max_size_x
        self.max_size_y = max_size_y
        self.size = size
        self.previous = None

        # * A* Purpose attributes
        self.f = 0
        self.g = 0
        self.h = 0

    def set_previous(self, previous):
        self.previous = previous

    def get_previous(self):
        return self.previous

    def set_f(self, f):
        self.f = f

    def set_g(self, g):
        self.g = g

    def set_h(self, h):
        self.h = h

    def get_f(self):
        return self.f  # self.g + self.h

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def get_coordinates(self):
        return [self.x, self.y]

    def get_visited(self):
        return self.is_visited

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def get_i(self):
        return self.i

    def get_j(self):
        return self.j

    def set_visited(self, is_visited):
        self.is_visited = is_visited

    def set_walls(self, walls):
        self.walls = walls
    # * return all the accesible neighbors, nodes that are not separated by a wall

    def get_available_neighbors(self, cells):
        neighbors = []
        if self.x >= self.size:
            if(not cells[math.floor((self.x - self.size)/20)][math.floor(self.y/20)].walls[Cell.RIGHT_WALL]):
                neighbors.append(
                    (math.floor((self.x - self.size)/20), math.floor(self.y/20)))
        if self.x < self.max_size_x - self.size:
            if(not cells[math.floor((self.x + self.size)/20)][math.floor(self.y/20)].walls[Cell.LEFT_WALL]):
                neighbors.append(
                    (math.floor((self.x + self.size)/20), math.floor(self.y/20)))
        if self.y >= self.size:
            if(not cells[math.floor(self.x/20)][math.floor((self.y - self.size)/20)].walls[Cell.BOTTOM_WALL]):
                neighbors.append(
                    (math.floor(self.x/20), math.floor((self.y - self.size)/20)))
        if self.y < self.max_size_y - self.size:
            if(not cells[math.floor(self.x/20)][math.floor((self.y + self.size)/20)].walls[Cell.TOP_WALL]):
                neighbors.append(
                    (math.floor(self.x/20), math.floor((self.y + self.size)/20)))
        return neighbors

    # * return alll the node neighbors
    def get_neighbors(self, cells):
        neighbors = []

        if self.x >= self.size:
            if(not cells[math.floor((self.x - self.size)/20)][math.floor(self.y/20)].is_visited):
                neighbors.append(
                    (math.floor((self.x - self.size)/20), math.floor(self.y/20)))
        if self.x < self.max_size_x - self.size:
            if(not cells[math.floor((self.x + self.size)/20)][math.floor(self.y/20)].is_visited):
                neighbors.append(
                    (math.floor((self.x + self.size)/20), math.floor(self.y/20)))
        if self.y >= self.size:
            if(not cells[math.floor(self.x/20)][math.floor((self.y - self.size)/20)].is_visited):
                neighbors.append(
                    (math.floor(self.x/20), math.floor((self.y - self.size)/20)))
        if self.y < self.max_size_y - self.size:
            if(not cells[math.floor(self.x/20)][math.floor((self.y + self.size)/20)].is_visited):
                neighbors.append(
                    (math.floor(self.x/20), math.floor((self.y + self.size)/20)))
        return neighbors

    # * set a wall as removed
    def remove_wall(self, wall):
        if wall == Cell.TOP_WALL:
            self.walls[0] = False
        elif wall == Cell.LEFT_WALL:
            self.walls[1] = False
        elif wall == Cell.RIGHT_WALL:
            self.walls[2] = False
        elif wall == Cell.BOTTOM_WALL:
            self.walls[3] = False

    def __str__(self):
        return f'Cell[ {self.x}, {self.y} ] -> walls{self.walls}'
