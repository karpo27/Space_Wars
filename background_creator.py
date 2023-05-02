# Scripts
from constants import *

# Modules
import pygame


class BackgroundCreator:
    def __init__(self, background, vel_y):
        self.scroll = 0
        self.background = pygame.image.load(background)
        self.bg_height = self.background.get_height()
        self.vel_y = vel_y

        '''
        mixer.music.load('Sounds/background.wav')
        mixer.music.play(-1)    # (-1) for playing on loop
        mixer.music.set_volume(0.0)
        '''

    def show(self):
        SCREEN.blit(self.background, (0, -self.bg_height + self.scroll))  # Position 2
        SCREEN.blit(self.background, (0, self.scroll))  # Position 1
        # Scroll Movement Speed
        self.scroll += self.vel_y

        # Reset Scroll
        if self.scroll >= self.bg_height:
            self.scroll = 0


# Background Images
background_img = {
    'main_menu': 'Images/Main_Menu/main_menu_img.png',
    'level_1': 'Images/Levels_Background/space_bg.jpg'
}

# Initialize Classes:
background_lvl_1 = BackgroundCreator(background_img['level_1'], 0.8)
background_main_menu = BackgroundCreator(background_img['main_menu'], 0.45)

