import pygame


class EnemyPad:
    def __init__(self):
        self.pos = [760, 250]
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def update(self, dt):
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 20, 100))
