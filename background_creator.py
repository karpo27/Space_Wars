# Scripts
from constants import *

# Modules
import pygame


class BackgroundCreator:
    def __init__(self, background, vel_y):
        # Image
        self.scroll = 0
        self.background = pygame.image.load(background)
        self.bg_height = self.background.get_height()
        self.vel_y = vel_y

    def update(self):
        # Show Background:
        SCREEN.blit(self.background, (0, -self.bg_height + self.scroll))  # Position 2
        SCREEN.blit(self.background, (0, self.scroll))  # Position 1
        # Scroll Movement Speed:
        self.scroll += self.vel_y

        # Reset Scroll:
        if self.scroll >= self.bg_height:
            self.scroll = 0

