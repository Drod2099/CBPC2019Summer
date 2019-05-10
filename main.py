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

player = PlayerPad()
enemy = EnemyPad()
puck = Puck()

# GAME LOOP
while not done:
    # UPDATES
    deltaTime = clock.tick() / 1000.0
    player.update(deltaTime)
    enemy.update(deltaTime)
    puck.update(deltaTime)

    # INPUT
    evt = pygame.event.poll()
    # ... event-handling
    if evt.type == pygame.QUIT:
        done = True

    # ... device-polling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True

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
