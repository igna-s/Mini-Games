import pygame
from random import randint, choice

black = (0, 0, 0)  #Global

class Ball(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        # Crear la superficie del paddle
        self.image = pygame.Surface([width, height])
        self.image.fill(black)
        self.image.set_colorkey(black)

        # Dibujar el paddle en la superficie
        pygame.draw.rect(self.image, color, [0, 0, width, height])

        self.velocity = [randint(10,15),randint(15,20)]

        # Obtener el rectángulo del paddle
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += self.velocity[0]
        self.rect.y +=self.velocity[1]

    def bouncing(self):
        self.velocity[0] =- self.velocity[0]
        self.velocity[1] = -self.velocity[1]
        # Variar levemente la dirección para evitar rebotes repetitivos
        self.velocity[0] += choice([-7, -4, 0, 4, 7])  # Pequeño cambio en X
        self.velocity[1] += choice([-7, -4, 0, 4, 7])  # Pequeño cambio en Y

        # Asegurar que la velocidad no se vuelva demasiado lenta o rápida
        self.velocity[0] = max(min(self.velocity[0], 15), -15)
        self.velocity[1] = max(min(self.velocity[1], 20), -20)