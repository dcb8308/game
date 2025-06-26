import sys
import pygame
from settings import Settings

class AlienInvasion:


    def __init__(self):
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height))
        

        pygame.display.set_caption("Alien Invasion")

        #set backround color#
        self.bg_color = (230, 230, 230)


    def run_game(self):

            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()

                self.screen.fill(self.bg_color)

                pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()


class Settings:

    def __init___(self):
         
         self.screenwidth = 1200
         self.screen_height = 800
         self.bg_color = (230, 230, 230)
