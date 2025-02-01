import pygame
import sys
from pygame.locals import *


pygame.init()
ventana = pygame.display.set_mode((800, 800))

#Colores
pygame.display.set_caption("Tigrillus - Juego en Python")
background = (255,140,70)
line_color = (50, 50, 50)  # Gris espacial oscuro
figure_color = (255, 255, 255)  
circle_color = (255, 255, 0)  # Azul

while True:
    #Lineas
    ventana.fill(background)
    pygame.draw.line(ventana, line_color, (20,30), (150,100), 5)
    pygame.draw.line(ventana, line_color, (10,30), (150,100), 5)
    pygame.draw.line(ventana, line_color, (50,30), (150,100), 5)

    #Circulos
    pygame.draw.circle(ventana, circle_color, (100, 100), 50, 5)

    #Figuras
    pygame.draw.rect(ventana, figure_color, (700, 700, 500, 500), 500)
    pygame.draw.polygon(ventana, figure_color, ((146, 0), (291, 106), (236, 277), (56, 277), (0, 106)))

    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()