"""
Class: Ships and behavior

Author: David Geier

Comments: Swapped movement from left/right to up/down. Moved starting location to midleft of screen

Date: 3/30/2025
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal'):
        """Initialize the ship, set its starting position, create ship_rect, y value, and movement flags"""
        
        # Initialize ship class
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Set up ship image (Set at midleft of the screen, rotated 270 degrees)
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_height, self.settings.ship_width)
            )
        self.image = pygame.transform.rotate(self.image, 90)

        # Create ship rect
        self.rect = self.image.get_rect()
        self._center_ship()

        # Store a float for the ship's exact vertical position.

        # Movement flags; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False

        # Set up Arsenal
        self.arsenal = arsenal

    def _center_ship(self):
        self.rect.midright = self.screen_rect.midright
        self.y = float(self.rect.y)

    def update(self):
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Update the ship's position based on movement flags."""
        # Update the ship's y value, not the rect.
        if self.moving_up:
            self.y -= self.settings.ship_speed
        if self.moving_down:
            self.y += self.settings.ship_speed

        # Update rect object from self.y.
        self.rect.y = self.y

    def draw(self):
        """Draw a ship at its current location"""
        self.arsenal.draw()
        self.screen.blit(self.image, self.rect)

    def fire(self):
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group):
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        else:
            return False