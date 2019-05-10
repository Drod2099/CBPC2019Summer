import pygame
import random
import math
from player_paddle import *
from enemy_paddle import *
from puck import *


# Pygame startup
pygame.display.init()
pygame.font.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
font = pygame.font.SysFont("Times New Roman", 22)
clock = pygame.time.Clock()
done = False
round_start = False
start_direction = "right"
round_count = 0

player = PlayerPad()
enemy = EnemyPad()
puck = Puck(start_direction)

# GAME LOOP
while not done:
    # UPDATES
    deltaTime = clock.tick() / 1000.0
    hit_player = False
    hit_enemy = False
    player.update(deltaTime)
    enemy.update(deltaTime)
    if round_start is True and round_count == 1:
        rand_dir = random.randint(1, 2)
        if rand_dir == 1:
            start_direction = "left"
        elif rand_dir == 2:
            start_direction = "right"
    if round_start is True:
        puck.update(deltaTime)

    # Collision Detection
    if puck.collision(player):
        hit_player = True
    elif puck.collision(enemy):
        hit_enemy = True

    # INPUT
    evt = pygame.event.poll()
    # ... event-handling
    if evt.type == pygame.QUIT:
        done = True

    # ... device-polling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    elif keys[pygame.K_SPACE]:
        round_start = True
        round_count += 1

    player.input(keys)

    # DRAWING
    win.fill((0, 0, 0))
    player.draw(win)
    enemy.draw(win)
    puck.draw(win)
    pygame.display.flip()

# Pygame shutdown
pygame.font.quit()
pygame.display.quit()
