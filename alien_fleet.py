import pygame
from alien import Alien
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class AlienFleet:
    """Class to manage the fleet of aliens
    """

    def __init__(self, game: 'AlienInvasion'):
        """Initializes the fleet, generates a fleet of aliens for the game."""

        self.game = game
        self.settings = game.settings
        self.screen_width = self.settings.screen_width
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        # Generates fleet
        self.create_fleet()

    def create_fleet(self):
        """Delegates computations for fleet size, generates fleet based on that information"""

        alien_height = self.settings.alien_height
        alien_width = self.settings.alien_width
        screen_height = self.settings.screen_height
        screen_width = self.settings.screen_width

        fleet_height, fleet_width = self.calculate_fleet_size(alien_height, alien_width, screen_height, screen_width)
        y_offset, x_offset = self.calculate_offsets(alien_height, alien_width, screen_height, screen_width, fleet_height, fleet_width)

        self._create_rectangle_fleet(alien_height, alien_width, screen_width, fleet_height, fleet_width, y_offset, x_offset)

    def _create_rectangle_fleet(self, alien_height, alien_width, screen_width, fleet_height, fleet_width, y_offset, x_offset):
        """Creates rows and columns of aliens based on precalculated parameters"""

        for collumn in range(fleet_width):
            for row in range(fleet_height):
                current_y = alien_height * row + y_offset
                current_x = alien_width * collumn + x_offset
                if row % 2 == 0 or collumn % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_height, alien_width, screen_height, screen_width, fleet_height, fleet_width):
        """Determine x and y offsets for alien fleet"""

        fleet_vertical_space = fleet_height * alien_height
        fleet_horizontal_space = fleet_width * alien_width
        y_offset = int((screen_height - fleet_vertical_space) // 2)
        x_offset = 0
        return y_offset,x_offset

    def calculate_fleet_size(self, alien_height, alien_width, screen_height, screen_width):
        """Determine appropriate fleet size, and trim accordingly to add margins"""

        fleet_height = (screen_height // alien_height)
        fleet_width = ((screen_width / 2) // alien_width)
        
        if fleet_height % 2 == 0:
            fleet_height -= 1
        else:
            fleet_height -= 2

        if fleet_width % 2 == 0:
            fleet_width -= 1
        else:
            fleet_width -= 2

        return int(fleet_height), int(fleet_width)
        
    def _create_alien(self, current_y: int, current_x: int):
        """Creates a new alien at the current positions and adds it to the sprite group for the fleet."""

        new_alien = Alien(self, current_y, current_x)

        self.fleet.add(new_alien)

    def _check_fleet_edges(self):
        """Calls function to check the edges of an alien for each alien in the fleet. Drops fleet if it collides with the screen edge."""

        for alien in self.fleet:
            alien: Alien
            if alien.check_edges():
                self._drop_alien_fleet()
                self.fleet_direction *= -1
                break
        
    def _drop_alien_fleet(self):
        """Moves each alien in the fleet by the predetermined drop speed."""

        for alien in self.fleet:
            alien.x += self.fleet_drop_speed

    def update_fleet(self):
        """Calls for edge checking and updates fleet."""

        self._check_fleet_edges()
        self.fleet.update()

    def draw(self):
        """Iterates over sprite group and calls for it to be drawn."""

        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def print_fleet_size(self, fleet):
        """Debugging function to ensure duplicate fleets were not created #Depricated."""

        fleet_number = len(fleet)
        print(fleet_number)

    def check_collisions(self, other_group):
        """Checks collisions via use of group collide, removes both objects that are in collision when detected."""

        return pygame.sprite.groupcollide(self.fleet, other_group, True, True)
    
    def check_fleet_side(self):
        """Checks the sides of the fleet to ensure that they are within the boundaries."""

        alien: Alien
        for alien in self.fleet:
            if alien.rect.right > self.screen_width:
                return True
        return False
    
    def check_destroyed_status(self):
        """Determines whether or not the fleet has been destroyed. Returns True if destroyed."""

        return not self.fleet