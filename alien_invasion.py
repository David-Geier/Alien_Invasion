"""
Title: Alien Invaders

Author: David Geier

Comments: This is an Alien Invasion game with 1 player controlling a ship in one dimension, shooting in the second dimension.

          I Chose to go with option number 1; rotate the ship and place it at the left side of the screen
          To do this I modified each class to accomodate the new mechanics. I chose to change the input keys
          to use the up and down arrows for more intuitive movement, and renamed the movement methods to reflect
          the movement of the ship

Date: 3/30/2025
"""


import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init()
        self.settings = Settings()
     
        # Set up display window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption(self.settings.name)
      
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_width, self.settings.screen_height)
            )
        
        self.running = True
        self.clock = pygame.time.Clock()
      
        # Create rect for screen size
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        # Set up sounds.
        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        # Ship setup
        self.ship = Ship(self, Arsenal(self))
        
    def run_game(self):
        """Main game loop"""
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _update_screen(self):
        """Update images on screen, then flip to new screen."""
        self.screen.blit(self.bg, (0,0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit
                sys.exit
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit
            sys.exit()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()