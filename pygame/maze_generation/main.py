import pygame
import time
from random import randint
from random import choice
import math
from pathlib import Path
from Cell import Cell

path = Path(__file__).parent.parent
pygame.init()
font = pygame.font.Font(str(path.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 8)

pygame.init()

start = time.time()

WIDTH = 1000
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
index = 0
for i in range(NR_CELLS):
    for j in range(NR_CELLS):
        cells.append( Cell(j,i, (255,255,255),index))
        index = index + 1

current_pos_x = randint(0,NR_CELLS - 1)
current_pos_y = randint(0,NR_CELLS - 1)

def drawVisitor(posX, posY):
    pygame.draw.rect(screen, purple, pygame.Rect(posX * CELL_SIZE, posY * CELL_SIZE, 1 * CELL_SIZE, 1 * CELL_SIZE))

def fill_neighbors(posX, posY):
    idx = ((posY+1) * NR_CELLS) -  NR_CELLS + posX   
    
    if posX > 0:
        cells[idx - 1].set_visited(True)
    if posX < NR_CELLS -1:        
        cells[idx + 1].set_visited(True)
    if posY > 0:        
        cells[idx - NR_CELLS].set_visited(True)    
    if posY < NR_CELLS -1:        
        cells[idx + NR_CELLS].set_visited(True)

def moveVisitor():
    global current_pos_x
    global current_pos_y

    idx = ((current_pos_y+1) * NR_CELLS) -  NR_CELLS + current_pos_x  
    
    non_visited_neighbors = []
    
    if current_pos_x  > 0:
        if not cells[idx - 1].visited:
            non_visited_neighbors.append((idx - 1, LEFT))
    if current_pos_x < NR_CELLS -1:        
        if not cells[idx + 1].visited:
            non_visited_neighbors.append((idx + 1, RIGHT))
    if current_pos_y < NR_CELLS -1:        
        if not cells[idx + NR_CELLS].visited:
            non_visited_neighbors.append((idx + NR_CELLS, BOTTOM))
    if current_pos_y > 0:        
        if not cells[idx - NR_CELLS].visited:
            non_visited_neighbors.append((idx - NR_CELLS, TOP))
    if not len(non_visited_neighbors) > 0:
        visited_cell = visited_cells.pop()
        current_pos_x = visited_cell.x
        current_pos_y = visited_cell.y
        return

    
    ch = choice(non_visited_neighbors)
    
    if ch[1] == TOP:
        cells[ch[0]].remove_wall(BOTTOM)
        cells[idx].remove_wall(TOP)
    elif ch[1] == BOTTOM:
        cells[ch[0]].remove_wall(TOP)
        cells[idx].remove_wall(BOTTOM)    
    elif ch[1] == RIGHT:
        cells[ch[0]].remove_wall(LEFT)
        cells[idx].remove_wall(RIGHT)
    else:        
        cells[ch[0]].remove_wall(RIGHT)
        cells[idx].remove_wall(LEFT)

    cells[ch[0]].set_visited(True)
    visited_cells.append(cells[ch[0]])
    current_pos_x = cells[ch[0]].x
    current_pos_y = cells[ch[0]].y

cells[((current_pos_y+1) * NR_CELLS) -  NR_CELLS + current_pos_x ].set_visited(True)
visited_cells.append(cells[((current_pos_y+1) * NR_CELLS) -  NR_CELLS + current_pos_x ])
while running:
    now = time.time()
    screen.fill(background_color)
    
    for i in range(NR_CELLS ** 2):
        cell = cells[i]        
        cell.draw(screen, CELL_SIZE)
    
    drawVisitor(current_pos_x, current_pos_y)
    
    if last_time + delaying < now and len(visited_cells) > 0:
        last_time = now
        moveVisitor()

    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False