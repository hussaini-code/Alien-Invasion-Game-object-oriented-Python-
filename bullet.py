import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """ A class for managing bullets"""

    def __init__(self, ai_game):
        """ Create a bullet object at ship's positon """
        
        super().__init__()
        self.screen = ai_game.screen 
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color
        
        # Create a bullet rect(0, 0) and then set on correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.midbottom = ai_game.ship.rect.midtop
        
        # Store the bulllet position as a float
        self.y = float(self.rect.y)

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """ Draw bullet to the screen """
        pygame.draw.rect(self.screen, self.color, self.rect)        