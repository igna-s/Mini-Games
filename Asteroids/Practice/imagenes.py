import pygame
import sys
from pygame.locals import *
from random import randint

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((800, 400))

# Imágenes
imagen = pygame.image.load("Practice/imagen/images.jpg")  # "Ubico en Asteroids el workspace
imagenes = pygame.image.load("Practice/imagen/descarga.jpg")

# Redimensionar imágenes
tamaño_imagen = (400, 400)  # Mitad del tamaño de la ventana
imagen = pygame.transform.scale(imagen, tamaño_imagen)
imagenes = pygame.transform.scale(imagenes, tamaño_imagen)

# Colores
pygame.display.set_caption("Tigrillus - Juego en Python")
background = (255, 140, 70)

# Bucle principal
while True:
    # Pantalla
    ventana.fill(background)
    ventana.blit(imagen, (0, 0))
    ventana.blit(imagenes, (400, 0))

    # Eventos
    for evento in pygame.event.get():
        if evento.type == QUIT:
            pygame.quit()
            sys.exit()

    # Ruido blanco
    for i in range(4):
        posX, posY = randint(0, 800), randint(0, 800)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        pygame.draw.rect(ventana, color, (posX, posY, 25, 25))

    # Actualizar pantalla
    pygame.display.update()
