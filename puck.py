import pygame
import random
from Vector import *


class Puck:
    def __init__(self):
        self.pos = [395, 295]
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 10, 10)
        self.dir = Vector(0, 0)

    def update(self, dt):
        pass

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 10, 10))
