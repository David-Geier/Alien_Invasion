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
from bullet import Bullet

class AlienInvasion:
    """Overall class to manage game assets and behavior"""

    def __init__(self):
        """Initialize game, and create game resources"""
        pygame.init()
        self.settings = Settings()
        self.running = True
        self.clock = pygame.time.Clock()
     
        # Set up display window
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
            )
        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg,
            (self.settings.screen_width, self.settings.screen_height)
            )
        pygame.display.set_caption(self.settings.name)
        
        # Create rect for screen size
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height
        self.bullets = pygame.sprite.Group()

        # Ship setup
        self.ship = Ship(self)
        
    def run_game(self):
        """Main game loop"""
        while self.running:
            self._check_events()
            self.ship.update()
            self._update_bullets()
            self._update_screen()
            self.clock.tick(self.settings.FPS)

    def _check_events(self):
        """Respond to keypresses and mouse events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit
                pygame.quit
                self.running = False
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        """Respond to keypresses"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        """Respond to key releases"""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False
        
    def _fire_bullet(self):
        """Creates a new bullet and add it to the bullets group."""
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
    
    def _update_bullets(self):
        """Updates the position of bullets and gets rid of old bullets."""
        # Update bullet positions.
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if bullet.rect.right >= self.screen.get_width():
                self.bullets.remove(bullet)

    def _update_screen(self):
        """Update images on screen, then flip to new screen."""
        self.screen.blit(self.bg, (0,0))
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.ship.draw()

        pygame.display.flip()

if __name__ == '__main__':
    # Make a game instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()