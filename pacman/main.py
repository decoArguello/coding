import pygame
import random
import math
from pathlib import Path
from maze import *
from pacman import Pacman

path = Path(__file__).parent
pygame.init()

WIDTH = 800
HEIGHT = 700

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac Man")

running = True
background_color = (0, 0, 0)
border_color = (32, 32, 214)
pacman_color = (255, 255, 0)
cookie_color = (255, 184, 151)


def draw_cookies():
    x, y = 1, 1
    for i in range(0, len(maze_array)):
        for j in range(0, len(maze_array[i])):
            if maze_array[i][j] != 0 and maze_array[i][j] != 5 and maze_array[i][j] != 9:
                pygame.draw.circle(screen, cookie_color, [
                                   (x*20)+120, (y*20)+70], 2 * maze_array[i][j])
            x = x + 1 if x < len(maze_array[i]) else 1
        y = y + 1


def draw_ghost_home():
    pygame.draw.line(screen, border_color, [320, 310], [320, 390], 1)
    pygame.draw.line(screen, border_color, [460, 310], [460, 390], 1)
    pygame.draw.line(screen, border_color, [320, 390], [460, 390], 1)
    pygame.draw.line(screen, border_color, [320, 310], [360, 310], 1)
    pygame.draw.line(screen, border_color, [420, 310], [460, 310], 1)


def draw_pacman():
    x = 390
    y = 530
    pi = 3.14
    pygame.draw.circle(screen, pacman_color, [390, 530], 15)
    #r = 15
    #cx, cy = 390, 530,
    # for n in range(45, 321):
    #    x = cx + int(r*math.cos(n*math.pi/180))
    #    y = cy + int(r*math.sin(n*math.pi/180))
    #    pygame.draw.line(screen, pacman_color, (390, 530), (x, y), 1)


pacman = Pacman(390, 530)
mouth = False
while running:
    screen.fill(background_color)

    draw_cookies()
    draw_ghost_home()
    pacman.draw(screen, mouth)
    pygame.display.update()
    keys = pygame.key.get_pressed()  # checking pressed keys
    if keys[pygame.K_UP]:
        mouth = not mouth
        pacman.set_direction(Pacman.UP)
        pacman.set_y(pacman.get_y()-10)
    elif keys[pygame.K_DOWN]:
        mouth = not mouth
        pacman.set_direction(Pacman.DOWN)
        pacman.set_y(pacman.get_y()+10)
    elif keys[pygame.K_RIGHT]:
        mouth = not mouth
        pacman.set_direction(Pacman.RIGHT)
        pacman.set_x(pacman.get_x()+10)
    elif keys[pygame.K_LEFT]:
        mouth = not mouth
        pacman.set_direction(Pacman.LEFT)
        pacman.set_x(pacman.get_x()-10)
    pygame.display.update()
    pygame.time.wait(250)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.key:
            mouth = not mouth
            if event.key == pygame.K_UP:
                pacman.set_direction(Pacman.UP)
                pacman.set_y(pacman.get_y()-10)
            elif event.key == pygame.K_DOWN:
                pacman.set_direction(Pacman.DOWN)
                pacman.set_y(pacman.get_y()+10)
            elif event.key == pygame.K_RIGHT:
                pacman.set_direction(Pacman.RIGHT)
                pacman.set_x(pacman.get_x()+10)
            elif event.key == pygame.K_LEFT:
                pacman.set_direction(Pacman.LEFT)
                pacman.set_x(pacman.get_x()-10)
