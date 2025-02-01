import pygame
import sys
from pygame.locals import *
from random import randint


pygame.init()
ventana = pygame.display.set_mode((800, 800))

#Colores
pygame.display.set_caption("Tigrillus - Juego en Python")
background = (255,140,70)
color_figure = (255,255,255)

#Variables
speed = 0.3
direction = True
posX, posY = randint(10, 400), randint(10, 400)

while True:
     #Ventana
    ventana.fill(background)
    pygame.draw.rect(ventana, color_figure, (posX, posY, 50, 50))


   # Auto MoMovimiento
    if direction == True:
        if posX <= 800-50:       
            posX += speed
        else:
             direction = False
    else:
        if posX > 1:
            posX -= speed
        else:
            direction = True 


    #Actualizacion
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()