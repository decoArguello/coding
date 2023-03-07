import pygame
import time
from random import randint
from random import choice
import math
from pathlib import Path
from Maze import Maze

path = Path(__file__).parent.parent
pygame.init()
font = pygame.font.Font(str(path.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 8)

pygame.init()

start = time.time()

WIDTH = 800
CELL_SIZE = 20
NR_CELLS = math.floor(WIDTH / CELL_SIZE)
TOP = 0
LEFT = 1
BOTTOM = 2
RIGHT = 3

background_color = (230,230,230)
purple = (127,0,255)
delaying = 0
last_time = time.time()
cells = []
visited_cells = []
screen = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Maze generator")

running = True

maze = Maze(WIDTH,WIDTH,CELL_SIZE, (225,225,225))

def drawVisitor(posX, posY):
    pygame.draw.rect(screen, purple, pygame.Rect(posX * CELL_SIZE, posY * CELL_SIZE, 1 * CELL_SIZE, 1 * CELL_SIZE))

while running:
    now = time.time()
    screen.fill(background_color)
    
    maze.draw(screen)
    
    ##drawVisitor(current_pos_x, current_pos_y)
    
    ## if last_time + delaying < now and len(visited_cells) > 0:
    ##     last_time = now
    ##     moveVisitor()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False