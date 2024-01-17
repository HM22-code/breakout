import pygame
import assets
from classes.state import State
from states.level import Level

class Level(State):
    
    def __init__(self, display, state_manager):
        self.display = display
        self.state_manager = state_manager
        
        # Sprite Groups
        
        # Create Game objects
        
        # Background music
        #self.music = assets.get_audio("start")
        #self.music.set_volume(0.3)
    
    def run(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            self.state_manager.set_state(self.state_manager.get_previous_state())
        
        #self.sprites.draw(self.display)
        #self.sprites.update()
        
    def enter_state(self):
        #self.music.play(loops = -1)
        pass
    
    def exit_state(self):
        #self.music.stop()
        pass