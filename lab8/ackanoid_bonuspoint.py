import pygame
import random

pygame.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 150
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('catch.wav')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    elif delta_x > delta_y:
        dy = -dy
    else:
        dx = -dx
    return dx, dy

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
num_unbreakable_blocks = random.randint(5, 15)
unbreakable_blocks = random.sample(block_list, num_unbreakable_blocks)
num_bonus_blocks = random.randint(3, 10)
bonus_blocks = random.sample([block for block in block_list if block not in unbreakable_blocks], num_bonus_blocks)

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Time variables
start_time = pygame.time.get_ticks()
ball_speed_increase_interval = 10000  # Increase ball speed every 10 seconds
paddle_shrink_interval = 15000  # Shrink paddle every 15 seconds

while not done:
    current_time = pygame.time.get_ticks()

    # Increase ball speed over time
    if current_time - start_time > ball_speed_increase_interval:
        ballSpeed += 1
        start_time = current_time

    # Shrink paddle over time
    if current_time - start_time > paddle_shrink_interval:
        paddleW = max(50, paddleW - 10)  # Minimum paddle width is 50
        paddle.width = paddleW
        start_time = current_time

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    # Drawing blocks
    for block in block_list:
        if block in unbreakable_blocks:
            pygame.draw.rect(screen, (255, 255, 255), block)  # Unbreakable blocks are white
        elif block in bonus_blocks:
            pygame.draw.rect(screen, (255, 255, 0), block)  # Bonus blocks are yellow
        else:
            pygame.draw.rect(screen, (0, 255, 0), block)  # Regular blocks are green

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Collision left/right
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius:
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision with blocks
    for block in block_list[:]:
        if ball.colliderect(block):
            if block in unbreakable_blocks:
                dx, dy = detect_collision(dx, dy, ball, block)
            else:
                block_list.remove(block)
                dx, dy = detect_collision(dx, dy, ball, block)
                game_score += 1
                collision_sound.play()
                if block in bonus_blocks:
                    game_score += 5  # Increase game score by 5 for hitting a bonus block

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not [block for block in block_list if block not in unbreakable_blocks]:  # Check if only unbreakable blocks are left
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    pygame.display.flip()
    clock.tick(FPS)
