import pygame

class Ship:
    """ A class for managing the ship """

    def __init__(self, ai_game):

        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        #Load image 
        self.image = pygame.image.load("images/cc.png")
        self.rect = self.image.get_rect()
        
        # loction of our ben
        self.rect.midbottom = self.screen_rect.midbottom
        
        # Store a float for the ship's exact horizantal position
        self.x = float(self.rect.x)
        
        # movement flag; start with a ship that's not moving
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
    
    def update(self):
        """ Update ship's positon based on movement"""
        if self.moving_right and self.rect.right < self.screen_rect.right :
            self.x += self.settings.ship_speed  
        if self.moving_left and self.rect.left > 0  :
            self.x -= self.settings.ship_speed 
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.ship_speed 
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.ship_speed        
        self.rect.x = self.x 
               
    def blitme(self):
        """ Draw the ship and set it's starting position """
        self.screen.blit(self.image, self.rect)    
    
    def center_ship(self):
        """ Center the ship on the screen """
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)