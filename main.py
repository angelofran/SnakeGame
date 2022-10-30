from random import randint
import pygame as pg
from pygame.locals import *


def pos_apple():
    x = randint(0, 590)
    y = randint(0, 590)
    return (x//10 * 10, y//10 * 10) 

def colisão(c1, c2):
    return (c1[0] == c2[0]) and (c1[1] == c2[1])


UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

# Dando início a janela, do aplicativo
pg.init()

#Tamanho da tela
screen = pg.display.set_mode((600, 600))

#Título da tela
title = pg.display.set_caption('Snake Game')

#ícone da tela
icon = pg.image.load("icone_app(2).jpg")
pg.display.set_icon(icon)

# Definido as posições que serão ocupadas
snake = [(200, 200),(210, 200),(220,200)]

#A cobra começará por se mover a esquerda
my_direction = LEFT

#Fazendo a cobra
snake_skin = pg.Surface((10, 10))

#Dando cor a cobra
snake_skin.fill((0, 128, 0))

#Definindo a posição da maça
apple_pos = pos_apple()

#Fazendo a maça
apple = pg.Surface((10, 10))

#Dando cor a maçã
apple.fill((255, 255, 0))

#Definindo o clock para controlar a velocidade da cobra
clock = pg.time.Clock()

#Texto


#Toda lógica do jogo fica dentro de um loop infinito
while True:
    pontos = 0
    #Dfinindo um fps de 20
    clock.tick(15) #Velocidade da cobra.
    
    #Para cada evento em eventos
    for event in pg.event.get():
        #Se algum evento for do tipo QUIT
        if event.type == QUIT:
            #Feche a janela
            pg.quit()

    # Quando as teclas forem precionadas, haverá alteração da posicão da cobra.
    if event.type == KEYDOWN:
        if event.key == K_UP:
            my_direction = UP

        if event.key == K_DOWN:
            my_direction = DOWN

        if event.key == K_RIGHT:
            my_direction = RIGHT

        if event.key == K_LEFT:
            my_direction = LEFT

    if colisão(snake[0], apple_pos):
        apple_pos = pos_apple()
        snake.append((0, 0))
        pontos += 1

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    #Traçando toda linha de movimentos da cobra
    if my_direction == UP:
        snake[0] = (snake[0][0],snake[0][1] - 10)
    if my_direction == DOWN:
        snake[0] = (snake[0][0],snake[0][1] + 10)
    if my_direction == RIGHT:
        snake[0] = (snake[0][0] + 10,snake[0][1])
    if my_direction == LEFT:
        snake[0] = (snake[0][0] - 10,snake[0][1])

    # Colocando a apple na tela
    screen.fill((0, 0, 0))
    screen.blit(apple, apple_pos)
    
    #Colocando a snake na tela
    for pos in snake:
        screen.blit(snake_skin, pos)

    pg.display.update()

