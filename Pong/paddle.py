import pygame
import pygame

black = (0, 0, 0)  #Global

class Paddle(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Crear la superficie del paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Dibujar el paddle en la superficie
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        # Obtener el rectángulo del paddle
        self.rect = self.image.get_rect()

    def paddle_moving_up(self, velocity):
        """Mueve el paddle hacia arriba"""
        self.rect.y -= velocity
        if self.rect.y < 0:
            self.rect.y = 0

    def paddle_moving_down(self, velocity):
        """Mueve el paddle hacia abajo"""
        self.rect.y += velocity
        if self.rect.y > 480:   #600 screen - 100 paddle
            self.rect.y = 480
