"""
Class: Settings

Author: David Geier

Comments: Swapped the height and width of bullets for horizontal behavior

Date: 3/30/2025
"""

from pathlib import Path

class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.name = 'Alien Invasion'
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_file = Path.cwd() / 'Assets' / 'Images' / 'Starbasesnow.png'
        self.FPS = 60


        # Ship settings
        self.ship_speed = 1.5
        self.ship_file = Path.cwd() / 'Assets' / 'Images' / 'ship2(no bg).png'
        self.ship_width = 40
        self.ship_height = 60

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 15
        self.bullet_height = 3
        self.bullet_color = (60,60,60)
        self.bullets_allowed = 3