import pygame
import math


class Pacman:
    pacman_color = (255, 255, 0)
    UP = 1
    DOWN = 2
    RIGHT = 3
    LEFT = 4

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direction = Pacman.RIGHT

    def draw(self, screen, mouth):
        if not mouth:
            pygame.draw.circle(screen, Pacman.pacman_color,
                               [self.x, self.y], 15)
        else:
            r = 15
            cx, cy = self.x, self.y
            d1, d2 = 45, 321
            if self.direction == Pacman.LEFT:
                d1, d2 = 225, 501
            if self.direction == Pacman.DOWN:
                d1, d2 = 491, 767
            if self.direction == Pacman.UP:
                d1, d2 = 311, 587
            for n in range(d1, d2):
                _x = cx + int(r*math.cos(n*math.pi/180))
                _y = cy + int(r*math.sin(n*math.pi/180))
                pygame.draw.line(screen, Pacman.pacman_color,
                                 (self.x, self.y), (_x, _y), 2)

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def set_x(self, x):
        self.x = x

    def set_y(self, y):
        self.y = y

    def set_direction(self, d):
        self.direction = d
