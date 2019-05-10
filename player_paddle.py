import pygame
import random


class PlayerPad:
    def __init__(self):
        self.pos = [20, 250]
        self.speed = 100
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 20, 100)
        self.move_down = False
        self.move_up = False

    def update(self, dt):
        if self.move_down is True:
            self.pos[1] += self.speed * dt
            self.move_down = False
        elif self.move_up is True:
            self.pos[1] += -(self.speed * dt)
            self.move_up = False

    def input(self, keys):
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move_down = True
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move_up = True

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 20, 100))
