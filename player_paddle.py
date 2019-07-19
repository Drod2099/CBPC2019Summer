import pygame


class PlayerPad:
    def __init__(self, color, single, num):
        self.speed = 100
        self.move_down = False
        self.move_up = False
        self.color = color
        self.single = single
        self.player = num
        if self.player == 1:
            self.pos = [20, 250]
            self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
            self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)
        elif self.player == 2:
            self.pos = [760, 250]
            self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
            self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def update(self, dt):
        if self.move_down is True:
            self.pos[1] += self.speed * dt
            self.move_down = False
        elif self.move_up is True:
            self.pos[1] += -(self.speed * dt)
            self.move_up = False
        if self.pos[1] >= 500:
            self.pos[1] = 500
        elif self.pos[1] <= 70:
            self.pos[1] = 70
        self.hitbox1 = pygame.Rect(self.pos[0], self.pos[1], 20, 50)
        self.hitbox2 = pygame.Rect(self.pos[0], (self.pos[1] + 50), 20, 50)

    def input(self, keys):
        if self.single:
            if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                self.move_down = True
            if keys[pygame.K_w] or keys[pygame.K_UP]:
                self.move_up = True
        elif not self.single and self.player == 1:
            if keys[pygame.K_s]:
                self.move_down = True
            if keys[pygame.K_w]:
                self.move_up = True
        elif not self.single and self.player == 2:
            if keys[pygame.K_DOWN]:
                self.move_down = True
            if keys[pygame.K_UP]:
                self.move_up = True

    def draw(self, surf):
        pygame.draw.rect(surf, self.color, (self.pos[0], self.pos[1], 20, 100))
