class Settings :

    def __init__(self):
        # Screen Settings
        self.screen_width = 600
        self.screen_height = 800
        self.color = (246, 246, 246)


        #ship settings
        self.ship_speed = 5.1
        self.ship_limit = 3

        #Bullet Settings
        self.bullet_speed = 8.0 
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (244, 0, 45)
        self.bullets_allowed = 90

        # Alien setting
        self.alien_speed = 3.0
        self.fleet_drop_speed = 4
        self.fleet_direction = 1
        
