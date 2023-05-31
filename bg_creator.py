# Scripts
from constants import *

# Modules
import pygame


class BGCreator:
    def __init__(self, img_path, vel_y):
        # Image
        self.scroll = 0
        self.image = pygame.image.load(img_path)
        self.bg_height = self.image.get_height()
        self.vel_y = vel_y

    def draw(self):
        # Show Background:
        SCREEN.blit(self.image, (0, -self.bg_height + self.scroll))  # Position 2
        SCREEN.blit(self.image, (0, self.scroll))  # Position 1
        # Scroll Movement Speed:
        self.scroll += self.vel_y

        # Reset Scroll:
        if self.scroll >= self.bg_height:
            self.scroll = 0

