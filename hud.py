"""
Class: hud

Author: David Geier

Date: 4/30/2025
"""

import pygame.font

class HUD:

    def __init__(self, game):
        """Initializes hud, updates scores, sets up life immage, updates level"""

        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = game.screen.get_rect()
        self.game_stats = game.game_stats
        self.font = pygame.font.Font(self.settings.font_file,
            self.settings.HUD_font_size)
        self.padding = 20
        self.update_scores()
        self._setup_life_image()
        self.update_level()

    def _setup_life_image(self):
        """Sets up life image"""

        self.life_image = pygame.image.load(self.settings.ship_file)
        self.life_image = pygame.transform.scale(self.life_image, (
            self.settings.ship_height, self.settings.ship_width
        ))
        self.life_rect = self.life_image.get_rect()

    def update_scores(self):
        """Delegates updates on score, max, and high"""

        self._update_score()
        self._update_max_score()
        self._update_high_score()

    def _update_score(self):
        """Updates the current score, defines location"""

        score_string = f'Score: {self.game_stats.score: ,.0f}'
        self.score_image = self.font.render(score_string, True,
            self.settings.text_color, None)
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.boundaries.right - self.padding
        self.score_rect.top = self.score_rect.bottom + self.padding
    
    def _update_max_score(self):
        """Updates the current max score, defines location"""

        max_score_string = f'Max-Score: {self.game_stats.max_score: ,.0f}'
        self.max_score_image = self.font.render(max_score_string, True,
            self.settings.text_color, None)
        self.max_score_rect = self.max_score_image.get_rect()
        self.max_score_rect.right = self.boundaries.right - self.padding
        self.max_score_rect.top = self.padding

    def _update_high_score(self):
        """Updates the current high score, defines location"""

        high_score_string = f'High-Score: {self.game_stats.high_score: ,.0f}'
        self.high_score_image = self.font.render(high_score_string, True,
            self.settings.text_color, None)
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.midtop = (self.boundaries.centerx, self.padding)

    def update_level(self):
        """Updates level, defines location"""

        level_string = f'Level: {self.game_stats.level: ,.0f}'
        self.level_image = self.font.render(level_string, True,
            self.settings.text_color, None)
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.padding
        self.level_rect.top = self.life_rect.bottom + self.padding

    def _draw_lives(self):
        """Draws lives in appropriate positions with padding"""

        current_x = self.padding
        current_y = self.padding
        for life in range(self.game_stats.ships_left):
            self.screen.blit(self.life_image, (current_x, current_y))
            current_x += self.life_rect.width + self.padding

    def draw(self):
        """Draws scores and delegates drawing lives"""
        
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.max_score_image, self.max_score_rect)
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self._draw_lives()