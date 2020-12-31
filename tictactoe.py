import pygame

pygame.init()
win = pygame.display.set_mode((600,700))
pygame.display.set_caption("Tic Tac Toe")
x_img = pygame.image.load('x.png')
o_img = pygame.image.load('o.png')
clock = pygame.time.Clock()
winner = None
draw_game = False
turn = 'X'
gameOver = False
moves = 0
location = [None, None, None,
            None, None, None,
            None, None, None]
        
def check_board(x, y):
    global location, turn, moves 
    if x in range(0, 200) and y in range(0, 200) and location[0] == None:
        location[0] = turn
        moves +=1                                               
    if x in range(200, 400) and y in range(0, 200) and location[1] == None:        
        location[1] = turn
        moves +=1
    if x in range(400, 600) and y in range(0, 200) and location[2] == None:        
        location[2] = turn
        moves +=1
    if x in range(0, 200) and y in range(200, 400) and location[3] == None:        
        location[3] = turn
        moves +=1
    if x in range(200, 400) and y in range(200, 400) and location[4] == None:        
        location[4] = turn
        moves +=1
    if x in range(400, 600) and y in range(200, 400) and location[5] == None:        
        location[5] = turn
        moves +=1
    if x in range(0, 200) and y in range(400, 600) and location[6] == None:        
        location[6] = turn
        moves +=1
    if x in range(200, 400) and y in range(400, 600) and location[7] == None:        
        location[7] = turn
        moves +=1
    if x in range(400, 600) and y in range(400, 600) and location[8] == None:        
        location[8] = turn
        moves +=1
                    
def draw():
    win.fill((255, 255, 255))
    pygame.draw.line(win, (0,0,0), (0,0), (600,0), width=1)
    pygame.draw.line(win, (0,0,0), (0,200), (600,200), width=1)
    pygame.draw.line(win, (0,0,0), (0,400), (600,400), width=1)
    pygame.draw.line(win, (0,0,0), (0,600), (600, 600), width=1)
    pygame.draw.line(win, (0,0,0), (200,0), (200,600), width=1)
    pygame.draw.line(win, (0,0,0), (400,0), (400,600), width=1)    
    if location[0] == 'X':
        win.blit(x_img, [25, 25])
    if location[0] == 'O':
        win.blit(o_img, [25, 25])        
    if location[1] == 'X':
        win.blit(x_img, [225, 25])
    if location[1] == 'O':
        win.blit(o_img, [225, 25])       
    if location[2] == 'X':
        win.blit(x_img, [425, 25])
    if location[2] == 'O':
        win.blit(o_img, [425, 25])        
    if location[3] == 'X':
        win.blit(x_img, [25, 225])
    if location[3] == 'O':
        win.blit(o_img, [25, 225])        
    if location[4] == 'X':
        win.blit(x_img, [225, 225])
    if location[4] == 'O':
        win.blit(o_img, [225, 225])        
    if location[5] == 'X':
        win.blit(x_img, [425, 225])
    if location[5] == 'O':
        win.blit(o_img, [425, 225])        
    if location[6] == 'X':
        win.blit(x_img, [25, 425])
    if location[6] == 'O':
        win.blit(o_img, [25, 425])        
    if location[7] == 'X':
        win.blit(x_img, [225, 425])
    if location[7] == 'O':
        win.blit(o_img, [225, 425])        
    if location[8] == 'X':
        win.blit(x_img, [425, 425])
    if location[8] == 'O':
        win.blit(o_img, [425, 425])
       
def status():
    if winner == None:
        text = str(turn) + "'s turn"
    else:
        text = str(winner) + ' wins!'
    if draw_game == True:
        text = '  Draw! '        
    font_style = pygame.font.SysFont('Technical', 36)
    game_text = font_style.render(text, True, (0, 0, 0))
    reset_text = font_style.render('(r) to reset', True, (0, 0, 0))
    win.blit(game_text, [250, 625])
    if gameOver or draw_game:
        win.blit(reset_text, [240, 660])
                                   
def logic():
    global winner, gameOver
    #check horizontal win
    if location[0] == 'X' and location[1] == 'X' and location[2] == 'X':
        winner = 'X'
        gameOver = True
    if location[3] == 'X' and location[4] == 'X' and location[5] == 'X':
        winner = 'X'
        gameOver = True
    if location[6] == 'X' and location[7] == 'X' and location[8] == 'X':
        winner = 'X'
        gameOver = True
    if location[0] == 'O' and location[1] == 'O' and location[2] == 'O':
        winner = 'O'
        gameOver = True
    if location[3] == 'O' and location[4] == 'O' and location[5] == 'O':
        winner = 'O'
        gameOver = True
    if location[6] == 'O' and location[7] == 'O' and location[8] == 'O':
        winner = 'O'
        gameOver = True
    #check vertical win
    if location[0] == 'X' and location[3] == 'X' and location[6] == 'X':
        winner = 'X'
        gameOver = True
    if location[1] == 'X' and location[4] == 'X' and location[7] == 'X':
        winner = 'X'
        gameOver = True
    if location[2] == 'X' and location[5] == 'X' and location[8] == 'X':
        winner = 'X'
        gameOver = True
    if location[0] == 'O' and location[3] == 'O' and location[6] == 'O':
        winner = 'O'
        gameOver = True
    if location[1] == 'O' and location[4] == 'O' and location[7] == 'O':
        winner = 'O'
        gameOver = True
    if location[2] == 'O' and location[5] == 'O' and location[8] == ')':
        winner = 'O'
        gameOver = True
    #check diagonal win
    if location[0] == 'X' and location[4] == 'X' and location[8] == 'X':
        winner = 'X'
        gameOver = True
    if location[6] == 'X' and location[4] == 'X' and location[2] == 'X':
        winner = 'X'
        gameOver = True
    if location[0] == 'O' and location[4] == 'O' and location[8] == 'O':
        winner = 'O'
        gameOver = True
    if location[6] == 'O' and location[4] == 'O' and location[2] == 'O':
        winner = 'O'
        gameOver = True

def change_turn():
    global turn, gameOver, draw_game
    if moves == 9 and winner == None:
        draw_game = True
        gameOver = True
    if moves % 2 == 0:
        turn = 'X'
    else:
        turn = 'O'
                               
def main():
    global clock, location, winner, gameOver, turn, moves, draw_game
    run = True
    while run:
        for event in pygame.event.get():       
            if event.type == pygame.QUIT:
                run = False           
            if pygame.mouse.get_pressed()[0] and not gameOver:                           
                pos = pygame.mouse.get_pos()
                x, y = pos      
                check_board(x, y)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and gameOver:
                    location[0] = None
                    location[1] = None
                    location[2] = None
                    location[3] = None
                    location[4] = None
                    location[5] = None
                    location[6] = None
                    location[7] = None
                    location[8] = None
                    winner = None
                    gameOver = False
                    moves = 0
                    draw_game = False
        logic()
        change_turn()
        draw()
        status()        
        clock.tick(30)
        pygame.display.update()
    pygame.quit()
main()

        
