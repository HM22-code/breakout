import pygame
import configs

class Brick(pygame.sprite.Sprite):
    """ Brick sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, column_number, column, row, space):
        super().__init__()
        self.image = pygame.Surface([configs.SCREEN_WIDTH // column_number - space, 20])
        self.image.fill(configs.BLUE)
        self.rect = self.image.get_rect()
        self.rect.x = column * (self.rect.width + space)
        self.rect.y = row * (self.rect.height + space) + 50
