import pygame
import configs
import random

class Ball(pygame.sprite.Sprite):
    """ Ball sprite class

    Args:
        pygame (_type_): sprite
    """
    
    ball_size = 20
    ball_speed = [7, 7]
    
    def __init__(self, paddle):
        super().__init__()
        self.image = pygame.Surface([self.ball_size, self.ball_size])
        self.image.fill(configs.RED)
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, configs.SCREEN_WIDTH - self.ball_size)
        self.rect.y = configs.SCREEN_HEIGHT - self.ball_size - (configs.SCREEN_WIDTH // 6)
        self.vx = self.ball_speed[0]
        self.vy = -self.ball_speed[1]
        self.paddle = paddle

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy
        if self.rect.x <= 0 or self.rect.x >= configs.SCREEN_WIDTH - self.ball_size:
            self.vx = -self.vx
        if self.rect.y <= 0:
            self.vy = -self.vy
        if pygame.sprite.collide_rect(self, self.paddle):
            self.vy = -self.vy
