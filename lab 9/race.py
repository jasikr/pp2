import pygame, sys
from pygame.locals import *
import random, time

# Initializing Pygame
pygame.init()

# Load sound effects
coin_sound = pygame.mixer.Sound("coin_sound.wav")

# Setting up FPS
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating color constants
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Game variables
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5  # Initial speed of enemies and coins
SCORE = 0  # Player's score
COINS_COLLECTED = 0  # Number of coins collected
COIN_THRESHOLD = 5  # Number of coins collected to increase enemy speed

# Setting up fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Load background image
background = pygame.image.load("AnimatedStreet.png")

# Create a white screen
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

class Enemy(pygame.sprite.Sprite):
    # Enemy sprite class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    # Player sprite class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        # Move the player based on key presses
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 10)
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-10, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(10, 0)

class Coin(pygame.sprite.Sprite):
    # Coin sprite class
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Coin.png")
        self.image = pygame.transform.scale(self.image, (48, 48))  # Resize coin image
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        # Move the coin down the screen
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Create player, enemy, and coin instances
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Create sprite groups
enemies = pygame.sprite.Group()
enemies.add(E1)
coins = pygame.sprite.Group()
coins.add(C1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, C1)

# Set up a timer event to increase speed
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Main game loop
while True:
    # Event handling loop
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5  # Increase speed over time
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Update game display
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_score = font_small.render(str(COINS_COLLECTED), True, BLACK)
    DISPLAYSURF.blit(coin_score, (SCREEN_WIDTH - 50, 10))

    # Move and redraw all sprites
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    # Check for collision between player and enemies
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()
        time.sleep(0.5)  # Wait for half a second

        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Remove all sprites
        time.sleep(2)
        pygame.quit()
        sys.exit()

    # Check for collision between player and coins
    if pygame.sprite.spritecollideany(P1, coins):
        COINS_COLLECTED += 1
        coin_sound.play()  # Play coin collection sound
        C1.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)  # Relocate coin

        # Increase enemy speed when COINS_COLLECTED reaches COIN_THRESHOLD
        if COINS_COLLECTED % COIN_THRESHOLD == 0:
            SPEED += 2  # Increment speed by 2

    pygame.display.update()  # Update the full display
    FramePerSec.tick(FPS)  # Maintain the specified FPS
