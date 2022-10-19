import pygame, random, time
from pygame.locals import *
 
pygame.init()
screen = pygame.display.set_mode((600,600))
screen.fill((255,255,255))
pygame.display.set_caption('Snake')
clock = pygame.time.Clock()
stop = 0
snake = [(200,200),
        (210,200),
        (220,200),
        (230,200),
        (240,200),
        (250,200),
        (260,200),
        (270,200),
        (280,200)]
snake_skin = pygame.Surface((10,10))
snake_skin.fill((0,0,0))

apple = pygame.Surface((10,10))
apple.fill((255,0,0))
pos_apple = ((random.randint(0,590)//10)*10,(random.randint(0,590)//10)*10)

CIMA = 0
ESQUERDA = 1
DIREITA = 2
BAIXO = 3
PARADO = 4

direcao = ESQUERDA

while True:
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
    screen.fill((255,255,255))
    
    for i in range(len(snake)-1,0,-1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Direcionando a snake
    if direcao == CIMA:
        snake[0] = (snake[0][0], snake[0][1] - 10)
    if direcao == BAIXO:
        snake[0] = (snake[0][0], snake[0][1] + 10)
    if direcao == DIREITA:
        snake[0] = (snake[0][0] + 10, snake[0][1])
    if direcao == ESQUERDA:
        snake[0] = (snake[0][0] - 10, snake[0][1])
    if direcao == PARADO:
        snake[0] = (snake[0][0], snake[0][1])
    for pos in snake:
        screen.blit(snake_skin,pos)

    screen.blit(apple,pos_apple)

    if snake[0] == pos_apple:
        pos_apple = ((random.randint(0,590)//10)*10,(random.randint(0,590)//10)*10)
        snake.append((10,10))
    
    for pos in snake[1:]:
        if snake[0] == pos:
            direcao = PARADO
            for pos in snake:
                screen.blit(snake_skin,pos)

            for i in range(len(snake)-1,0,-1):
                snake[i] = (snake[i-1][0], snake[i-1][1])
            pygame.display.update()
            pygame.draw.rect(screen, (0,0,0), [200,190,200,100])
            pygame.display.update()
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
                font = pygame.font.SysFont(None, 10)
                texto = font.render('Gamer Over', True, (255,255,255))
                screen.blit(texto, (202,191))

    pygame.display.update()