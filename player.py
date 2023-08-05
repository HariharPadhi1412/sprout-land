import pygame
from setting import *


class Player(pygame.sprite.Sprite):

    def __init__(self, pos, group):
        super().__init__(group)

        self.image = pygame.Surface((64, 32))
        self.image.fill('green')
        self.rect = self.image.get_rect(center=pos)

        # directions
        self.directions = pygame.math.Vector2()
        self.pos = pygame.math.Vector2(self.rect.center)
        self.speed = 200

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_UP]:
            self.directions.y = -1
        elif keys[pygame.K_DOWN]:
            self.directions.y = 1
        else:
            self.directions.y = 0

        if keys[pygame.K_RIGHT]:
            self.directions.x = 1
        elif keys[pygame.K_LEFT]:
            self.directions.x = -1
        else:
            self.directions.x = 0


    def move(self, dt):

        # normalizing the vector
        if self.directions.magnitude() > 0:
            self.directions = self.directions.normalize()

        # horizontal movement
        self.pos.x += self.directions.x * self.speed * dt
        self.rect.centerx = self.pos.x

        # vertical movement
        self.pos.y += self.directions.y * self.speed * dt
        self.rect.centery = self.pos.y


    def update(self, dt):
        self.input()
        self.move(dt)
