import pygame
import sys
from pygame.locals import *
from random import randint

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((800, 800))

# Configurar la ventana
pygame.display.set_caption("Tigrillus - Juego en Python")
background = (255, 140, 70)
color_figure = (255, 255, 255)

# Variables
speed = 5
posX, posY = randint(10, 400), randint(10, 400)
use_keyboard = True  # Alternar entre controles de teclado y ratón

# Bucle principal
while True:
    # Rellenar la pantalla con el color de fondo
    ventana.fill(background)

    # Dibujar la figura
    pygame.draw.rect(ventana, color_figure, (posX, posY, 50, 50))

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        # Alternar entre teclado y ratón con "TAB"
        if evento.type == KEYDOWN and evento.key == K_TAB:
            use_keyboard = not use_keyboard

    # Controles con el teclado
    if use_keyboard:
        keys = pygame.key.get_pressed()
        if keys[K_LEFT]:
            posX -= speed
            if posX < 0:
                posX = 0
        if keys[K_RIGHT]:
            posX += speed
            if posX > (800 - 50):
                posX = 750
        if keys[K_UP]:
            posY -= speed
            if posY < 0:
                posY = 0
        if keys[K_DOWN]:
            posY += speed
            if posY > (800 - 50):
                posY = 750
    # Controles con el ratón
    else:
        posX, posY = pygame.mouse.get_pos()
        posX -= 25  # Ajustar para centrar la figura
        posY -= 25  # Ajustar para centrar la figura

        # Asegurar que la figura no salga de la pantalla
        posX = max(0, min(posX, 800 - 50))
        posY = max(0, min(posY, 800 - 50))

    # Actualizar la pantalla
    pygame.display.update()
