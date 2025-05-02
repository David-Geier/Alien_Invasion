"""
Class: game_stats

Author: David Geier

Date: 4/30/2025

Comments: Manages stats for the game to be pulled by the HUD and alien_invasion

"""

from typing import TYPE_CHECKING
from pathlib import Path
import json

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion


class GameStats():

    def __init__(self, game: 'AlienInvasion'):
        """Initializes game stats, delegates initializing saved scores and reseting stats"""

        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats() 

    def init_saved_scores(self):
        """Accesses scores.json file and loads contents if it exists. Otherwise, high score is 0"""

        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.high_score = scores.get('high_score', 0)
        else:
            self.high_score = 0
            self.save_scores()

    def save_scores(self):
        """Creates scores and dumps to json file"""

        scores = {
            'high_score' : self.high_score
        }
        contents = json.dumps(scores, indent=4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f'File Not Found: {e}')

    def reset_stats(self):
        """Resets remaining ships, current score, and level"""

        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions):
        """Delegates score updates based on collisions"""

        # update score
        self._update_score(collisions)
        # update max score
        self._update_max_score() 
        # update high score
        self._update_high_score()

    def _update_max_score(self):
        """Changes max score if current score is higher"""

        if self.score > self.max_score:
            self.max_score = self.score

    def _update_high_score(self):
        """Changes high score if current max score is higher"""

        if self.score > self.high_score:
            self.high_score = self.score
 
    def _update_score(self, collisions):
        """Iterates over collisions and increments score"""

        for alien in collisions.values():
            self.score += self.settings.alien_points

    def update_level(self):
        """Does this \/"""
        
        self.level += 1