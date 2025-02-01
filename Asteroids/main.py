
"""
Guia
Flechas izquierda o derecha para mover, espacio para disparar.

"""

import pygame
import sys
from pygame.locals import *
import jugador
import asteroide
from random import randint
import time

# Variables
ANCHO = 480
ALTO = 700
colorFuente = (120, 200, 40)

# Inicialización de Pygame
pygame.init()
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Meteoritos")

# Cargar recursos
fondo = pygame.image.load(("imagenes/fondo.png"))
pygame.mixer.music.load(("sonidos/fondo.wav"))
sonidoColision = pygame.mixer.Sound(("sonidos/colision.aiff"))
fuenteMarcador = pygame.font.SysFont("Arial", 10)
FuenteGameOver = pygame.font.SysFont("Arial", 40)
FuenteReiniciar = pygame.font.SysFont("Arial", 30)

# Función para cargar asteroides
def cargarAsteroides(x, y, listaAsteroide):
    meteoro = asteroide.Asteroide(x, y)
    listaAsteroide.append(meteoro)

# Función principal del juego
def meteoritos():
    nave = jugador.Nave()
    listaAsteroide = []
    puntos = 0
    jugando = True
    contador = 0
    pygame.mixer.music.play(3)

    while True:
        ventana.blit(fondo, (0, 0))
        nave.dibujar(ventana)
        tiempo = time.perf_counter()
        textoMarcador = fuenteMarcador.render(f"Puntos: {puntos}", 0, colorFuente)
        ventana.blit(textoMarcador, (10, 10))

        # Generación de asteroides
        if tiempo - contador > 1:
            contador = tiempo
            posX = randint(2, 478)
            cargarAsteroides(posX, 0, listaAsteroide)

        # Manejo de asteroides
        for x in listaAsteroide[:]:
            if jugando:
                x.dibujar(ventana)
                x.recorrido()
            if x.rect.top > ALTO:
                listaAsteroide.remove(x)
            elif x.rect.colliderect(nave.rect):
                listaAsteroide.remove(x)
                sonidoColision.play()
                nave.vida = False
                jugando = False

        # Disparos del jugador
        for x in nave.listaDisparo[:]:
            x.dibujar(ventana)
            x.recorrido()
            if x.rect.top < -10:
                nave.listaDisparo.remove(x)
            else:
                for meteorito in listaAsteroide[:]:
                    if x.rect.colliderect(meteorito.rect):
                        listaAsteroide.remove(meteorito)
                        nave.listaDisparo.remove(x)
                        puntos += 1

        nave.mover()

        # Movimiento del jugador y disparos
        teclas = pygame.key.get_pressed()
        if jugando:
            if teclas[K_LEFT]:
                nave.rect.left -= nave.velocidad
            elif teclas[K_RIGHT]:
                nave.rect.right += nave.velocidad
            #elif teclas[K_SPACE]:
            #    x, y = nave.rect.center
            #    nave.disparar(x, y)   #Disparos infinitos
       
        else:
            textoGameOver = FuenteGameOver.render("Game Over", 0, colorFuente)
            textoReiniciar = FuenteReiniciar.render("Reiniciar: Sí (Y) / No (N)", 0, colorFuente)
            ventana.blit(textoGameOver, (140, 300))
            ventana.blit(textoReiniciar, (100, 400))
            pygame.mixer.music.fadeout(3000)

            if teclas[K_y]:  # Si presiona 'Y'
                return  # Reinicia el juego volviendo a empezar el bucle principal
            elif teclas[K_n]:  # Si presiona 'N'
                pygame.quit()
                sys.exit()

        for evento in pygame.event.get():
            if evento.type == QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == KEYDOWN:
                if evento.key == K_SPACE:     #Disparo finito
                    x, y = nave.rect.center
                    nave.disparar(x, y)

        pygame.display.update()

# Bucle principal 
while True:
    meteoritos()
