import pygame
from classes.state import State
from objects.text import Text
from states.level import Level

class Start(State):
    """ Start state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        Text("Press Enter to play",self.sprites)
    
    def run(self):
        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.game.set_state(Level(self.game))
        # Draw
        self.game.screen.fill((0,0,0))
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()