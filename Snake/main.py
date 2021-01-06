import pygame
import random
from pathlib import Path

# pygame initialing
pygame.init()

# game variables
path = Path(__file__).parent
font = pygame.font.Font(str(path.parent.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 12)

running = True
snake_color = (41, 60, 15)
background_color = (132, 169, 3)
screen_size = (800, 600)

snake_head_x = 400
snake_head_y = 300
move_x = 10
move_y = 0
snake = [[snake_head_x, snake_head_y], [snake_head_x -
                                        10, snake_head_y], [snake_head_x-20, snake_head_y]]

is_fruit_visible = False
fruit_x = -1
fruit_y = 0
fruit_timer = 0
fruit_timer2 = 0

score = 0
# pygame game window setup
screen = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Snake")

# game functions


def reset():
    global snake_head_x
    global snake_head_y
    global snake
    global is_fruit_visible
    global fruit_x
    global fruit_y
    global fruit_timer
    global fruit_timer2
    global score

    score = 0
    snake_head_x = 400
    snake_head_y = 300
    snake = [[snake_head_x, snake_head_y], [snake_head_x -
                                            10, snake_head_y], [snake_head_x-20, snake_head_y]]
    is_fruit_visible = False
    fruit_x = -1
    fruit_y = 0
    fruit_timer = 0
    fruit_timer2 = 0

# draw snake body


def draw_block(x, y):
    pygame.draw.rect(screen, snake_color, [x, y, 10, 10])

# draw the block that increments the snake size


def draw_fruit():
    global fruit_x
    global fruit_y
    if fruit_x == -1:
        fruit_y = random.randrange(0, 590, 10)
        fruit_x = random.randrange(0, 790, 10)
    pygame.draw.rect(screen, snake_color, [fruit_x + 3, fruit_y + 0, 4, 4])
    pygame.draw.rect(screen, snake_color, [fruit_x + 3, fruit_y + 6, 4, 4])
    pygame.draw.rect(screen, snake_color, [fruit_x + 0, fruit_y + 3, 4, 4])
    pygame.draw.rect(screen, snake_color, [fruit_x + 6, fruit_y + 3, 4, 4])

# validate if exists collision


def validate_collision():
    global score
    if len(snake) > 1:
        for i in range(2, len(snake)):
            if snake[0][0] == snake[i][0] and snake[0][1] == snake[i][1]:
                return True
    return False

# draw all the pieces of the snake body


def draw_snake(x, y):
    for i in range(len(snake)):
        tmp_x = snake[i][0]
        tmp_y = snake[i][1]
        snake[i][0] = x
        snake[i][1] = y
        draw_block(snake[i][0], snake[i][1])
        x = tmp_x
        y = tmp_y


# game loop
while running:
    text = font.render('Score: '+str(score), True, (0, 0, 0))
    rect = text.get_rect()
    rect.bottomleft = (20, 20)

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

    screen.fill(background_color)

    screen.blit(text, rect)

    draw_snake(snake_head_x, snake_head_y)

    # change snake direction movement
    if snake_head_x > screen_size[0] - 10:
        snake_head_x = 0
    elif snake_head_y > screen_size[1] - 10:
        snake_head_y = 0
    elif snake_head_x < 0:
        snake_head_x = screen_size[0] - 10
    elif snake_head_y < 0:
        snake_head_y = screen_size[1] - 10
    else:
        snake_head_x += move_x
        snake_head_y += move_y

    # show or hide fruit
    if not is_fruit_visible:
        fruit_timer2 = 0
        if fruit_timer == 20:  # 150:
            fruit_timer = 0
            is_fruit_visible = True
        else:
            fruit_timer += 1
    else:
        fruit_timer = 0
        draw_fruit()

        if fruit_x == snake[0][0] and fruit_y == snake[0][1]:
            snake.append([snake[len(snake)-1][0], snake[len(snake)-1][1]])
            is_fruit_visible = False
            fruit_x = -1
            score += 1
        if fruit_timer2 == 70:
            fruit_timer2 = 0
            is_fruit_visible = False
            fruit_x = -1
        else:
            fruit_timer2 += 1

    if validate_collision():
        reset()
    pygame.display.update()
    pygame.time.wait(100)

pygame.quit()
