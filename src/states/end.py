import pygame
import sys
from classes.state import State
from objects.text import Text

class End(State):
    """ End state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprite Groups
        self.sprites = pygame.sprite.LayeredUpdates()
        # Create Game objects
        Text("Game Over",self.sprites)
    
    def run(self):
        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.running = False
            pygame.quit()
            sys.exit()
        # Draw
        self.game.screen.fill((0,0,0))
        self.sprites.draw(self.game.screen)
        # Update
        self.sprites.update()