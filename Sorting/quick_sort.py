import pygame
import random
import math
from pathlib import Path

path = Path(__file__).parent


pygame.init()

screen_size = (600, 600)
WIDTH = 800
HEIGHT = 600
running = True
background_color = (0, 0, 0)
time = 100
lines = []
pause = False

font = pygame.font.Font(str(path.parent.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 12)
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("QuickSort Algorithm")


class Line:
    def __init__(self, color, size):
        self.color = color
        self.size = size

    def get_color(self):
        return self.color

    def get_size(self):
        return self.size

    def __str__(self):
        return f"{self.size}"

    def __repr__(self):
        return f"{self.size}"


def init():
    t = round(HEIGHT / 255)
    c = 1
    r = 255
    v = 0
    for i in range(1, HEIGHT):
        l = Line((r, v, 0), i)
        lines.append(l)
        if c < t:
            c += 1
        else:
            r -= 1
            v += 1
            c = 0


def shuffle():
    for i in range(0, 1000):
        x1 = random.randrange(0, len(lines) - 1)
        x2 = random.randrange(0, len(lines) - 1)
        tmp = lines[x1]
        lines[x1] = lines[x2]
        lines[x2] = tmp


def partition(arr, min, max):
    i = (min - 1)
    pivot = arr[max].get_size()

    for j in range(min, max):
        if arr[j].get_size() <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[max] = arr[max], arr[i+1]
    return i + 1

###
# Recursive implementation
#! for practical purpose this visualization use an iterative implementation
#! in order to show the algorithm step by step.


def quickSort(arr, min, max):
    if len(arr) == 1:
        return arr
    if min < max:
        pi = partition(arr, min, max)
        quickSort(arr, min, pi-1)
        quickSort(arr, pi+1, max)


init()
shuffle()
idx = 0

# Create an auxiliary stack
size = HEIGHT
stack = [0] * (size)
l = 0
h = len(lines) - 1

top = -1

top = top + 1
stack[top] = l
top = top + 1
stack[top] = h

while running:
    screen.fill(background_color)

    x = 1

    for i in lines:
        pygame.draw.line(screen, i.get_color(), (x, HEIGHT),
                         (x, HEIGHT - i.get_size()))
        x += 1
    if not pause:
        if top >= 0:

            h = stack[top]
            top = top - 1
            l = stack[top]
            top = top - 1

            p = partition(lines, l, h)

            if p-1 > l:
                top = top + 1
                stack[top] = l
                top = top + 1
                stack[top] = p - 1

            if p + 1 < h:
                top = top + 1
                stack[top] = p + 1
                top = top + 1
                stack[top] = h

    pygame.display.update()
    pygame.time.wait(time)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pause = not pause
