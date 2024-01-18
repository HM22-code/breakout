import pygame
import configs
from objects.ball import Ball
from objects.brick import Brick
from objects.paddle import Paddle

class Game():
    
    def __init__(self):
        # Init Pygame
        pygame.init()

        # Screen
        self.screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
        pygame.display.set_caption("Breakout")

        # Clock to control FPS
        self.clock = pygame.time.Clock()
        
        # Sprites group
        self.all_sprites = pygame.sprite.Group()
        self.all_bricks = pygame.sprite.Group()

        # Adding Paddle
        self.paddle = Paddle()
        self.all_sprites.add(self.paddle)

        # Adding Bricks
        row_number = 4
        column_number = 10
        space = 10
        for row in range(row_number):
            for column in range(column_number):
                brick = Brick(10, column, row, space)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)

        # Adding ball
        self.ball = Ball(self.paddle)
        self.all_sprites.add(self.ball)
    
    def print_text(self, text, x, y, size=36, color=configs.BLACK):
        font = pygame.font.SysFont(None, size)
        surface_text = font.render(text, True, color)
        rect = surface_text.get_rect()
        rect.center = (x, y)
        self.screen.blit(surface_text, rect)

    def run(self):
        # Game loop
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.all_sprites.update()

            # Collisions between ball and bricks
            collisions = pygame.sprite.spritecollide(self.ball, self.all_bricks, True)
            if collisions:
                self.ball.vy = -self.ball.vy

            # Check if ball is off screen
            if self.ball.rect.y > configs.SCREEN_HEIGHT:
                running = False

            self.screen.fill(configs.WHITE)
            self.all_sprites.draw(self.screen)

            # Print text if game over
            if not running:
                self.print_text("Game Over", configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2)

            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        quit()

if __name__ == "__main__":
    Game().run()
