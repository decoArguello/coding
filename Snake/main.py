import pygame
import random
# pygame initialing
pygame.init()

# game variables
running = True
snakeColor = (41, 60, 15)
backgroundColor = (132, 169, 3)
screenSize = (800, 600)

snake_head_x = 400
snake_head_y = 300
move_x = 10
move_y = 0
snake = [[snake_head_x, snake_head_y]]

isFruitVisible = False
fruit_x = -1
fruit_y = 0
fruitTimer = 0
fruitTimer2 = 0

# pygame game window setup
screen = pygame.display.set_mode(screenSize)
pygame.display.set_caption("Snake")

# game functions


def reset():
    global snake_head_x
    global snake_head_y
    global snake
    global isFruitVisible
    global fruit_x
    global fruit_y
    global fruitTimer
    global fruitTimer2

    snake_head_x = 400
    snake_head_y = 300
    snake = [[snake_head_x, snake_head_y]]
    isFruitVisible = False
    fruit_x = -1
    fruit_y = 0
    fruitTimer = 0
    fruitTimer2 = 0

# draw snake body


def drawBlock(x, y):
    pygame.draw.rect(screen, snakeColor, [x, y, 10, 10])

# draw the block that increments the snake size


def drawFruit():
    global fruit_x
    global fruit_y
    if fruit_x == -1:
        fruit_y = random.randrange(0, 590, 10)
        fruit_x = random.randrange(0, 790, 10)
    pygame.draw.rect(screen, snakeColor, [fruit_x + 3, fruit_y + 0, 4, 4])
    pygame.draw.rect(screen, snakeColor, [fruit_x + 3, fruit_y + 6, 4, 4])
    pygame.draw.rect(screen, snakeColor, [fruit_x + 0, fruit_y + 3, 4, 4])
    pygame.draw.rect(screen, snakeColor, [fruit_x + 6, fruit_y + 3, 4, 4])

# validate if exists collision


def validateCollision():
    if len(snake) > 1:
        for i in range(1, len(snake)-1):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                return True
    return False

# draw all the pieces of the snake body


def drawSnake(x, y):
    for i in range(len(snake)):
        tmp_x = snake[i][0]
        tmp_y = snake[i][1]
        snake[i][0] = x
        snake[i][1] = y
        drawBlock(snake[i][0], snake[i][1])
        x = tmp_x
        y = tmp_y


# game loop
while running:
    # event manager
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and move_y == 0:
                move_x = 0
                move_y = -10
            elif event.key == pygame.K_DOWN and move_y == 0:
                move_x = 0
                move_y = 10
            elif event.key == pygame.K_RIGHT and move_x == 0:
                move_x = 10
                move_y = 0
            elif event.key == pygame.K_LEFT and move_x == 0:
                move_x = -10
                move_y = 0

    screen.fill(backgroundColor)

    drawSnake(snake_head_x, snake_head_y)

    # change snake direction movement
    if snake_head_x > screenSize[0] - 10:
        snake_head_x = 0
    elif snake_head_y > screenSize[1] - 10:
        snake_head_y = 0
    elif snake_head_x < 0:
        snake_head_x = screenSize[0] - 10
    elif snake_head_y < 0:
        snake_head_y = screenSize[1] - 10
    else:
        snake_head_x += move_x
        snake_head_y += move_y

    # show or hide fruit
    if not isFruitVisible:
        fruitTimer2 = 0
        if fruitTimer == 20:  # 150:
            fruitTimer = 0
            isFruitVisible = True
        else:
            fruitTimer += 1
    else:
        fruitTimer = 0
        drawFruit()

        if fruit_x == snake[0][0] and fruit_y == snake[0][1]:
            snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]])
            isFruitVisible = False
            fruit_x = -1
        if fruitTimer2 == 70:
            fruitTimer2 = 0
            isFruitVisible = False
            fruit_x = -1
        else:
            fruitTimer2 += 1

    if validateCollision():
        reset()

    pygame.time.wait(100)
    pygame.display.update()
