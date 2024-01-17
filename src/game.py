import pygame
import configs
from objects.ball import Ball
from objects.brick import Brick
from objects.paddle import Paddle

# Init Pygame
pygame.init()

# Screen
screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
pygame.display.set_caption("Breakout")

# Clock to control FPS
clock = pygame.time.Clock()

def print_text(text, x, y, size=36, color=configs.BLACK):
    font = pygame.font.SysFont(None, size)
    surface_text = font.render(text, True, color)
    rect = surface_text.get_rect()
    rect.center = (x, y)
    screen.blit(surface_text, rect)

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
        brick = Brick(10, column, row, space)
        all_sprites.add(brick)
        all_bricks.add(brick)

# Adding ball
ball = Ball(paddle)
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
    if ball.rect.y > configs.SCREEN_HEIGHT:
        running = False

    screen.fill(configs.WHITE)
    all_sprites.draw(screen)

    # Print text if game over
    if not running:
        print_text("Game Over", configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()