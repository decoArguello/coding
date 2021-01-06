import pygame
import random
from cell import Cell
from pathlib import Path

pygame.init()

# Variables definition
background_color = (0, 0, 0)
size = 20
screen_size = (800, 600)
rect_color = (255, 255, 255)
running = True
cells = []
visited = []
cur_cell = Cell(0, 0, size, screen_size[0], screen_size[1])
cur_c_x = 0
cur_c_y = 0
pause = False

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("Maze Generator")


# functions definition
def draw_rect(x, y, size, walls):
    # ? top wall
    if walls[0]:
        pygame.draw.line(screen, rect_color, (x, y), (x+size, y))
    # ? left wall
    if walls[1]:
        pygame.draw.line(screen, rect_color, (x, y), (x, y+size))
    # ? right wall
    if walls[2]:
        pygame.draw.line(screen, rect_color, (x+size, y), (x+size, y+size))
    # ? bottom wall
    if walls[3]:
        pygame.draw.line(screen, rect_color, (x, y+size), (x+size, y+size))


def reset():
    global visited
    global cells
    global cur_cell
    global cur_c_x
    global cur_c_y
    cur_cell = Cell(0, 0, size, screen_size[0], screen_size[1])
    visited = []
    cells = []
    cur_c_x = 0
    cur_c_y = 0
    init()


def init():
    for i in range(0, screen_size[0], size):
        new = []
        for j in range(0, screen_size[1], size):
            # * [Top wall visibility,  Left wall visibility, Right wall visibility, Bottom wall visibility]
            c = Cell(int(i), int(j), size, screen_size[0], screen_size[1])
            new.append(c)
        cells.append(new)
    cells[0][0].set_visited(True)
    visited.append((cells[0][0].get_i(), cells[0][0].get_j()))
    cur_cell = cells[0][0]


def draw_grid():
    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            draw_rect(i*size, j*size, size, cells[i][j].walls)


def draw_visitor(x, y):
    pygame.draw.rect(screen, (164, 0, 219), [x+1, y+1, size-1, size-1])


# * grid initialization
init()
# * Gameloop
draw_visitor(0, 0)
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
    if not pause:
        screen.fill(background_color)
        draw_grid()
        cur_neighbors = cur_cell.get_neighbors(cells)
        draw_visitor(cur_cell.get_x(), cur_cell.get_y())
        idx = 0
        if len(cur_neighbors) > 0:
            tmp_cell = cur_cell
            if len(cur_neighbors) > 1:
                idx = random.randrange(0, len(cur_neighbors), 1)
            cur_cell = cells[cur_neighbors[idx][0]][cur_neighbors[idx][1]]
            cells[cur_neighbors[idx][0]
                  ][cur_neighbors[idx][1]].set_visited(True)
            visited.append((cur_cell.get_i(), cur_cell.get_j()))
            # * validate what direction the visitor follows
            if tmp_cell.get_i() > cur_cell.get_i():
                cells[tmp_cell.get_i()][tmp_cell.get_j()
                                        ].remove_wall(Cell.LEFT_WALL)
                cells[cur_cell.get_i()][cur_cell.get_j()
                                        ].remove_wall(Cell.RIGHT_WALL)
            elif tmp_cell.get_i() < cur_cell.get_i():
                cells[tmp_cell.get_i()][tmp_cell.get_j()
                                        ].remove_wall(Cell.RIGHT_WALL)
                cells[cur_cell.get_i()][cur_cell.get_j()
                                        ].remove_wall(Cell.LEFT_WALL)
            elif tmp_cell.get_j() > cur_cell.get_j():
                cells[tmp_cell.get_i()][tmp_cell.get_j()
                                        ].remove_wall(Cell.TOP_WALL)
                cells[cur_cell.get_i()][cur_cell.get_j()
                                        ].remove_wall(Cell.BOTTOM_WALL)
            elif tmp_cell.get_j() < cur_cell.get_j():
                cells[tmp_cell.get_i()][tmp_cell.get_j()
                                        ].remove_wall(Cell.BOTTOM_WALL)
                cells[cur_cell.get_i()][cur_cell.get_j()
                                        ].remove_wall(Cell.TOP_WALL)
        else:
            if len(visited) > 0:
                cor = visited.pop()
                cur_cell = cells[cor[0]][cor[1]]
            else:
                reset()

    pygame.display.update()
    pygame.time.wait(50)
pygame.quit()
