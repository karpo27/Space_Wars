# Scripts:
from constants import *

# Modules:
import pygame


class Sounds:
    def __init__(self, path, initial_volume):
        self.sound = pygame.mixer.Sound(f'Sounds/{path}')
        self.initial_volume = initial_volume
        self.new_volume = initial_volume
        self.scale_volume = 5

    def update_volume(self, new_volume):
        self.new_volume = self.initial_volume * new_volume / self.scale_volume

    def play(self):
        self.sound.play().set_volume(self.new_volume)


# Initialize Object:
menu_movement = Sounds(*SOUNDS2['menu_movement'])
sounds_list = [menu_movement]
'''
menu_selection
menu_back
player_laser
player_hit
player_explosion
enemy_laser
enemy_hit
enemy_explosion
boss_laser
boss_explosion
boss_bg
win_bg
win_fireworks
game_over_bg'''
