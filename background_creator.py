# Scripts
from constants import *

# Modules
import pygame
from pygame import mixer


class BackgroundCreator:
    def __init__(self, background, vel_y, music):
        # Image
        self.scroll = 0
        self.background = pygame.image.load(background)
        self.bg_height = self.background.get_height()
        self.vel_y = vel_y

        # Music:
        mixer.init()
        self.music = pygame.mixer.Sound(music)

    def update(self):
        '''
        # Start Music:
        self.music.play(-1)
        self.music.set_volume(0.01)
        '''

        # Show Background:
        SCREEN.blit(self.background, (0, -self.bg_height + self.scroll))  # Position 2
        SCREEN.blit(self.background, (0, self.scroll))  # Position 1
        # Scroll Movement Speed:
        self.scroll += self.vel_y

        # Reset Scroll:
        if self.scroll >= self.bg_height:
            self.scroll = 0

