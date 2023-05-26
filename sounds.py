# Scripts:
from constants import *

# Modules:
import pygame
pygame.mixer.init()

class Sound:
    def __init__(self, path, initial_volume):
        self.sound = pygame.mixer.Sound(f'Sounds/{path}')
        self.initial_volume = initial_volume
        self.new_volume = initial_volume
        self.scale_volume = 5

    def update_volume(self, new_volume):
        self.new_volume = self.initial_volume * new_volume / self.scale_volume

    def play(self):
        self.sound.play().set_volume(self.new_volume)


def set_bg_music(music, volume, loop, fadeout_time=None):
    if fadeout_time is not None:
        pygame.mixer.music.fadeout(fadeout_time)
        pygame.mixer.music.queue(music, loops=loop)
        pygame.mixer.music.set_volume(volume)
    else:
        pygame.mixer.music.load(music)
        pygame.mixer.music.set_volume(volume)
        pygame.mixer.music.play(loop)


# Initialize Objects:
menu_movement = Sound(*SOUNDS['menu_movement'])
menu_selection = Sound(*SOUNDS['menu_selection'])
menu_back = Sound(*SOUNDS['menu_back'])
player_laser = Sound(*SOUNDS['player_laser'])
player_hit = Sound(*SOUNDS['player_hit'])
player_explosion = Sound(*SOUNDS['player_explosion'])
enemy_laser = Sound(*SOUNDS['enemy_laser'])
enemy_hit = Sound(*SOUNDS['enemy_hit'])
enemy_explosion = Sound(*SOUNDS['enemy_explosion'])
boss_laser = Sound(*SOUNDS['boss_laser'])
boss_explosion = Sound(*SOUNDS['boss_explosion'])
win_fireworks = Sound(*SOUNDS['win_fireworks'])

sounds_list = [menu_movement, menu_selection, menu_back, player_laser, player_hit, player_explosion, enemy_laser,
               enemy_hit, enemy_explosion, boss_laser, boss_explosion, win_fireworks]


