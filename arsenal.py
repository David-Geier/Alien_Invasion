"""
Class: Arsenal

Author: David Geier

Date: 04/15/25

Comments: Manages a sprite group of bullets
"""

import pygame
from bullet import Bullet
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Class for managing the arsenal of bullets."""

    def __init__(self, game: 'AlienInvasion'):
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self):
        self.arsenal.update()
        self._remove_bullets_offscreen()

    def _remove_bullets_offscreen(self):
        for bullet in self.arsenal.copy():
            if bullet.rect.left <= 0:
                self.arsenal.remove(bullet)

    def draw(self):
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self):
        if len(self.arsenal) < self.settings.bullets_allowed:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False