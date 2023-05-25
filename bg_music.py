# Scripts:

# Modules:
import pygame


def set_bg_music(music, volume, loop, fadeout_time=None):
    if fadeout_time is not None:
        pygame.mixer.music.fadeout(fadeout_time)
        pygame.mixer.music.queue(music, loops=loop)
        pygame.mixer.music.set_volume(volume)
    else:
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)
