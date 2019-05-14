import pygame


class EnemyPad:
    def __init__(self):
        self.pos = [760, 250]
        self.speed = 100
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def update(self, dt, puck_pos):
        if puck_pos[1] > self.pos[1] + 50:
            self.pos[1] += (puck_pos[1] * (1 / self.speed) * dt)
        elif puck_pos[1] < self.pos[1] + 50:
            self.pos[1] -= (puck_pos[1] * (1 / self.speed) * dt)
        else:
            self.pos[1] = self.pos[1]
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def draw(self, surf):
        pygame.draw.rect(surf, (255, 255, 255), (self.pos[0], self.pos[1], 20, 100))
