import pygame
import random
import math
from cell import Cell
from pathlib import Path

pygame.init()

# Variables definition
background_color = (0, 0, 0)
size = 20
screen_size = (1000, 600)
WIDTH = 800
HEIGHT = 600
time = 10
rect_color = (255, 255, 255)
running = True
cells = []
visited = []
cur_cell = Cell(0, 0, size, WIDTH, HEIGHT)
target_cell = Cell(0, 0, size, WIDTH, HEIGHT)
cur_c_x = 0
cur_c_y = 0
visitor_color = (164, 0, 219)
target_color = (255, 0, 0)
step_color = (164, 0, 219)
path_color = (0, 0, 255)
pause = False
path = Path(__file__).parent
font = pygame.font.Font(str(path.parent.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 12)
open_set = []
closed_set = []
path_followed = []

screen = pygame.display.set_mode(screen_size)

pygame.display.set_caption("A* Path Finding")


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
    cur_cell = Cell(0, 0, size, WIDTH, HEIGHT)
    visited = []
    cells = []
    cur_c_x = 0
    cur_c_y = 0
    init()


def init():
    global target_cell
    for i in range(0, WIDTH, size):
        new = []
        for j in range(0, HEIGHT, size):
            # * [Top wall visibility,  Left wall visibility, Right wall visibility, Bottom wall visibility]
            c = Cell(int(i), int(j), size, WIDTH, HEIGHT)
            # c.set_h(10)
            new.append(c)
        cells.append(new)
    cells[0][0].set_visited(True)
    # cells[0][0].set_h(0)
    visited.append((cells[0][0].get_i(), cells[0][0].get_j()))
    cur_cell = cells[0][0]

    target_cell = cells[len(cells)-1][len(cells[len(cells)-1])-1]
    open_set.append(cur_cell)


def draw_grid():
    for i in range(0, len(cells)):
        for j in range(0, len(cells[i])):
            draw_rect(i*size, j*size, size, cells[i][j].walls)


def draw_visitor(x, y, color):
    #pygame.draw.rect(screen, color, [x+1, y+1, size-1, size-1])
    pygame.draw.circle(screen, color, [x+10, y+10], 5)


def generate_maze():
    global cur_cell
    is_generated = False
    while not is_generated:
        cur_neighbors = cur_cell.get_neighbors(cells)
        # draw_visitor(cur_cell.get_x(), cur_cell.get_y())
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
                is_generated = True


def heuristic(c, t):
    dist = (math.sqrt(((t.get_x() - c.get_x())**2)+((t.get_y() - c.get_y())**2)))
    return dist


# * grid initialization
init()
generate_maze()
print(cur_cell)
print(target_cell)
path_followed.append(cur_cell)
#! test for non solvable mazes
#! cells[len(cells)-1][len(cells[len(cells)-1]) - 1].set_walls([True, True, True, True])
#!for i in range(0, len(cells)):
#!    for j in range(0, len(cells[i])):
#!        cells[i][j].set_walls([False, False, False, False])
# * Gameloop
ii = 0
while running:
    screen.fill(background_color)
    draw_grid()
    labels1 = []
    labels2 = []
    for cell in open_set:
        draw_visitor(cell.get_x(), cell.get_y(), (0, 255, 0))
        labels1.append(font.render(
            f"[{cell.get_x()},{cell.get_y()}]\n", True, (255, 255, 255)))

    for i in range(0, len(closed_set)):
        cell = closed_set[i]
        draw_visitor(cell.get_x(), cell.get_y(), step_color)
        if i > len(closed_set) - 20:
            labels2.append(font.render(
                f"[{cell.get_x()},{cell.get_y()}]\n", True, (255, 255, 255)))

    text = font.render('OpenSet: ', True, (255, 255, 255))
    text2 = font.render('ClosedSet: ', True, (255, 255, 255))
    rect = text.get_rect()
    rect2 = text.get_rect()
    rect.bottomleft = (820, 20)
    rect2.bottomleft = (900, 20)
    screen.blit(text, rect)
    screen.blit(text2, rect2)
    i = 20
    for label in labels1:
        screen.blit(label, [820, i, 850, i+20])
        i += 20
    i = 20
    for label in labels2:
        screen.blit(label, [900, i, 950, i+20])
        i += 20
    if not pause:
        if len(open_set) > 0:
            best = 0
            for i in range(0, len(open_set)):
                if open_set[i].get_f() < open_set[best].get_f():
                    best = i

            cur_cell = open_set[best]

            if cur_cell == target_cell:

                if time == 10:
                    last_cell = closed_set[len(closed_set) - 1]
                    path_followed.append(last_cell)
                    time = 100

                    while not last_cell.get_previous() is None:
                        path_followed.append(last_cell)
                        last_cell = last_cell.get_previous()
                    path_followed.reverse()
                else:
                    for i in range(0, ii):
                        c = path_followed[i]
                        draw_visitor(c.get_x(), c.get_y(), (235, 203, 0))
                    ii += 1 if (ii < len(path_followed)) else 0
            else:
                open_set.pop(best)
                closed_set.append(cur_cell)

                neighbors = cur_cell.get_available_neighbors(cells)

                for idx in neighbors:
                    cell = cells[idx[0]][idx[1]]
                    cell.set_g(1)
                    if not cell in closed_set:
                        tmp_g = cur_cell.get_g() + 1

                    if cells[idx[0]][idx[1]] in open_set:
                        if tmp_g < cells[idx[0]][idx[1]].get_g():
                            tmp_g = cur_cell.get_g() + 1
                    elif not cells[idx[0]][idx[1]] in closed_set:
                        cells[idx[0]][idx[1]].set_g(tmp_g)
                        cells[idx[0]][idx[1]].set_previous(cur_cell)
                        open_set.append(cells[idx[0]][idx[1]])
                        cells[idx[0]][idx[1]].set_h(
                            heuristic(cells[idx[0]][idx[1]], target_cell))
                        cells[idx[0]][idx[1]].set_f(
                            cells[idx[0]][idx[1]].get_g() + cells[idx[0]][idx[1]].get_h())

        else:
            print("No Solution")
    draw_visitor(WIDTH - size, HEIGHT - size, target_color)

    pygame.display.update()
    pygame.time.wait(time)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
