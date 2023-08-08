import pygame
from pygame.locals import *

pygame.init()

icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Variables
screen_width = 600
screen_height = 600
line_width = 3
markers = []
Clicked = False
pos = []
player = 1
red = 255,0,0
blue = 0,0,255
green = 0,255,0
winner = 0
Tie = False
game_over = False
again_rect = Rect(screen_width//2 - 180, screen_height//2, 300, 70)


screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption("TicTacToe")

def draw_grid():
    bg = 135,206,250
    screen.fill(bg)
    grid = 50,50,50
    for x in range(1,3):
        pygame.draw.line(screen, grid, (20,x*200), (screen_width-20, x*200), line_width)
        pygame.draw.line(screen, grid, (x*200,20), (x*200, screen_height-20), line_width)

def ini_markers():
    for i in range(3):
        row = [0,0,0]
        markers.append(row)

ini_markers()
# print(markers)

def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, red, (x_pos*200 + 20, y_pos*200 + 20), (x_pos*200 + 180, y_pos*200 +180), line_width+5)
                pygame.draw.line(screen, red, (x_pos*200 + 20, y_pos*200 +180), (x_pos*200 + 180, y_pos*200 + 20), line_width+5)
            if y == -1:
                pygame.draw.circle(screen, blue, (x_pos*200 + 101, y_pos*200 + 101), 80, line_width+5)
            y_pos+=1;
        x_pos+=1

def check_winner():
    global winner
    global Tie
    global game_over
    y_pos = 0
    for x in markers:
        # check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
            break
        if sum(x) == -3:
            winner = 2
            game_over = True
            break
        # check row
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == 3:
            winner = 1
            game_over = True
            break
        if markers[0][y_pos] + markers[1][y_pos] + markers[2][y_pos] == -3:
            winner = 2
            game_over = True
            break
        y_pos += 1
    # check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[0][2] + markers[1][1] + markers[2][0] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[0][2] + markers[1][1] + markers[2][0] == -3:
        winner = 2
        game_over = True
    # check tie
    flag = False
    for x in markers:
        for y in x:
            if y == 0:
                flag = True
                break
    if winner == 0 and flag == False:
        Tie = True
        game_over = True

font = pygame.font.SysFont(None, 40)    

def draw_winner(winner, Tie):
    

    if Tie == True:
        win_txt = "It's a Tie"
        win_img = font.render(win_txt, True, green)
        pygame.draw.rect(screen, (255,165,0), (screen_width//2 - 180, screen_height//2 - 120, 300, 70))
        screen.blit(win_img, (screen_width//2 - 160, screen_height//2 - 100))
    else:
        win_txt = "Player " + str(winner) + " wins!"
        win_img = font.render(win_txt, True, green)
        pygame.draw.rect(screen, (255,165,0), (screen_width//2 - 180, screen_height//2 - 120, 300, 70))
        screen.blit(win_img, (screen_width//2 - 160, screen_height//2 - 100))

    # Play again
    again_txt = "Play Again"
    again_img = font.render(again_txt, True, green)
    pygame.draw.rect(screen, (255,165,0), again_rect)
    screen.blit(again_img, (screen_width//2 - 160, screen_height//2 + 20))
        



run = True
while run:

    draw_grid()
    draw_markers()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if game_over == False:
            if event.type == pygame.MOUSEBUTTONDOWN and Clicked == False:
                Clicked = True
            if event.type == pygame.MOUSEBUTTONUP and Clicked == True:
                Clicked = False
                pos = pygame.mouse.get_pos()
                pos_x = pos[0] // 200
                pos_y = pos[1] // 200
                if markers[pos_x][pos_y] == 0:
                    markers[pos_x][pos_y] = player
                    player *= -1
                    check_winner()
        
    if game_over == True:
        draw_winner(winner, Tie)
        # check play again
        if event.type == pygame.MOUSEBUTTONDOWN and Clicked == False:
                Clicked = True
        if event.type == pygame.MOUSEBUTTONUP and Clicked == True:
            Clicked = False
            pos = pygame.mouse.get_pos()
            if again_rect.collidepoint(pos):
                markers = []
                pos = []
                player = 1
                winner = 0
                game_over = False
                Tie = False
                ini_markers()

    pygame.display.update()


pygame.quit()