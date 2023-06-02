# Scripts:
from constants import *
from text_creator import TextCreator
from hud import score, HPBar

# Modules:
import pygame


class UI:
    def __init__(self, player):
        super().__init__()
        self.player = player

        # Score:
        self.score_pos = 1/43 * WIDTH + 55, 14/17 * HEIGHT + 22
        self.score_size = 26

        # Lives:
        self.image = player.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.6, self.image.get_height() * 0.6))
        self.rect = self.image.get_rect()
        self.rect.center = 1/43 * WIDTH, 15 / 17 * HEIGHT
        self.lives_pos = 1/43 * WIDTH + 58, 15 / 17 * HEIGHT + 22

        # Initialize Objects:
        self.hp_bar = HPBar(self.player)

    def show_lives(self):
        text_lives = TextCreator(0, f'x {str(self.player.lives)}', 'freesansbold.ttf', 26, 26, "white", None, self.lives_pos, "", 0)
        text_lives.render_text(-1)
        SCREEN.blit(self.image, self.rect.center)

    def draw(self):
        score.show_score(self.score_pos, self.score_size)
        self.hp_bar.show_bar()
        self.show_lives()
