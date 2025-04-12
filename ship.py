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

class Ship:
    """A class to manage the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Initialize the ship, set its starting position, create ship_rect, y value, and movement flags"""
        
        # Initialize ship class
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.screen_rect = game.screen.get_rect()

        # Set up ship image (Set at midleft of the screen, rotated 270 degrees)
        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.ship_width, self.settings.ship_height)
            )
        self.image = pygame.transform.rotate(self.image, 270)

        # Create ship rect
        self.rect = self.image.get_rect()
        self.rect.midleft = self.screen_rect.midleft

        # Store a float for the ship's exact vertical position.
        self.y = float(self.rect.y)

        # Movement flags; start with a ship that's not moving.
        self.moving_up = False
        self.moving_down = False

    def update(self):
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
        self.screen.blit(self.image, self.rect)