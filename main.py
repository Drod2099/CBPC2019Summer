from player_paddle import *
from enemy_paddle import *
from puck import *
import random
import platform
import os


# Pygame startup
pygame.display.init()
pygame.font.init()
pygame.mixer.init()

win_width = 800
win_height = 600
win = pygame.display.set_mode((win_width, win_height))
clock = pygame.time.Clock()

# Platform
windows = platform.release()
username = os.getenv('username')

# Fonts
if windows == "10":
    if os.path.isfile('C:\\Users\\' + username + '\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93_0.ttf'):
        controls_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93_0.ttf", 24)
        game_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93_0.ttf", 48)
        options_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93_0.ttf", 72)
        end_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93_0.ttf", 190)
        title_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93_0.ttf", 230)

    elif os.path.isfile('C:\\Users\\' + username + '\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93.ttf'):
        controls_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93.ttf", 24)
        game_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93.ttf", 48)
        options_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93.ttf", 72)
        end_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93.ttf", 190)
        title_font = pygame.font.Font("C:\\Users\\" + username + "\\AppData\\Local\\Microsoft\\Windows\\Fonts\\BAUHS93.ttf", 230)
elif windows == "7":
    controls_font = pygame.font.Font("C:\\Windows\\Fonts\\BAUHS93_0.ttf", 24)
    game_font = pygame.font.Font("C:\\Windows\\Fonts\\BAUHS93_0.ttf", 48)
    options_font = pygame.font.Font("C:\\Windows\\Fonts\\BAUHS93_0.ttf", 72)
    end_font = pygame.font.Font("C:\\Windows\\Fonts\\BAUHS93_0.ttf", 190)
    title_font = pygame.font.Font("C:\\Windows\\Fonts\\BAUHS93_0.ttf", 230)

# Booleans
done = False
start_screen = True
round_start = False
win_screen = False
win_screen_1 = False
win_screen_2 = False
lose_screen = False
options_screen = False
single = True

start_direction = "right"

# Colors
WHT = (255, 255, 255)
GREY = (150, 150, 150)
BLK = (0, 0, 0)
color1 = WHT
color2 = BLK

# Options settings
dif = "Medium"
max_score = 11
color_inversion = "Off"

# Counters
round_count = 0
enemy_points = 0
player_points = 0
hit_timer = 0

# Main Menu Hitboxes
one_box = pygame.Rect(275, 240, 280, 90)
two_box = pygame.Rect(270, 335, 280, 74)
options_box = pygame.Rect(276, 420, 260, 72)
exit_box = pygame.Rect(335, 503, 141, 69)

# Win/Lose Hitboxes
restart_box = pygame.Rect(295, 380, 235, 70)
main_menu_box = pygame.Rect(225, 470, 365, 70)

# Options Hitboxes
dif_easy_box = pygame.Rect(295, 155, 105, 55)
dif_medium_box = pygame.Rect(445, 155, 180, 55)
dif_hard_box = pygame.Rect(670, 155, 110, 55)
color_inv_on_box = pygame.Rect(395, 415, 75, 50)
color_inv_off_box = pygame.Rect(545, 415, 85, 50)
eleven_score_box = pygame.Rect(495, 285, 65, 50)
seven_score_box = pygame.Rect(395, 285, 40, 50)
fifteen_score_box = pygame.Rect(620, 285, 65, 50)
back_box = pygame.Rect(345, 525, 120, 50)

# Class initialization
player = PlayerPad(color1, single, 1)
enemy = EnemyPad(dif, color1)
player_two = PlayerPad(color1, single, 2)

# GAME LOOP
while not done:
    # UPDATES
    deltaTime = clock.tick() / 1000.0
    hit_timer += deltaTime

    # In-game creation and updates
    if not start_screen or not win_screen or not lose_screen or not options_screen:
        hit_player = False
        hit_enemy = False
        if round_start is False and single:
            player = PlayerPad(color1, single, 1)
            enemy = EnemyPad(dif, color1)
            puck = Puck(start_direction, color1)
        elif round_start is False and not single:
            player = PlayerPad(color1, single, 1)
            player_two = PlayerPad(color1, single, 2)
            puck = Puck(start_direction, color1)
        if round_start is True and single:
            player.update(deltaTime)
            enemy.update(deltaTime, puck.pos)
        elif round_start is True and not single:
            player.update(deltaTime)
            player_two.update(deltaTime)
        if round_start is True and round_count == 1:
            rand_dir = random.randint(1, 2)
            if rand_dir == 1:
                start_direction = "left"
            elif rand_dir == 2:
                start_direction = "right"
        if round_start is True:
            puck.update(deltaTime)

        # Win-Lose Check
        if enemy_points == max_score and single:
            lose_screen = True
            enemy_points = 0
            player_points = 0
        elif enemy_points == max_score and not single:
            win_screen_2 = True
            enemy_points = 0
            player_points = 0
        elif player_points == max_score and single:
            win_screen = True
            enemy_points = 0
            player_points = 0
        elif player_points == max_score and not single:
            win_screen_1 = True
            enemy_points = 0
            player_points = 0

        # Collision Detection
        if hit_timer >= 1 and single:
            hit_player = puck.collision(player)
            hit_enemy = puck.collision(enemy)
        elif hit_timer >= 1 and not single:
            hit_player = puck.collision(player)
            hit_enemy = puck.collision(player_two)
        if hit_player or hit_enemy and not (start_screen or options_screen or win_screen or win_screen_1 or win_screen_2 or lose_screen):
            pygame.mixer.Sound("paddle-collision.wav").play()
            hit_timer = 0

        # Score detection
        if puck.pos[0] < -5:
            enemy_points += 1
            round_start = False
            start_direction = "left"
            puck = Puck(start_direction, color1)
        if puck.pos[0] > 805:
            player_points += 1
            round_start = False
            start_direction = "right"
            puck = Puck(start_direction, color1)

        # After-score Reset
        if round_start is False and single:
            player = PlayerPad(color1, single, 1)
            enemy = EnemyPad(dif, color1)
        elif round_start is False and not single:
            player = PlayerPad(color1, single, 1)
            player_two = PlayerPad(color1, single, 2)

    # INPUT
    evt = pygame.event.poll()
    # ... event-handling
    if evt.type == pygame.QUIT:
        done = True

    # Main Menu selections
    elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and start_screen:
        mpos = pygame.mouse.get_pos()
        if one_box.collidepoint(mpos[0], mpos[1]):
            start_screen = False
            single = True
        elif two_box.collidepoint(mpos[0], mpos[1]):
            start_screen = False
            single = False
        elif options_box.collidepoint(mpos[0], mpos[1]):
            start_screen = False
            options_screen = True
        elif exit_box.collidepoint(mpos[0], mpos[1]):
            done = True

    # Win/Lose selections
    elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and (win_screen or win_screen_1 or win_screen_2 or lose_screen):
        mpos = pygame.mouse.get_pos()
        if restart_box.collidepoint(mpos[0], mpos[1]):
            win_screen = False
            win_screen_1 = False
            win_screen_2 = False
            lose_screen = False
        if main_menu_box.collidepoint(mpos[0], mpos[1]):
            start_screen = True
            win_screen = False
            win_screen_1 = False
            win_screen_2 = False
            lose_screen = False

    # Options selections
    elif evt.type == pygame.MOUSEBUTTONDOWN and evt.button == 1 and options_screen:
        mpos = pygame.mouse.get_pos()

        # Difficulty selection
        if dif_easy_box.collidepoint(mpos[0], mpos[1]):
            dif = "Easy"
        if dif_medium_box.collidepoint(mpos[0], mpos[1]):
            dif = "Medium"
        if dif_hard_box.collidepoint(mpos[0], mpos[1]):
            dif = "Hard"

        # Color inversion selection
        if color_inv_on_box.collidepoint(mpos[0], mpos[1]):
            color_inversion = "On"
            color = BLK
            color1 = BLK
            color2 = WHT
        if color_inv_off_box.collidepoint(mpos[0], mpos[1]):
            color_inversion = "Off"
            color = WHT
            color1 = WHT
            color2 = BLK

        # Score selection
        if eleven_score_box.collidepoint(mpos[0], mpos[1]):
            max_score = 11
        if seven_score_box.collidepoint(mpos[0], mpos[1]):
            max_score = 7
        if fifteen_score_box.collidepoint(mpos[0], mpos[1]):
            max_score = 15

        # Back button
        if back_box.collidepoint(mpos[0], mpos[1]):
            options_screen = False
            start_screen = True

    # ... device-polling
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        done = True

    # Round start key
    elif keys[pygame.K_SPACE] and not (start_screen or options_screen or win_screen or win_screen_1 or win_screen_2 or lose_screen):
        round_start = True
        round_count += 1

    # Player input
    if not start_screen and round_start and single:
        player.input(keys)
    elif not start_screen and round_start and not single:
        player.input(keys)
        player_two.input(keys)

    # DRAWING
    win.fill(color2)

    # Main Menu drawing
    if start_screen:
        win.blit(title_font.render("Pong", True, color1), (160, -25))
        win.blit(options_font.render("1-Player", True, color1), (275, 240))
        win.blit(options_font.render("2-Player", True, color1), (275, 325))
        win.blit(options_font.render("Options", True, color1), (281, 410))
        win.blit(options_font.render("Exit", True, color1), (345, 495))

    # Lose Screen drawing
    elif lose_screen:
        win.blit(end_font.render("You", True, color1), (50, 0))
        win.blit(end_font.render("Lose!", True, color1), (350, 150))
        win.blit(options_font.render("Restart", True, color1), (300, 375))
        win.blit(options_font.render("Main Menu", True, color1), (230, 465))

    # Single Win Screen Drawing
    elif win_screen:
        win.blit(end_font.render("You", True, color1), (50, 0))
        win.blit(end_font.render("Win!", True, color1), (350, 150))
        win.blit(options_font.render("Restart", True, color1), (300, 375))
        win.blit(options_font.render("Main Menu", True, color1), (230, 465))

    # Player 1 Win Screen Drawing
    elif win_screen_1:
        win.blit(end_font.render("Player 1", True, color1), (65, -20))
        win.blit(end_font.render("Wins!", True, color1), (200, 185))
        win.blit(options_font.render("Restart", True, color1), (300, 375))
        win.blit(options_font.render("Main Menu", True, color1), (230, 465))

    # Player 2 Win Screen Drawing
    elif win_screen_2:
        win.blit(end_font.render("Player 2", True, color1), (65, -20))
        win.blit(end_font.render("Wins!", True, color1), (200, 185))
        win.blit(options_font.render("Restart", True, color1), (300, 375))
        win.blit(options_font.render("Main Menu", True, color1), (230, 465))

    # Options Screen Drawing
    elif options_screen:
        win.blit(options_font.render("Options", True, color1), (275, 15))
        win.blit(game_font.render("Difficulty:", True, color1), (10, 150))
        win.blit(game_font.render("Winning Score:", True, color1), (10, 280))
        win.blit(game_font.render("Color Inversion:", True, color1), (10, 410))
        win.blit(game_font.render("Back", True, color1), (350, 520))

        if dif == "Easy":
            win.blit(game_font.render("Easy", True, color1), (300, 150))
            win.blit(game_font.render("Medium", True, GREY), (450, 150))
            win.blit(game_font.render("Hard", True, GREY), (675, 150))

        elif dif == "Medium":
            win.blit(game_font.render("Easy", True, GREY), (300, 150))
            win.blit(game_font.render("Medium", True, color1), (450, 150))
            win.blit(game_font.render("Hard", True, GREY), (675, 150))

        elif dif == "Hard":
            win.blit(game_font.render("Easy", True, GREY), (300, 150))
            win.blit(game_font.render("Medium", True, GREY), (450, 150))
            win.blit(game_font.render("Hard", True, color1), (675, 150))

        if max_score == 7:
            win.blit(game_font.render("7", True, color1), (400, 280))
            win.blit(game_font.render("11", True, GREY), (500, 280))
            win.blit(game_font.render("15", True, GREY), (625, 280))

        elif max_score == 11:
            win.blit(game_font.render("7", True, GREY), (400, 280))
            win.blit(game_font.render("11", True, color1), (500, 280))
            win.blit(game_font.render("15", True, GREY), (625, 280))

        elif max_score == 15:
            win.blit(game_font.render("7", True, GREY), (400, 280))
            win.blit(game_font.render("11", True, GREY), (500, 280))
            win.blit(game_font.render("15", True, color1), (625, 280))

        if color_inversion == "On":
            win.blit(game_font.render("On", True, color1), (400, 410))
            win.blit(game_font.render("Off", True, GREY), (550, 410))

        elif color_inversion == "Off":
            win.blit(game_font.render("On", True, GREY), (400, 410))
            win.blit(game_font.render("Off", True, color1), (550, 410))

    # Single In-Game Drawing
    elif not start_screen and single:
        if round_start is False:
            win.blit(game_font.render("Space to Start Round", True, (255, 0, 0)), (190, 100))
            win.blit(controls_font.render("Up = W or Up-Arrow", True, color1), (300, 250))
            win.blit(controls_font.render("Down = S or Down-Arrow", True, color1), (275, 310))
        pygame.draw.rect(win, color1, (0, 60, win_width, 10))
        pygame.draw.rect(win, color1, (395, 0, 10, 60))
        win.blit(game_font.render(str(player_points), True, color1), (345, 7))
        win.blit(game_font.render(str(enemy_points), True, color1), (425, 7))
        player.draw(win)
        enemy.draw(win)
        puck.draw(win)

    # Multi In-Game Drawing
    elif not start_screen and not single:
        if round_start is False:
            win.blit(game_font.render("Space to Start Round", True, (255, 0, 0)), (190, 100))
            win.blit(controls_font.render("1st: Up = W, Down = S", True, color1), (285, 250))
            win.blit(controls_font.render("2nd: Up = Up-Arrow, Down = Down-Arrow", True, color1), (190, 310))
        pygame.draw.rect(win, color1, (0, 60, win_width, 10))
        pygame.draw.rect(win, color1, (395, 0, 10, 60))
        win.blit(game_font.render(str(player_points), True, color1), (345, 7))
        win.blit(game_font.render(str(enemy_points), True, color1), (425, 7))
        player.draw(win)
        player_two.draw(win)
        puck.draw(win)

    pygame.display.flip()

# Pygame shutdown
pygame.font.quit()
pygame.display.quit()
