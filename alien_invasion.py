import sys
import pygame

from settings import Settings
from ship import Ship


class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.settings = Settings()
        # esto sobra :   self.bg_color = (230,230,230)

        # no olvidar settings en self.settings.screen_width
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_height))
        pygame.display.set_caption("o titulo e ALIEN INVASION ")
        #o barco vai ao final
        self.ship = Ship(self) # no engadir second parameter
        

    def run_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()    
        pygame.display.flip()

if __name__ == '__main__':

    ai = AlienInvasion()
    # ai and ai_game ...are good friends , twins maybe
    ai.run_game()

