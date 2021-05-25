import pygame
import time
import random
import math
from pathlib import Path
from spot import Spot


path = Path(__file__).parent
pygame.init()

start = time.time()

font = pygame.font.Font(str(path.parent.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 12)
font2 = pygame.font.Font(str(path.parent.resolve()) +
                        '/fonts/Roboto-Regular.ttf', 25)
WIDTH = 900
HEIGHT = 420
background_color = (230,230,230)
isFirstClick = True

filas = int((HEIGHT - 20 ) /20)
columnas = int(WIDTH / 20)

print(f"{filas}, {columnas}")
screen = pygame.display.set_mode((WIDTH, HEIGHT+40))
pygame.display.set_caption("Buscaminas")

colors = {
1 : (0,0,255),
2 : (33,139,33),
3 : (255,0,0),
4 : (0,0,128),
5 : (155,82,82),
6 : (255,123,0),
7 : (127, 0, 130),
8 : (241, 240, 50),
0 : (0,0,0)
}

numbers = {
1 : pygame.image.load(f"{path}/images/1.PNG"),
2 : pygame.image.load(f"{path}/images/2.PNG"),
3 : pygame.image.load(f"{path}/images/3.PNG"),
4 : pygame.image.load(f"{path}/images/4.PNG"),
5 : pygame.image.load(f"{path}/images/5.PNG"),
6 : pygame.image.load(f"{path}/images/6.PNG"),
7 : pygame.image.load(f"{path}/images/7.PNG"),
8 : pygame.image.load(f"{path}/images/8.PNG"),
9 : pygame.image.load(f"{path}/images/9.PNG"),
0 : pygame.image.load(f"{path}/images/0.PNG"),
}


icono = pygame.image.load(f"{path}/images/Minesweeper_Icon.PNG")
pygame.display.set_icon(icono)


brick = pygame.image.load(f"{path}/images/Brick.PNG")
flag = pygame.image.load(f"{path}/images/flag.PNG")
empty = pygame.image.load(f"{path}/images/Empty.PNG")
mine = pygame.image.load(f"{path}/images/Mine.PNG")

happy = pygame.image.load(f"{path}/images/happy.PNG")
winner = pygame.image.load(f"{path}/images/winner.PNG")
death = pygame.image.load(f"{path}/images/death.PNG")
asombrado = pygame.image.load(f"{path}/images/O.PNG")

icons = {
'lose' : death,
'winner' : winner,
'running' : happy,
':O': asombrado,
}

game_status =  'running'

board = []


running = True
minesPct = 12
nMines = 100 #int((filas * columnas - 20) * minesPct / 100 )
nFlags = nMines

def reset():
    global board
    global game_status
    global start
    global nFlags
    global isFirstClick

    board = []
    nFlags = nMines
    game_status =  'running'
    genBoard()
    start = time.time()
    isFirstClick = True

def genBoard():    
    for i in range(0, filas):
        row = []
        for j in range(0,columnas):
            b = Spot(i,j)
            row.append(b)
        board.append(row)

def fillMines(_x,_y):
    mines_counter = 0
    while mines_counter < nMines:
        x = random.randrange(0, columnas)
        y = random.randrange(0, filas)
        if(not board[y][x].get_is_mine()) and x != _x and y != _y:
            board[y][x].set_x = x
            board[y][x].set_y = y
            board[y][x].set_is_mine(True)
            mines_counter = mines_counter + 1

def get_neighbors_count(x,y):
    mine_count = 0
    if y > 0 and x > 0:
        if board[y-1][x-1].get_is_mine():
            mine_count = mine_count + 1

    if x > 0 and y <filas - 1:
        if board[y+1][x-1].get_is_mine():
                mine_count = mine_count + 1
    
    if y < filas - 1 and x < columnas -1:
        if board[y+1][x+1].get_is_mine():
            mine_count = mine_count + 1
    
    if y > 0 and x < columnas -1:
        if board[y-1][x+1].get_is_mine():
            mine_count = mine_count + 1
    
    if y > 0:
        if board[y-1][x].get_is_mine():
            mine_count = mine_count + 1

    if y < filas - 1:
        if board[y+1][x].get_is_mine():
            mine_count = mine_count + 1
    
    if x > 0:       
        if board[y][x-1].get_is_mine():
            mine_count = mine_count + 1
    
    if x < columnas -1:
        if board[y][x+1].get_is_mine():
            mine_count = mine_count + 1
    
    return mine_count
def descubrir_vecinos(c, r):
    co = 0 ## Cuenta el numero de llamados a la funcion por cada celda
    if get_neighbors_count(c,r) == 0:
        if c > 0 and not board[r][c-1].get_is_discovered() and not board[r][c-1].get_is_mine() and not board[r][c-1].get_is_flagged():
            board[r][c-1].set_is_discovered(True)
            descubrir_vecinos(c-1,r)
            co = co + 1

        if c < columnas - 1 and not board[r][c+1].get_is_discovered() and not board[r][c+1].get_is_mine() and not board[r][c+1].get_is_flagged():
            board[r][c+1].set_is_discovered(True)
            descubrir_vecinos(c+1,r)
            co = co + 1
        
        if r > 0 and not board[r-1][c].get_is_discovered() and not board[r-1][c].get_is_mine() and not board[r-1][c].get_is_flagged():   
            board[r-1][c].set_is_discovered(True)
            descubrir_vecinos(c,r-1)
            co = co + 1

        if r < filas - 1 and not board[r+1][c].get_is_discovered() and not board[r+1][c].get_is_mine() and not board[r+1][c].get_is_flagged():   
            board[r+1][c].set_is_discovered(True)
            descubrir_vecinos(c,r+1)
            co = co + 1
        
        if c > 0 and r > 0 and not board[r-1][c-1].get_is_discovered() and not board[r-1][c-1].get_is_mine() and not board[r-1][c-1].get_is_flagged():
            board[r-1][c-1].set_is_discovered(True)
            descubrir_vecinos(c-1,r-1)
            co = co + 1
        
        if c < columnas -1 and r > 0 and not  board[r-1][c+1].get_is_discovered() and not board[r-1][c+1].get_is_mine() and not board[r-1][c+1].get_is_flagged():
            board[r-1][c+1].set_is_discovered(True)
            descubrir_vecinos(c+1,r-1)
            co = co + 1
        
        if c < columnas - 1 and r < filas - 1 and not board[r+1][c+1].get_is_discovered() and not board[r+1][c+1].get_is_mine() and not board[r+1][c+1].get_is_flagged():
            board[r+1][c+1].set_is_discovered(True)
            descubrir_vecinos(c+1,r+1)
            co = co + 1
        
        if c > 0 and r < filas - 1 and not  board[r+1][c-1].get_is_discovered() and not board[r+1][c-1].get_is_mine() and not board[r+1][c-1].get_is_flagged():
            board[r+1][c-1].set_is_discovered(True)
            descubrir_vecinos(c-1,r+1)
            co = co + 1

def validate_click(btn, pos):
    global game_status
    global isFirstClick
    x = int(pos[0]/20)
    y = int((pos[1] - 40)/20)
    global nFlags

    if isFirstClick:
        fillMines(x,y)
        isFirstClick = False
    if(btn == 1):    
        if(not board[y][x].get_is_flagged()):   
            if board[y][x].get_is_mine():
                game_status='lose'         
            elif get_neighbors_count(x,y) == 0 and not board[y][x].get_is_discovered() and not board[y][x].get_is_mine():
               descubrir_vecinos(x,y)         
            board[y][x].set_is_discovered(True) 
    elif(btn == 3):
        
        if(not board[y][x].get_is_discovered()): 
            if not board[y][x].get_is_flagged():
                if nFlags > 0:
                    board[y][x].set_is_flagged(True)
                    nFlags = nFlags - 1
            else:
                board[y][x].set_is_flagged(False)
                nFlags = nFlags + 1
    validate_game_status()

def button_clicked():
    reset()

def validate_game_status():
    global game_status
    for y in range(0,filas):
        for x in range(0,columnas):
            if not board[y][x].get_is_flagged() and not board[y][x].get_is_discovered():
                return
    game_status =  'winner'
    print(game_status)

def debug_board():
    for y in range(0,filas):
        for x in range(0,columnas):
            p = "*" if board[y][x].get_is_mine() else str(get_neighbors_count(x,y))
            print(  f"{p} " , end = '')
        print("")


genBoard()

click_counter  = 0


while running:
    screen.fill(background_color)
    
    if game_status == 'running':

        current = time.time()
        seconds=int(current - start)
        t = 4 - len(str(seconds))
        zeros = "0" * t
        str_timer = zeros + str(seconds)
        
    font2.bold = True
    text = font2.render(f'{int(str_timer[0])}', True, colors.get(3, "Invalid number"))
    rect = text.get_rect()
    rect.bottomleft = (10, 35)
    screen.blit(text, rect)

    font2.bold = True
    text = font2.render(f'{int(str_timer[1])}', True, colors.get(3, "Invalid number"))
    rect = text.get_rect()
    rect.bottomleft = (25, 35)
    screen.blit(text, rect)

    font2.bold = True
    text = font2.render(f'{int(str_timer[2])}', True, colors.get(3, "Invalid number"))
    rect = text.get_rect()
    rect.bottomleft = (40, 35)
    screen.blit(text, rect)

    font2.bold = True
    text = font2.render(f'{int(str_timer[3])}', True, colors.get(3, "Invalid number"))
    rect = text.get_rect()
    rect.bottomleft = (55, 35)
    screen.blit(text, rect)


    font.bold = True
    text = font.render(f'Banderas:', True, colors.get(1, "Invalid number"))
    rect = text.get_rect()
    rect.bottomleft = (785, 35)
    screen.blit(text, rect)

    font.bold = True
    text = font.render(f'{nFlags}', True, colors.get(1, "Invalid number"))
    rect = text.get_rect()
    rect.bottomleft = (850, 35)
    screen.blit(text, rect)
    
    
    b = pygame.transform.scale(icons.get(game_status, 'what?'), (30,30))
    screen.blit(b, ((WIDTH / 2) - 15, 5)) 
  
    for i in range(0,filas):
        for j in range(0,columnas):
            if(board[i][j].get_is_flagged()):
                b = pygame.transform.scale(flag, (20,20))
                screen.blit(b, ((j*20), (i*20)+40))   
            elif(not board[i][j].get_is_discovered()):
                b = pygame.transform.scale(brick, (20,20))
                screen.blit(b, ((j*20), (i*20)+40))
            elif(board[i][j].get_is_discovered() and not board[i][j].get_is_mine()):
                b = pygame.transform.scale(empty, (20,20))
                screen.blit(b, ((j*20), (i*20)+40)) 
                
                n_mines = get_neighbors_count(j,i)
                s = "" if n_mines == 0 else n_mines
                font.bold = True
                text = font.render(f'{s}', True, colors.get(n_mines, "Invalid number"))
                rect = text.get_rect()
                rect.bottomleft = ((j*20)+7, (i*20)+58)
                screen.blit(text, rect)
            else:
                b = pygame.transform.scale(mine, (20,20))
                screen.blit(b, ( (j*20),(i*20)+40))
  
    pygame.display.update()
    ##pygame.time.wait(250)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.pos[1] > 5 and event.pos[1] < 35 and event.pos[0] > (WIDTH / 2) - 15 and event.pos[0] < (WIDTH / 2) + 15:
                button_clicked()
                #print(f"button clicked: {click_counter}")
                #click_counter = click_counter +1
            if event.pos[1] >= 40 and event.pos[1] <= HEIGHT +20  and game_status == 'running':
                validate_click(event.button, event.pos)
                if event.button == 3:
                    b = pygame.transform.scale(icons.get(":O", 'what?'), (30,30))
                    screen.blit(b, ((WIDTH / 2) - 15, 5))
                    pygame.display.update()
                    pygame.time.wait(180)