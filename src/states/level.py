import pygame
import configs
from classes.state import State
from objects.ball import Ball
from objects.brick import Brick
from objects.paddle import Paddle
from states.end import End

class Level(State):
    """ Level state class

    Args:
        State (_type_): state
    """
    
    def __init__(self, game):
        super().__init__(game)
        # Sprites group
        self.all_sprites = pygame.sprite.Group()
        self.all_bricks = pygame.sprite.Group()
        # Adding Paddle
        self.paddle = Paddle()
        self.all_sprites.add(self.paddle)
        # Adding Bricks
        for row in range(4):
            for column in range(10):
                brick = Brick(10, column, row, 10)
                self.all_sprites.add(brick)
                self.all_bricks.add(brick)
        # Adding ball
        self.ball = Ball(self.paddle)
        self.all_sprites.add(self.ball)
    
    def run(self):
        # Input
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.game.set_state(self.game.get_previous_state())
        # Update
        self.all_sprites.update()
        # Collisions between ball and bricks
        collisions = pygame.sprite.spritecollide(self.ball, self.all_bricks, True)
        if collisions:
            self.ball.vy = -self.ball.vy
        # Check if ball is off screen
        if self.ball.rect.y > configs.SCREEN_HEIGHT:
            self.game.set_state(End(self.game))
        # Draw
        self.game.screen.fill(configs.WHITE)
        self.all_sprites.draw(self.game.screen)