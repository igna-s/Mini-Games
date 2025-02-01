import pygame
import sys
from pygame.locals import *
from random import randint

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((800, 800))

# Configurar la ventana
pygame.display.set_caption("Tigrillus - Python Game")
fondo = (255, 140, 70)
color_pared = (255, 255, 255)
color_objeto = (0, 0, 0)

# Variables
velocidad = 1
posX, posY = randint(10, 400), randint(10, 400)
posXw, posYw = randint(10, 750), randint(10, 750)
usar_teclado = True  # Alternar entre controles de teclado y ratón
colisiones = 0

# Bucle principal
while True:
    # Rellenar la pantalla con el color de fondo
    ventana.fill(fondo)

    # Dibujar los cuadrados
    cuadrado = pygame.draw.rect(ventana, color_objeto, (posX, posY, 50, 50))
    cuadrado_pared = pygame.draw.rect(ventana, color_pared, (posXw, posYw, 50, 50))

    # Detección de colisión
    if cuadrado.colliderect(cuadrado_pared):
        colisiones += 1
        print(f'¡Colisión número {colisiones}!')
        # Reposicionar el cuadrado blanco
        posXw, posYw = randint(0, 750), randint(0, 750)

    # Manejo de eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()
        # Alternar entre teclado y ratón con la tecla "TAB"
        if evento.type == KEYDOWN and evento.key == K_TAB:
            usar_teclado = not usar_teclado

    # Controles con teclado
    if usar_teclado:
        teclas = pygame.key.get_pressed()
        if teclas[K_LEFT]:
            posX -= velocidad
            if posX < 0:
                posX = 0
        if teclas[K_RIGHT]:
            posX += velocidad
            if posX > (800 - 50):
                posX = 750
        if teclas[K_UP]:
            posY -= velocidad
            if posY < 0:
                posY = 0
        if teclas[K_DOWN]:
            posY += velocidad
            if posY > (800 - 50):
                posY = 750
    # Controles con ratón
    else:
        posX, posY = pygame.mouse.get_pos()
        posX -= 25  # Ajustar para centrar la figura
        posY -= 25  # Ajustar para centrar la figura

        # Asegurar que la figura no se salga de la pantalla
        posX = max(0, min(posX, 800 - 50))
        posY = max(0, min(posY, 800 - 50))

    # Actualizar la pantalla
    pygame.display.update()
