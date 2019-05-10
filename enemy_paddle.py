import pygame
import random


class EnemyPad:
    def __init__(self):
        self.pos = [760, 250]
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 20, 100)

    def update(self, dt):
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 20, 100)

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 20, 100))
