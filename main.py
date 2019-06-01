from player_paddle import *
from enemy_paddle import *
from puck import *
import random


# Pygame startup
pygame.display.init()
pygame.font.init()
pygame.mixer.init()
win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
font = pygame.font.SysFont("Times New Roman", 48)
clock = pygame.time.Clock()
done = False
start_screen = True
round_start = False
start_direction = "right"
round_count = 0
enemy_points = 0
player_points = 0
hit_timer = 0
start_img = pygame.image.load("PongStartScreen.png")
start_box = pygame.Rect(312, 348, 183, 74)
options_box = pygame.Rect(310, 438, 236, 66)
exit_box = pygame.Rect(311, 521, 141, 69)

player = PlayerPad()
enemy = EnemyPad()
puck = Puck(start_direction)

# GAME LOOP
while not done:
    # UPDATES
    deltaTime = clock.tick() / 1000.0
    hit_timer += deltaTime
    if not start_screen:
        hit_player = False
        hit_enemy = False
        if round_start is True:
            player.update(deltaTime)
            enemy.update(deltaTime, puck.pos)
        if round_start is True and round_count == 1:
            rand_dir = random.randint(1, 2)
            if rand_dir == 1:
                start_direction = "left"
            elif rand_dir == 2:
                start_direction = "right"
        if round_start is True:
            puck.update(deltaTime)

        # Collision Detection
        if hit_timer >= 1:
            hit_player = puck.collision(player)
            hit_enemy = puck.collision(enemy)
        if hit_player or hit_enemy:
            pygame.mixer.Sound("paddle-collision.wav").play()
            hit_timer = 0

        if puck.pos[0] < -5:
            enemy_points += 1
            round_start = False
            start_direction = "left"
            puck = None
            puck = Puck(start_direction)
        if puck.pos[0] > 805:
            player_points += 1
            round_start = False
            start_direction = "right"
            puck = None
            puck = Puck(start_direction)

        if round_start is False:
            player = None
            player = PlayerPad()
            enemy = None
            enemy = EnemyPad()

    # INPUT
    evt = pygame.event.poll()
    # ... event-handling
    if evt.type == pygame.QUIT:
        done = True
    elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and start_screen:
        mpos = pygame.mouse.get_pos()
        if start_box.collidepoint(mpos):
            start_screen = False
        elif options_box.collidepoint(mpos):
            start_screen = False
            options_screen = True
        elif exit_box.collidepoint(mpos):
            done = True

    # ... device-polling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True
    elif keys[pygame.K_SPACE] and not start_screen:
        round_start = True
        round_count += 1

    if not start_screen:
        player.input(keys)

    # DRAWING
    win.fill((0, 0, 0))
    if start_screen:
        win.blit(start_img, (0, 0))
    if not start_screen:
        if round_start is False:
            win.blit(font.render("Space to Start Round", True, (255, 0, 0)), (190, 100))
        pygame.draw.rect(win, (255, 255, 255), (0, 60, win_width, 10))
        pygame.draw.rect(win, (255, 255, 255), (395, 0, 10, 60))
        win.blit(font.render(str(player_points), True, (255, 255, 255)), (350, 7))
        win.blit(font.render(str(enemy_points), True, (255, 255, 255)), (425, 7))
        player.draw(win)
        enemy.draw(win)
        puck.draw(win)

    pygame.display.flip()

# Pygame shutdown
pygame.font.quit()
pygame.display.quit()
