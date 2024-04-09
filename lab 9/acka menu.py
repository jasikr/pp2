import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
W, H = 1200, 800
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Initialize screen and clock
screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
pygame.display.set_caption("Breakout Game")
clock = pygame.time.Clock()

# Paddle setup
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball setup
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Score setup
game_score = 0
score_font = pygame.font.SysFont('comicsansms', 40)

# Sound
collision_sound = pygame.mixer.Sound('catch.wav')  # Ensure this sound file is in your project directory

# Menu flags
main_menu_active = True
pause_menu_active = False
show_settings = False

# Settings
settings = {
    'paddle_speed': paddleSpeed,
    'ball_speed': ballSpeed,
    'unbreakable_blocks': True
}

# Blocks setup
block_list = [pygame.Rect(10 + 120 * i, 80 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
unbreakable_blocks = random.sample(block_list, random.randint(5, 15))
num_bonus_blocks = random.randint(3, 10)
bonus_blocks = random.sample([block for block in block_list if block not in unbreakable_blocks], num_bonus_blocks)

def draw_blocks():
    for block in block_list:
        if block in unbreakable_blocks and settings['unbreakable_blocks']:
            pygame.draw.rect(screen, WHITE, block)
        elif block in bonus_blocks:
            pygame.draw.rect(screen, YELLOW, block)  # Bonus blocks are yellow
        else:
            pygame.draw.rect(screen, GREEN, block)

def draw_paddle_and_ball():
    pygame.draw.rect(screen, WHITE, paddle)
    pygame.draw.circle(screen, RED, ball.center, ballRadius)

def show_score():
    score_text = score_font.render(f'Score: {game_score}', True, WHITE)
    score_rect = score_text.get_rect(center=(W // 2, 20))
    screen.blit(score_text, score_rect)

def handle_collision():
    global dx, dy, game_score
    # Ball collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dy *= -1
    # Ball collision with blocks
    for block in block_list[:]:
        if ball.colliderect(block):
            if block in unbreakable_blocks and settings['unbreakable_blocks']:
                dy *= -1
            else:
                block_list.remove(block)
                if block in bonus_blocks:
                    game_score += 5  # Increase game score for bonus block
                else:
                    game_score += 1  # Increase game score for regular block
                collision_sound.play()
                dy *= -1
                break

def reset_ball():
    global ball, dx, dy
    ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
    dx, dy = random.choice([-1, 1]), -1

def reset_game():
    global game_score, block_list, unbreakable_blocks, bonus_blocks
    game_score = 0
    block_list = [pygame.Rect(10 + 120 * i, 80 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
    unbreakable_blocks = random.sample(block_list, random.randint(5, 15))
    bonus_blocks = random.sample([block for block in block_list if block not in unbreakable_blocks], num_bonus_blocks)
    paddleSpeed = 20
    ballSpeed = 6
    paddle.width = paddleW
    reset_ball()

def draw_menu(menu_active, show_settings):
    if menu_active:
        # Menu Background
        menu_bg = pygame.Surface((W, H), pygame.SRCALPHA)
        menu_bg.fill((0, 0, 0, 128))
        screen.blit(menu_bg, (0, 0))

        # Title Font
        title_font = pygame.font.SysFont('comicsansms', 72)
        menu_font = pygame.font.SysFont('comicsansms', 50)

        # If not in settings, show the pause menu
        if not show_settings:
            title = title_font.render('PAUSED', True, WHITE)
            continue_text = menu_font.render('Press "P" to continue', True, WHITE)
            settings_text = menu_font.render('Press "S" for settings', True, WHITE)
            quit_text = menu_font.render('Press "ESC" to quit', True, WHITE)
            
            screen.blit(title, (W // 2 - title.get_width() // 2, H // 4))
            screen.blit(continue_text, (W // 2 - continue_text.get_width() // 2, H // 4 + 100))
            screen.blit(settings_text, (W // 2 - settings_text.get_width() // 2, H // 4 + 150))
            screen.blit(quit_text, (W // 2 - quit_text.get_width() // 2, H // 4 + 200))
        else:
            # If in settings, show the settings menu
            settings_title = title_font.render('SETTINGS', True, WHITE)
            paddle_speed_text = menu_font.render(f'Paddle Speed: {settings["paddle_speed"]}', True, WHITE)
            ball_speed_text = menu_font.render(f'Ball Speed: {settings["ball_speed"]}', True, WHITE)
            unbreakable_blocks_text = menu_font.render(f'Unbreakable Blocks: {"ON" if settings["unbreakable_blocks"] else "OFF"}', True, WHITE)
            return_text = menu_font.render('Press "R" to return', True, WHITE)
            
            screen.blit(settings_title, (W // 2 - settings_title.get_width() // 2, H // 4))
            screen.blit(paddle_speed_text, (W // 2 - paddle_speed_text.get_width() // 2, H // 4 + 100))
            screen.blit(ball_speed_text, (W // 2 - ball_speed_text.get_width() // 2, H // 4 + 150))
            screen.blit(unbreakable_blocks_text, (W // 2 - unbreakable_blocks_text.get_width() // 2, H // 4 + 200))
            screen.blit(return_text, (W // 2 - return_text.get_width() // 2, H // 4 + 250))

# Main menu before game starts
def handle_main_menu():
    global main_menu_active, pause_menu_active
    title_font = pygame.font.SysFont('comicsansms', 72)
    title = title_font.render('BREAKOUT GAME', True, WHITE)
    start_text = score_font.render('Press any key to start', True, WHITE)

    while main_menu_active:
        screen.fill(BLACK)
        screen.blit(title, (W // 2 - title.get_width() // 2, H // 2 - title.get_height() // 2 - 150))
        screen.blit(start_text, (W // 2 - start_text.get_width() // 2, H // 2 + 50))
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                main_menu_active = False
                pygame.quit()
                exit()
            if event.type == pygame.KEYDOWN:
                main_menu_active = False
                pause_menu_active = False

handle_main_menu()

# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p and not show_settings:
                pause_menu_active = not pause_menu_active
            if pause_menu_active and event.key == pygame.K_s:
                show_settings = True
            if show_settings and event.key == pygame.K_r:
                show_settings = False
            if event.key == pygame.K_ESCAPE:
                running = False
            # Settings adjustments
            if show_settings:
                if event.key == pygame.K_UP:
                    settings['paddle_speed'] += 1
                if event.key == pygame.K_DOWN:
                    settings['paddle_speed'] = max(1, settings['paddle_speed'] - 1)
                if event.key == pygame.K_LEFT:
                    settings['ball_speed'] = max(1, settings['ball_speed'] - 1)
                if event.key == pygame.K_RIGHT:
                    settings['ball_speed'] += 1
                if event.key == pygame.K_u:
                    settings['unbreakable_blocks'] = not settings['unbreakable_blocks']

    if pause_menu_active or show_settings:
        draw_menu(pause_menu_active, show_settings)
        pygame.display.flip()
        clock.tick(FPS)
        continue

    # Game logic
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= settings['paddle_speed']
    if keys[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += settings['paddle_speed']

    ball.x += dx * settings['ball_speed']
    ball.y += dy * settings['ball_speed']
    if ball.left <= 0 or ball.right >= W or ball.colliderect(paddle):
        dx = -dx
    if ball.top <= 0 or ball.bottom >= H:
        dy = -dy
    if ball.bottom > H:
        reset_game()

    handle_collision()

    # Draw everything
    screen.fill(BLACK)
    draw_blocks()
    draw_paddle_and_ball()
    show_score()

    # Refresh the screen
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
