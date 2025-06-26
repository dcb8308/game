import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:


    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        

        pygame.display.set_caption("Alien Invasion")

        self.ship = Ship(self)

        #set backround color#
        self.bg_color = (230, 230, 230)


    def run_game(self):
        while True:
             self.check_events()
             self.ship.update()
             self.update_screen()


    def _check_events(self):
         for event in pygame.event.get():
               if event.type == pygame.QUIT:
                  sys.exit()
            
                elif event.type == pygame.KEYDOWN:
                     self._check_keydown_events(event)
                elif event.type == pygame.KEYUP:
                     self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
                self.ship.moving_right = True
                self.ship.rect.x += 1
        elif  event.key == pygame.K_LEFT:
               self.ship.moving_left = True
        elif event.key == pygame.K_q:
             sys.exit()
             
            
             
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
                 self.ship.moving_left = False

            


    def _updatde_screen(self):

        self.screen.fill(self.bg_color)
        self.ship.blitme()

        pygame.display.flip()

        

    

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


