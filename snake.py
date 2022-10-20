import pygame, random, time
from pygame.locals import *
 
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((0,0,0))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
stop = 0


snake = [(200,200),
        (210,200)]

shadow_snake = [(200,200),
                (210,200)]

snake_skin = pygame.Surface((10,10))
shadow_snake_skin = pygame.Surface((9,9))
snake_skin.fill((255,255,255))
shadow_snake_skin.fill((255, 255, 0))
apple = pygame.Surface((10,10))
apple.fill((255,0,0))
pos_apple = ((random.randint(10,590)//10)*10,(random.randint(0,540)//10)*10)

IMAGE_MACA = pygame.image.load('maca.png')
IMAGE_MACA = pygame.transform.scale(IMAGE_MACA,(70,40))




game_over = pygame.image.load("gameover.png")
rect_image = game_over.get_rect(center=(200,190))

CIMA = 0
ESQUERDA = 1
DIREITA = 2
BAIXO = 3
PARADO = 4

direcao = ESQUERDA
jogo = 0
menu = 1
while menu:
    clock.tick(20)
    for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == MOUSEBUTTONDOWN:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                if x > 250 and x < 400 and y > 340 and y < 430:
                    menu = 0
                    jogo = 1
                    stop = 0
                
    screen.fill((0,0,0))

    IMAGE_SNAKEGAME = pygame.image.load('snakegame.png')
    IMAGE_SNAKEGAME = pygame.transform.scale(IMAGE_SNAKEGAME, (500, 250))
    rect_snakegame = IMAGE_SNAKEGAME.get_rect(center=(275,200))
    screen.blit(IMAGE_SNAKEGAME, rect_snakegame)
    
    IMAGE_START = pygame.image.load('start.png')
    IMAGE_START = pygame.transform.scale(IMAGE_START, (250,150))
    rect_start = IMAGE_START.get_rect(center=(300, 415))
    screen.blit(IMAGE_START, rect_start)
    pygame.display.update()

    while jogo:
        #Ajustando fps da tela
        clock.tick(20)
        #Gerenciando os comandos
        for event in pygame.event.get():
            #Fechar o jogo
            if event.type == QUIT:
                pygame.quit()
            #Direcionando a snake
            if event.type == KEYDOWN:
                if event.key ==K_UP and direcao != BAIXO:
                    direcao = CIMA
                if event.key ==K_DOWN and direcao != CIMA:
                    direcao = BAIXO
                if event.key ==K_LEFT and direcao != DIREITA:
                    direcao = ESQUERDA
                if event.key ==K_RIGHT and direcao != ESQUERDA:
                    direcao = DIREITA    
        #Limpar tela
        screen.fill((0,0,0))
        
        pygame.draw.rect(screen, (255,255,0), [0, 0, 600, 560], 4)
        
        for i in range(len(snake)-1,0,-1):
            snake[i] = (snake[i-1][0], snake[i-1][1])
            shadow_snake[i] = (shadow_snake[i-1][0], shadow_snake[i-1][1])

        #Direcionando a snake
        if direcao == CIMA:
            snake[0] = (snake[0][0], snake[0][1] - 10)
            shadow_snake[0] = (shadow_snake[0][0], shadow_snake[0][1] - 10)
        if direcao == BAIXO:
            snake[0] = (snake[0][0], snake[0][1] + 10)
            shadow_snake[0] = (shadow_snake[0][0], shadow_snake[0][1] + 10)
        if direcao == DIREITA:
            snake[0] = (snake[0][0] + 10, snake[0][1])
            shadow_snake[0] = (shadow_snake[0][0] + 10, shadow_snake[0][1])
        if direcao == ESQUERDA:
            snake[0] = (snake[0][0] - 10, snake[0][1])
            shadow_snake[0] = (shadow_snake[0][0] - 10, shadow_snake[0][1])
        if direcao == PARADO:
            snake[0] = (snake[0][0], snake[0][1])
            shadow_snake[0] = (shadow_snake[0][0], shadow_snake[0][1])
        
        for pos in snake:
            screen.blit(snake_skin,pos)
        for pos in shadow_snake:
            screen.blit(shadow_snake_skin,pos)
        

        rect_maca = IMAGE_MACA.get_rect(center=(pos_apple[0],pos_apple[1]))
        screen.blit(IMAGE_MACA,rect_maca)

        pygame.display.update()

        if snake[0] == pos_apple:
            pos_apple = ((random.randint(10,590)//10)*10,(random.randint(0,540)//10)*10)
            snake.append((10,10))
            shadow_snake.append((10,10))
        
        fonte_placar = pygame.font.SysFont(None, 25)
        pontucao = fonte_placar.render(f"Pontuação: {len(snake)-2}",True, (255,255,255))
        screen.blit(pontucao, [2, 570])

        if snake[0][0] > 600:
            snake[0] = (0,snake[0][1])
            shadow_snake[0] = (0,shadow_snake[0][1])
        if snake[0][1] == 550:
            snake[0] = (snake[0][0],0)
            shadow_snake[0] = (shadow_snake[0][0],0)
        if snake[0][0] < 0:
            snake[0] = (600,snake[0][1])
            shadow_snake[0] = (600,shadow_snake[0][1])
        if snake[0][1] < 0:
            snake[0] = (snake[0][0],550)
            shadow_snake[0] = (shadow_snake[0][0],550)

        for pos in snake[1:]:
            if snake[0] == pos:
                direcao = PARADO
                stop = 1
                while stop:
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                        if event.type == KEYDOWN:
                            if event.key ==K_UP and direcao != BAIXO:
                                direcao = PARADO
                            if event.key ==K_DOWN and direcao != CIMA:
                                direcao = PARADO
                            if event.key ==K_LEFT and direcao != DIREITA:
                                direcao = PARADO
                            if event.key ==K_RIGHT and direcao != ESQUERDA:
                                direcao = PARADO
                    pygame.font.init()
                    IMAGE_GAMEOVER = pygame.image.load('gameover1.png')
                    IMAGE_GAMEOVER = pygame.transform.scale(IMAGE_GAMEOVER, (250,150))
                    rect = IMAGE_GAMEOVER.get_rect(center = (290, 250))
                    screen.blit(IMAGE_GAMEOVER,rect)
                    
                    restart = pygame.draw.rect(screen,(255,255,0), [100, 400, 100, 50] )
                    fonte_restart = pygame.font.SysFont(None, 25)
                    letra_restart = fonte_restart.render('Restart',True, (0,0,0))
                    screen.blit(letra_restart, (119, 415))

                    menu = pygame.draw.rect(screen,(255,255,0), [400, 400, 100, 50] )
                    fonte_menu = pygame.font.SysFont(None, 25)
                    letra_menu = fonte_menu.render('Menu',True, (0,0,0))
                    screen.blit(letra_menu, (430,415))
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            pygame.quit()
                        if event.type == MOUSEBUTTONDOWN:
                            x = pygame.mouse.get_pos()[0]
                            y = pygame.mouse.get_pos()[1]
                            if x > 100 and x < 200 and y > 400 and y < 450:
                                stop = 0
                                snake = [(200,200),
                                        (210,200)]
                                shadow_snake = [(200,200),
                                                (210,200)]
                                direcao = ESQUERDA
                                pygame.display.update()
                            if x > 400 and x < 500 and y > 400 and y < 450:
                                menu = 1
                                jogo = 0
                                stop = 0
                                snake = [(200,200),
                                        (210,200)]
                                shadow_snake = [(200,200),
                                                (210,200)]
                                direcao = ESQUERDA
                                pygame.display.update()
                    pygame.display.update()

        pygame.display.update()
    