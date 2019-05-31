import pygame
import random
from Vector import *


class Puck:
    def __init__(self, direction):
        self.pos = [395, 295]
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 10, 10)
        if direction == "left":
            self.dir = Vector(-400, 0)
        elif direction == "right":
            self.dir = Vector(400, 0)

    def update(self, dt):
        self.pos[0] += self.dir[0] * dt
        self.pos[1] += self.dir[1] * dt
        if self.pos[1] >= 590:
            self.pos[1] = 590
            self.dir[1] = self.dir[1] * -1
            pygame.mixer.Sound("paddle-collision.wav").play()
        elif self.pos[1] <= 70:
            self.pos[1] = 70
            self.dir[1] = self.dir[1] * -1
            pygame.mixer.Sound("paddle-collision.wav").play()
        self.hitbox = pygame.Rect(self.pos[0], self.pos[1], 10, 10)

    def collision(self, other):
        if self.hitbox.colliderect(other.hitbox1):
            self.dir[0] = self.dir[0] * -1
            self.dir[1] = 0
            y = random.randint(30, 60)
            self.dir[1] -= y
            return True
        elif self.hitbox.colliderect(other.hitbox2):
            self.dir[0] = self.dir[0] * -1
            self.dir[1] = 0
            y = random.randint(30, 60)
            self.dir[1] += y
            return True
        else:
            return False

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 10, 10))
