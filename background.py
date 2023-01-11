# Scripts
from constants import *

# Modules
import pygame
from pygame import mixer

class Background:
    scroll = 0

    def __init__(self):
        self.space_bg = pygame.image.load(background_img['level_1'])
        self.bg_height = self.space_bg.get_height()
        mixer.music.load('Sounds/background.wav')
        mixer.music.play(-1)    # (-1) for playing on loop
        mixer.music.set_volume(0.0)

    def show(self):
        SCREEN.blit(self.space_bg, (0, -self.bg_height + Background.scroll))  # Position 2
        SCREEN.blit(self.space_bg, (0, Background.scroll))  # Position 1
        # Scroll Movement Speed
        Background.scroll += 0.8

        # Reset Scroll
        if Background.scroll >= self.bg_height:
            Background.scroll = 0
