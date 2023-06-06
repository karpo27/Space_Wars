# Scripts:
from constants import *

# Modules:
import pygame

# Initialize Mixer:
pygame.mixer.init()
pygame.mixer.set_num_channels(40)
channel = pygame.mixer.Channel(0)


class Sound:
    def __init__(self, path, initial_volume):
        self.path = path
        self.sound = pygame.mixer.Sound(f'Sounds/{self.path}')
        self.initial_volume = initial_volume
        self.new_volume = initial_volume
        self.ref_volume = 5

    def update_volume(self, new_volume, category):
        self.new_volume = self.initial_volume * new_volume/self.ref_volume
        if category == "music":
            pygame.mixer.music.set_volume(self.new_volume)

    def play_sound(self, queue_sound=None):
        if queue_sound is not None:
            self.sound.set_volume(self.new_volume)
            channel.queue(self.sound)
        else:
            self.sound.play().set_volume(self.new_volume)

    def play_bg_music(self, loop, fadeout_time=None):
        if fadeout_time is not None:
            pygame.mixer.music.fadeout(fadeout_time)
            pygame.mixer.music.queue(f'Sounds/{self.path}', loops=loop)
            pygame.mixer.music.set_volume(self.new_volume)
        else:
            pygame.mixer.music.load(f'Sounds/{self.path}')
            pygame.mixer.music.set_volume(self.new_volume)
            pygame.mixer.music.play(loop)


# Initialize Objects:
menu_movement = Sound(*SOUNDS['menu_movement'])
menu_selection = Sound(*SOUNDS['menu_selection'])
menu_back = Sound(*SOUNDS['menu_back'])
scene_1_galaxy_laser = Sound(*SOUNDS['scene_1_galaxy_laser'])
scene_1_galaxy_explosion = Sound(*SOUNDS['scene_1_galaxy_explosion'])
scene_1_dialogue_globe = Sound(*SOUNDS['scene_1_dialogue_globe'])
scene_1_dialogue_letter = Sound(*SOUNDS['scene_1_dialogue_letter'])
player_laser = Sound(*SOUNDS['player_laser'])
player_hit = Sound(*SOUNDS['player_hit'])
player_explosion = Sound(*SOUNDS['player_explosion'])
player_item_hp = Sound(*SOUNDS['player_item_hp'])
player_item_life = Sound(*SOUNDS['player_item_life'])
enemy_laser = Sound(*SOUNDS['enemy_laser'])
enemy_hit = Sound(*SOUNDS['enemy_hit'])
enemy_explosion = Sound(*SOUNDS['enemy_explosion'])
enemy_e_flyby = Sound(*SOUNDS['enemy_e_flyby'])
boss_laser = Sound(*SOUNDS['boss_laser'])
boss_deflect = Sound(*SOUNDS['boss_deflect'])
boss_explosion = Sound(*SOUNDS['boss_explosion'])
win_fireworks = Sound(*SOUNDS['win_fireworks'])

menu_bg = Sound(*MUSICS['menu_bg'])
scene_1_bg = Sound(*MUSICS['scene_1_bg'])
level_1_bg = Sound(*MUSICS['level_1_bg'])
boss_bg = Sound(*MUSICS['boss_bg'])
win_level_bg = Sound(*MUSICS['win_level_bg'])
win_bg = Sound(*MUSICS['win_bg'])
game_over_bg = Sound(*MUSICS['game_over_bg'])

sounds_list = [menu_movement, menu_selection, menu_back, scene_1_galaxy_laser, scene_1_galaxy_explosion,
               scene_1_dialogue_globe, scene_1_dialogue_letter, player_laser, player_hit, player_explosion,
               player_item_hp, enemy_laser, player_item_life, enemy_hit, enemy_explosion, enemy_e_flyby, boss_laser,
               boss_deflect, boss_explosion, win_fireworks]

musics_list = [menu_bg, scene_1_bg, level_1_bg, boss_bg, win_bg, game_over_bg, win_level_bg]
