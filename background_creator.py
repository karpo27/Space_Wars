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


# Background Assets: Image, Scroll, Music
background_assets = {
    'main_menu': ['Images/Main_Menu/main_menu_img.png', 0.45, 'Sounds/main_menu_music.mp3'],
    'level_1': ['Images/Levels_Background/space_bg.jpg', 0.8, 'Sounds/background.wav']
}

# Initialize Classes:
background_main_menu = BackgroundCreator(*background_assets['main_menu'])
background_lvl_1 = BackgroundCreator(*background_assets['level_1'])

