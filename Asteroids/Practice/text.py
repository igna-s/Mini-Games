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
color_wall = (255, 255, 255)
color_object = (0, 0, 0)

# Variables
speed = 1
posX, posY = randint(10, 400), randint(10, 400)
posXw, posYw = randint(10, 750), randint(10, 750)
use_keyboard = True  # Alternar entre controles de teclado y ratón

# Variables de texto
text_color = (50, 50, 50)
type = pygame.font.SysFont("Arial", 20)
fuente = pygame.font.SysFont("Impact", 20)
cant = 0

# Función para actualizar la pantalla
def refresh():
    ventana.fill(background)
    # Actualizar el texto de colisiones
    cadena = f"Presiona TAB para alternar entre teclado y ratón, Colisiones: {cant}"
    text = type.render(cadena, True, text_color)  # Renderizar el texto con las colisiones actualizadas
    ventana.blit(text, (10, 10))  # Dibujar el texto actualizado
    time = fuente.render("Tiempo: " + str(pygame.time.get_ticks() / 1000), True, text_color)
    ventana.blit(time, (650, 10))  # Dibujar el texto del tiempo

# Bucle principal
while True:
    # Llenar la pantalla con el color de fondo
    refresh()

    # Dibujar los cuadrados
    square = pygame.draw.rect(ventana, color_object, (posX, posY, 50, 50))
    square_wall = pygame.draw.rect(ventana, color_wall, (posXw, posYw, 50, 50))

    # Detección de colisión
    if square.colliderect(square_wall):
        cant += 1
        # Reposicionar el cuadrado blanco
        posXw, posYw = randint(0, 750), randint(0, 750)
        # Actualizar el texto de colisiones
        refresh()

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
