import pygame


class EnemyPad:
    def __init__(self, dif, color):
        self.pos = [760, 250]
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)
        if dif == "Easy":
            self.speed = 15
        elif dif == "Medium":
            self.speed = 10
        elif dif == "Hard":
            self.speed = 7
        self.color = color

    def update(self, dt, puck_pos):
        if puck_pos[1] > self.pos[1] + 50:
            self.pos[1] += (puck_pos[1] * (1 / self.speed) * dt)
        elif puck_pos[1] < self.pos[1] + 50:
            self.pos[1] -= (puck_pos[1] * (1 / self.speed) * dt)
        else:
            self.pos[1] = self.pos[1]
        if self.pos[1] >= 500:
            self.pos[1] = 500
        elif self.pos[1] <= 70:
            self.pos[1] = 70
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (self.pos[0], self.pos[1], 20, 100))
