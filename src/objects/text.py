import pygame.sprite
import configs
from layers import Layers

class Text(pygame.sprite.Sprite):
    """ Text sprite class

    Args:
        pygame (_type_): sprite
    """
    
    def __init__(self, text, *groups):
        super().__init__(*groups)
        self._layer = Layers.UI
        self.font = pygame.font.SysFont(None, 36)
        self.image = self.font.render(text, True, (255, 255, 255))
        self.rect = self.image.get_rect(center=(configs.SCREEN_WIDTH // 2, configs.SCREEN_HEIGHT // 2))