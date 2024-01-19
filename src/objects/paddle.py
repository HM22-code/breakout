import pygame
import configs

class Paddle(pygame.sprite.Sprite):
    """ Paddle sprite class

    Args:
        pygame (_type_): sprite
    """
    
    paddle_size = (configs.SCREEN_WIDTH // 6, 10)
    paddle_speed = 8
    
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface(self.paddle_size)
        self.image.fill(configs.GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = (configs.SCREEN_WIDTH - self.rect.width) // 2
        self.rect.y = configs.SCREEN_HEIGHT - self.rect.height - 10

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.paddle_speed
        if keys[pygame.K_RIGHT] and self.rect.x < configs.SCREEN_WIDTH - self.rect.width:
            self.rect.x += self.paddle_speed