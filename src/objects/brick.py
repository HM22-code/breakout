import pygame
import configs

class Brick(pygame.sprite.Sprite):
    
    paddle_size = (configs.SCREEN_WIDTH // 6, 10)
    paddle_speed = 8
    
    def __init__(self, column_number, column, row, space):
        super().__init__()
        self.image = pygame.Surface([configs.SCREEN_WIDTH // column_number - space, 20])
        self.image.fill(configs.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = column * (self.rect.width + space)
        self.rect.y = row * (self.rect.height + space) + 50
