import pygame
import sys
from time import sleep
from settings import Settings
from game_state import GameState
from ship import Ship
from bullet import Bullet
from alien import Alien

class BenTenInvasion:
    
    def __init__(self):
        """ Initialize game and create game resoureses """
        
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        
        # For making display
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        
        # for making game name
        pygame.display.set_caption("BenTenInvasion")

        # Create an instance to store game statistics
        self.stats = GameState(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        
        # Start AlienINvasion in an active state.
        self.game_active = True
    
    def run_game(self):
        """ Main loop for game """
        while True:
            """ Keyboard and mouse events """
            self._check_event()
            if self.game_active:
                self.ship.update()
                self.bullets.update()
                self._update_bullets()
                self._update_alien()        
            self._update_screen()
            self.clock.tick(60)
    
    def _create_fleet(self):
        """ Create the fleet of aleins"""
        # Make an alien
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        current_x, current_y = alien_width, alien_height 
        
        while current_y < (self.settings.screen_height - 4 * alien_width):
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += (1.5 * alien_width)
            # Finished a row; rsest x value and increment y value
            current_x = alien_width
            current_y += 1.5 * alien_height    
    
    def _ship_hit(self):
        """ Resspopning to the ship hit """
        if self.stats.ships_left > 0 :
            # decrement ship_left
            self.stats.ships_left -= 1
            
            #Get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            
            # Pause
            sleep(0.5)
        else:
            self.game_active = False    

    def _create_alien(self, x_position, y_position):
            """ Create an alien an place it in the row"""
            new_alien = Alien(self)
            new_alien.x = x_position
            new_alien.rect.x = x_position
            new_alien.rect.y = y_position
            self.aliens.add(new_alien)

    def _update_alien(self):
        """update the  position of all aliens in the fleet"""
        self._check_fleet_edges()
        self.aliens.update()
        # lok for alien ship collision
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
            print("Hit")
        # Look for aliens hitting the bottom of the screen    
        self._check_aliens_bottom()    

    def _check_fleet_edges(self):
        """ Responding appropritary if any alien have reached an egde""" 
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break

    def _check_aliens_bottom(self):
        """check if any aliens have reached the bottom of screen""" 
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= self.settings.screen_height:
                self._ship_hit()
                break       

    def _change_fleet_direction(self):
        """ resppon apporopriating if any aliens reached and edge """
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        self.settings.fleet_direction *= -1

    def _check_event(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    self._check_key_down(event)
                elif event.type == pygame.KEYUP:
                    self._check_key_up(event)
                    
    def _fire_bullet(self):
        """ Create a new bullet and add it to the bullet group """
        if len(self.bullets) < self.settings.bullets_allowed :
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """ Update positon of bullet and get rid of old bullets"""
        self.bullets.update() 

        # Get rid of bullet that have disappeared   
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)   
        print(len(self.bullets))
        self._check_bullet_alien_collision()
    
    def _check_bullet_alien_collision(self):
        """ Check any bullets that have hit alien"""
        # remove bullets an aliens that have collided
        collision = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if not self.aliens:
            #Destroy exiting bullets and create new fleet
            self.bullets.empty()
            self._create_fleet()

    
    def _update_screen(self):
        """ Updte images on screen, and flip to the new screen"""
        # screen color 
        self.screen.fill(self.settings.color) 
        
        
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.blitme()
        self.aliens.draw(self.screen)
        pygame.display.flip()

    def _check_key_down(self, event):
        """Respod to the key presses """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_UP:
            self.ship.moving_up = True

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True

        elif event.key == pygame.K_q:
            sys.exit()

        elif event.key == pygame.K_SPACE:
            self._fire_bullet()    
    
    def _check_key_up(self, event):
        """Respond to the key releases """
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

        elif event.key == pygame.K_UP:
            self.ship.moving_up = False 

        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False        
         


                         

if __name__ == "__main__":
    # Make game instance for running
    ai = BenTenInvasion()
    ai.run_game()                       