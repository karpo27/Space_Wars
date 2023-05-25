# Scripts:

# Modules:
import pygame


def set_bg_music(music, volume, loop):
    pygame.mixer.music.load(music)
    pygame.mixer.music.set_volume(volume)
    pygame.mixer.music.play(loop)
