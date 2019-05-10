import pygame
import random
from Vector import *


class Puck:
    def __init__(self, direction):
        self.pos = [395, 295]
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 10, 10)
        if direction == "left":
            self.dir = Vector(-100, 0)
        elif direction == "right":
            self.dir = Vector(100, 0)

    def update(self, dt):
        self.pos[0] += self.dir[0] * dt
        self.pos[1] += self.dir[1] * dt
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 10, 10)

    def collision(self, other):
        if self.hitbox.colliderect(other.hitbox):
            self.dir[0] = self.dir[0] * -1
            return True

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 10, 10))
