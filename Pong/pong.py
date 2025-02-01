import pygame
import sys
from paddle import Paddle  # Asegúrate de que paddle.py está en la misma carpeta
from ball import Ball

# Inicializar pygame
pygame.init()

# Definir colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Puntuaciones
score1 = 0
score2 = 0

# Cargar sonidos
poping = pygame.mixer.Sound('bounce.wav')
scoring = pygame.mixer.Sound('score.wav')

# Crear paddles
paddle1 = Paddle(WHITE, 10, 100)
paddle1.rect.x = 25
paddle1.rect.y = 250

paddle2 = Paddle(WHITE, 10, 100)
paddle2.rect.x = 765
paddle2.rect.y = 250

# Crear Bola
ball = Ball(WHITE, 20, 20)
ball.rect.x = 400
ball.rect.y = 200
ball.velocity = [5, 5]  # Asegurar que tenga velocidad inicial

# Velocidad de movimiento
VELOCITY = 15

# Configurar pantalla
SCREEN_SIZE = (800, 600)
game_display = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Pong")

# Grupo de sprites
sprites = pygame.sprite.Group()
sprites.add(paddle1)
sprites.add(paddle2)
sprites.add(ball)

# Variable de control del juego
clock = pygame.time.Clock()
playing = True

while playing:
    # Manejo de eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            playing = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_x:
                playing = False

    # Capturar teclas presionadas
    keys = pygame.key.get_pressed()

    # Movimiento Paddle 1 (Jugador 1)
    if keys[pygame.K_w]:
        paddle1.paddle_moving_up(VELOCITY)
    if keys[pygame.K_s]:
        paddle1.paddle_moving_down(VELOCITY)

    # Movimiento Paddle 2 (Jugador 2)
    if keys[pygame.K_UP]:
        paddle2.paddle_moving_up(VELOCITY)
    if keys[pygame.K_DOWN]:
        paddle2.paddle_moving_down(VELOCITY)

    # Limpiar pantalla
    game_display.fill(BLACK)

    # Dibujar línea de la mitad
    pygame.draw.line(game_display, WHITE, [400, 0], [400, 600], 5)

    # Dibujar paddles
    sprites.draw(game_display)
    sprites.update()

    # Mostrar puntuaciones
    font = pygame.font.Font(None, 100)
    text = font.render(str(score1), 1, WHITE)
    game_display.blit(text, (305, 10))

    text = font.render(str(score2), 1, WHITE)
    game_display.blit(text, (420, 10))

    # Colisiones con los bordes superiores e inferiores
    if ball.rect.y >= 580 or ball.rect.y <= 0:
        ball.velocity[1] = -ball.velocity[1]  # Rebote vertical

    # Golpe contra paddles
    if pygame.sprite.collide_mask(ball, paddle1) or pygame.sprite.collide_mask(ball, paddle2):
        ball.velocity[0] = -ball.velocity[0]  # Invertir dirección horizontal
        poping.play()

    # Puntos y reinicio de la pelota
    if ball.rect.x >= 780:
        score1 += 1
        scoring.play()
        ball.rect.x = 400
        ball.rect.y = 200
        ball.velocity = [-5, 5]  # Restablecer velocidad

    if ball.rect.x <= 2:
        score2 += 1
        scoring.play()
        ball.rect.x = 400
        ball.rect.y = 200
        ball.velocity = [5, 5]  # Restablecer velocidad

    # Mover la pelota
    ball.rect.x += ball.velocity[0]
    ball.rect.y += ball.velocity[1]

    # Actualizar pantalla
    pygame.display.flip()
    clock.tick(60)  # Limitar FPS a 60

# Cerrar pygame
pygame.quit()
sys.exit()
