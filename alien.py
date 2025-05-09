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
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """A class to manage alien enemies."""

    def __init__(self, fleet: 'AlienFleet', x: float, y:float):
        """Initialize alien object at ______ position."""
        super().__init__()

        # Grab some game data.
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings
        
        # Load and transform alien image for horizontal use.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_width, self.settings.alien_height)
            )
        self.image = pygame.transform.rotate(self.image, 90)

        # Create an alien rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float (self.rect.x)

    def update(self):
        """Update function handles alien movement."""

        temp_speed = self.settings.fleet_speed

        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self):
        """Determines if an alien is in contact with the upper or lower boundary of the screen."""

        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)

    def draw_alien(self):
        """Draws an alien to the screen."""
        
        self.screen.blit(self.image, self.rect)