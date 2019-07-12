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
game_font = pygame.font.SysFont("Bauhaus 93", 48)
options_font = pygame.font.SysFont("Bauhaus 93", 72)
clock = pygame.time.Clock()

done = False
start_screen = False
round_start = False
win_screen = False
lose_screen = False
options_screen = True

start_direction = "right"

WHT = (255, 255, 255)
GREY = (100, 100, 100)

dif = "Medium"
max_score = 11
color_inversion = "Off"

round_count = 0
enemy_points = 0
player_points = 0
hit_timer = 0

start_img = pygame.image.load("PongStartScreen.png")
lose_img = pygame.image.load("PongLoseScreen.png")
win_img = pygame.image.load("PongWinScreen.png")

start_box = pygame.Rect(312, 348, 183, 74)
options_box = pygame.Rect(310, 438, 236, 66)
exit_box = pygame.Rect(311, 521, 141, 69)

restart_box = pygame.Rect(305, 380, 180, 65)
main_menu_box = pygame.Rect(260, 465, 280, 65)

dif_easy_box = pygame.Rect(295, 155, 105, 55)
dif_medium_box = pygame.Rect(445, 155, 180, 55)
dif_hard_box = pygame.Rect(670, 155, 110, 55)
color_inv_on_box = pygame.Rect(395, 415, 75, 50)
color_inv_off_box = pygame.Rect(545, 415, 85, 50)
eleven_score_box = pygame.Rect(495, 285, 65, 50)
seven_score_box = pygame.Rect(395, 285, 40, 50)
fifteen_score_box = pygame.Rect(620, 285, 65, 50)
back_box = pygame.Rect(345, 525, 120, 50)

player = PlayerPad()
enemy = EnemyPad()
puck = Puck(start_direction)

# GAME LOOP
while not done:
    # UPDATES
    deltaTime = clock.tick() / 1000.0
    hit_timer += deltaTime
    if not start_screen or not win_screen or not lose_screen or not options_screen:
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

        # Win-Lose Check
        if enemy_points == max_score:
            lose_screen = True
            enemy_points = 0
            player_points = 0
        elif player_points == max_score:
            win_screen = True
            enemy_points = 0
            player_points = 0

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
    elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and (win_screen or lose_screen):
        mpos = pygame.mouse.get_pos()
        if restart_box.collidepoint(mpos):
            win_screen = False
            lose_screen = False
        if main_menu_box.collidepoint(mpos):
            start_screen = True
    elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and options_screen:
        mpos = pygame.mouse.get_pos()
        if dif_easy_box.collidepoint(mpos):
            dif = "Easy"
        if dif_medium_box.collidepoint(mpos):
            dif = "Medium"
        if dif_hard_box.collidepoint(mpos):
            dif = "Hard"

        if color_inv_on_box.collidepoint(mpos):
            color_inversion = "On"
        if color_inv_off_box.collidepoint(mpos):
            color_inversion = "Off"

        if eleven_score_box.collidepoint(mpos):
            max_score = 11
        if seven_score_box.collidepoint(mpos):
            max_score = 7
        if fifteen_score_box.collidepoint(mpos):
            max_score = 15

        if back_box.collidepoint(mpos):
            options_screen = False
            start_screen = True

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
    elif lose_screen:
        win.blit(lose_img, (0, 0))
    elif win_screen:
        win.blit(win_img, (0, 0))
    elif options_screen:
        win.blit(options_font.render("Options", True, WHT), (275, 15))
        win.blit(game_font.render("Difficulty:", True, WHT), (10, 150))
        win.blit(game_font.render("Winning Score:", True, WHT), (10, 280))
        win.blit(game_font.render("Color Inversion:", True, WHT), (10, 410))
        win.blit(game_font.render("Back", True, WHT), (350, 520))

        if dif == "Easy":
            win.blit(game_font.render("Easy", True, WHT), (300, 150))
            win.blit(game_font.render("Medium", True, GREY), (450, 150))
            win.blit(game_font.render("Hard", True, GREY), (675, 150))

        elif dif == "Medium":
            win.blit(game_font.render("Easy", True, GREY), (300, 150))
            win.blit(game_font.render("Medium", True, WHT), (450, 150))
            win.blit(game_font.render("Hard", True, GREY), (675, 150))

        elif dif == "Hard":
            win.blit(game_font.render("Easy", True, GREY), (300, 150))
            win.blit(game_font.render("Medium", True, GREY), (450, 150))
            win.blit(game_font.render("Hard", True, WHT), (675, 150))

        if max_score == 7:
            win.blit(game_font.render("7", True, WHT), (400, 280))
            win.blit(game_font.render("11", True, GREY), (500, 280))
            win.blit(game_font.render("15", True, GREY), (625, 280))

        elif max_score == 11:
            win.blit(game_font.render("7", True, GREY), (400, 280))
            win.blit(game_font.render("11", True, WHT), (500, 280))
            win.blit(game_font.render("15", True, GREY), (625, 280))

        elif max_score == 15:
            win.blit(game_font.render("7", True, GREY), (400, 280))
            win.blit(game_font.render("11", True, GREY), (500, 280))
            win.blit(game_font.render("15", True, WHT), (625, 280))

        if color_inversion == "On":
            win.blit(game_font.render("On", True, WHT), (400, 410))
            win.blit(game_font.render("Off", True, GREY), (550, 410))

        elif color_inversion == "Off":
            win.blit(game_font.render("On", True, GREY), (400, 410))
            win.blit(game_font.render("Off", True, WHT), (550, 410))

        # Test
        pygame.draw.rect(win, WHT, dif_easy_box, 1)
        pygame.draw.rect(win, WHT, dif_medium_box, 1)
        pygame.draw.rect(win, WHT, dif_hard_box, 1)
        pygame.draw.rect(win, WHT, color_inv_on_box, 1)
        pygame.draw.rect(win, WHT, color_inv_off_box, 1)
        pygame.draw.rect(win, WHT, eleven_score_box, 1)
        pygame.draw.rect(win, WHT, seven_score_box, 1)
        pygame.draw.rect(win, WHT, fifteen_score_box, 1)
        pygame.draw.rect(win, WHT, back_box, 1)

    elif not start_screen:
        if round_start is False:
            win.blit(game_font.render("Space to Start Round", True, (255, 0, 0)), (190, 100))
        pygame.draw.rect(win, (255, 255, 255), (0, 60, win_width, 10))
        pygame.draw.rect(win, (255, 255, 255), (395, 0, 10, 60))
        win.blit(game_font.render(str(player_points), True, (255, 255, 255)), (345, 7))
        win.blit(game_font.render(str(enemy_points), True, (255, 255, 255)), (425, 7))
        player.draw(win)
        enemy.draw(win)
        puck.draw(win)

    pygame.display.flip()

# Pygame shutdown
pygame.font.quit()
pygame.display.quit()
