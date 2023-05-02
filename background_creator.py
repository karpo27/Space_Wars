# Scripts
from constants import *

# Modules
from pygame import *


class BackgroundCreator:
    def __init__(self, background, vel_y, music):
        # Image
        self.scroll = 0
        self.background = pygame.image.load(background)
        self.bg_height = self.background.get_height()
        self.vel_y = vel_y

        # Music:
        mixer.init()
        mixer.music.load(music)
        mixer.music.set_volume(0.4)

    def show(self):
        # Start Music if it's not already playing:
        if not mixer.music.get_busy():
            mixer.music.play(-1)  # (-1) for playing on loop

        # Show Background:
        SCREEN.blit(self.background, (0, -self.bg_height + self.scroll))  # Position 2
        SCREEN.blit(self.background, (0, self.scroll))  # Position 1
        # Scroll Movement Speed:
        self.scroll += self.vel_y

        # Reset Scroll:
        if self.scroll >= self.bg_height:
            self.scroll = 0


# Background Images
background_img = {
    'main_menu': 'Images/Main_Menu/main_menu_img.png',
    'level_1': 'Images/Levels_Background/space_bg.jpg'
}

# Initialize Classes:
background_lvl_1 = BackgroundCreator(background_img['level_1'], 0.8, 'Sounds/background.wav')
background_main_menu = BackgroundCreator(background_img['main_menu'], 0.45, 'Sounds/main_menu_music.mp3')

