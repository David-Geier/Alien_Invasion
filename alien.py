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

class Alien(Sprite):
    """A class to manage alien enemies."""

    def __init__(self, game: 'AlienInvasion', x: float, y:float):
        """Initialize alien object at ______ position."""
        super().__init__()

        # Grab some game data.
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.settings = game.settings
        
        # Load and transform alien image for horizontal use.
        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image,
            (self.settings.alien_width, self.settings.alien_height)
            )
        self.image = pygame.transform.rotate(self.image, 270)

        # Create an alien rect at (0, 0) and then set correct position.
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float (self.rect.x)

    def update(self):
        temp_speed = self.settings.fleet_speed

        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.x -= self.settings.fleet_drop_speed

        self.y += temp_speed * self.settings.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self):
        return (self.rect.bottom >= self.boundaries.bottom or self.rect.top <= self.boundaries.top)

    def draw_alien(self):
        self.screen.blit(self.image, self.rect)