import pygame
import random

# Init Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Screen parameters
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SIZE = 20
PADDLE_SIZE = (SCREEN_WIDTH // 6, 10)
PADDLE_SPEED = 8
BALL_SPEED = [7, 7]

# Screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

# Clock to control FPS
clock = pygame.time.Clock()

def print_text(text, x, y, size=36, color=WHITE):
    font = pygame.font.SysFont(None, size)
    surface_text = font.render(text, True, color)
    rect = surface_text.get_rect()
    rect.center = (x, y)
    screen.blit(surface_text, rect)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(PADDLE_SIZE)
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = (SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = SCREEN_HEIGHT - self.rect.height - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= PADDLE_SPEED
        if keys[pygame.K_RIGHT] and self.rect.x < SCREEN_WIDTH - self.rect.width:
            self.rect.x += PADDLE_SPEED

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([BALL_SIZE, BALL_SIZE])
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - BALL_SIZE)
        self.rect.y = SCREEN_HEIGHT - BALL_SIZE - PADDLE_SIZE[1]
        self.vx = BALL_SPEED[0]
        self.vy = -BALL_SPEED[1]

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

        if self.rect.x <= 0 or self.rect.x >= SCREEN_WIDTH - BALL_SIZE:
            self.vx = -self.vx
        if self.rect.y <= 0:
            self.vy = -self.vy
        if pygame.sprite.collide_rect(self, paddle):
            self.vy = -self.vy

# Sprites group
all_sprites = pygame.sprite.Group()
all_bricks = pygame.sprite.Group()

# Adding Paddle
paddle = Paddle()
all_sprites.add(paddle)

# Adding Bricks
row_number = 4
column_number = 10
space = 10
for row in range(row_number):
    for column in range(column_number):
        brick = pygame.sprite.Sprite()
        brick .image = pygame.Surface([SCREEN_WIDTH // column_number - space, 20])
        brick .image.fill(BLUE)
        brick .rect = brick.image.get_rect()
        brick .rect.x = column * (brick.rect.width + space)
        brick .rect.y = row * (brick.rect.height + space) + 50
        all_sprites.add(brick)
        all_bricks.add(brick)

# Adding ball
ball = Ball()
all_sprites.add(ball)

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    # Collisions between ball and bricks
    collisions = pygame.sprite.spritecollide(ball, all_bricks, True)
    if collisions:
        ball.vy = -ball.vy

    # Check if ball is off screen
    if ball.rect.y > SCREEN_HEIGHT:
        running = False

    screen.fill(WHITE)
    all_sprites.draw(screen)

    # Print text if game over
    if not running:
        print_text("Game Over", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()