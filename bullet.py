"""
Class: Bullet

Author: David Geier

Comments: Changed bullet direction and starting location

Date: 3/30/2025
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """A class to manage bullets fired from the ship."""

    def __init__(self, game: 'AlienInvasion'):
        """Create a bullet object at the ship's current position."""
        super().__init__()

        # Grab some game data.
        self.screen = game.screen
        self.settings = game.settings
        
        # Load and transform bullet image for horizontal use.
        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.bullet_width, self.settings.bullet_height)
            )
        self.image = pygame.transform.rotate(self.image, 270)

        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright

        # Store the bullet's position as a float.
        self.x = float (self.rect.x)

    def update(self):
        """Move the bullets up the screen"""
        # Update the exact position of the bullet.
        self.x += self.settings.bullet_speed
        # Update the rect position.
        self.rect.x = self.x

    def draw_bullet(self):
        """Draw the bullets to the screen."""
        self.screen.blit(self.image, self.rect)