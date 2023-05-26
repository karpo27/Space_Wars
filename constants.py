# Modules:
import pygame

# Create the screen:
SIZE = WIDTH, HEIGHT = (1000, 800)
SCREEN = pygame.display.set_mode(SIZE)

# Icon Window:
ICON = 'Images/Screen/icon.png'

# Mouse Button Constants:
LEFT = 1
RIGHT = 3

# Background Assets - Image, Scroll, Music:
BACKGROUNDS = {
    'main_menu': ['Images/Main_Menu/main_menu_img.png', 0.45],
    'level_1': ['Images/Levels_Background/level_1.jpg', 0.8],
    'win': ['Images/Levels_Background/win.jpg', 0]
}
# Player - Category, Path, Scale, Pos, Velocity, HP, Lives, State, Explosion Scale, Particles Range:
PLAYER_ATTRIBUTES = [
    'A', 'Images/Player/', 1, [WIDTH / 2, 19 / 18 * HEIGHT], [6, 6], 3, 3, "alive", 30, 0.85, (22, 38)
]
# Player Bullet - Path, Image Quantity, Scale, Animation Delay, Movement, Velocity, Angle, Bounce, Bullet Sound, Explosion Sound:
PLAYER_BULLETS = {
    'A': ['Images/Player_Bullet/', 5, 0.4, 6, 1, [0, -13], 0, False]
}
# Enemies - Category, Path, Scale, Movement Type, Velocity, HP, Shoots, Bullet Type, Fire Rate, Explosion Scale, Particles Range:
ENEMIES = {
    'a': ['A', 'Images/Enemies/', 0.6, 3, [1, 2], 2, True, ('a1', 'a2'), 200, 0.8, (6, 24)],
    'b': ['B', 'Images/Enemies/', 0.8, 2, [1, 2], 5, True, ('b1', 'b2', 'b3', 'b4', 'b5', 'b6'), 200, 1.5, (16, 30)],
    'c': ['C', 'Images/Enemies/', 0.8, 4, [2, 2], 3, True, ('c1', 'c2'), 200, 0.9, (9, 26)],
    'd': ['D', 'Images/Enemies/', 0.4, 5, [3, 1], 1, True, 'd', 100, 0.6, (6, 24)],
    'e': ['E', 'Images/Enemies/', 0.8, 1, [0, 5], 2, False, None, 0, 1.4, (5, 22)],
    'f1': ['F', 'Images/Enemies/', 0.7, 1, [1, 2], 2, True, ('f', 'd'), 100, 1.1, (9, 26)],
    'f2': ['F', 'Images/Enemies/', 0.7, 1, [-1, 2], 2, True, ('f', 'd'), 100, 1.1, (9, 26)]
}
# Enemies Bullets - Path, Image Quantity, Scale, Animation Delay, Movement Type, Velocity, Angle, Bounce, Sound, Explosion Sound:
ENEMIES_BULLETS = {
    'a1': ['Images/Enemies_Bullets/', 3, 0.2, 8, 2, [-1, 5], -10, True],
    'a2': ['Images/Enemies_Bullets/', 3, 0.2, 8, 2, [1, 5], 10, True],
    'b1': ['Images/Enemies_Bullets/', 3, 0.2, 8, 2, [-6, 6], -45, True],
    'b2': ['Images/Enemies_Bullets/', 3, 0.2, 8, 1, [0, 6], 0, False],
    'b3': ['Images/Enemies_Bullets/', 3, 0.2, 8, 2, [6, 6], 45, True],
    'b4': ['Images/Enemies_Bullets/', 3, 0.2, 8, 2, [-7, 7], -45, True],
    'b5': ['Images/Enemies_Bullets/', 3, 0.2, 8, 1, [0, 7], 0, False],
    'b6': ['Images/Enemies_Bullets/', 3, 0.2, 8, 2, [7, 7], 45, True],
    'c1': ['Images/Enemies_Bullets/', 3, 0.2, 8, 1, [0, 8], 0, False],
    'c2': ['Images/Enemies_Bullets/', 3, 0.2, 8, 1, [0, 6], 0, False],
    'd': ['Images/Enemies_Bullets/', 3, 0.2, 8, 1, [0, 8], 0, False],
    'f': ['Images/Enemies_Bullets/', 3, 0.2, 8, 1, [0, 6], 0, False]
}
# Bosses Action Pattern - Bullet, Quantity, Fire Rate, Fire Rate 2, Movement Duration:
W = {
    'bullet': [['a1', 'b1', 'b2']],
    'qty': (1, 2),
    'fire_rate': 4,
    'fire_rate_2': 6,
    'duration': 1200
}
X = {
    'bullet': [['a2', 'b0', 'b2'], ['a1', 'b1'],
               ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'],
               ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']],
    'qty': (2, 3),
    'fire_rate': 50,
    'fire_rate_2': 20,
    'duration': 1200
}
Y = {
    'bullet': [['b6', 'a6', 'c0', 'c1', 'd5']],
    'qty': (3, 4),
    'fire_rate': 12,
    'fire_rate_2': 9,
    'duration': 900
}
Z = {
    'bullet': [['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'c5', 'c4', 'c3', 'c2', 'c1', 'c0']],
    'qty': (1, 2),
    'fire_rate': 14,
    'fire_rate_2': 7,
    'duration': 1000
}
# Bosses - Category, Path, Scale, Action[Movement], Velocity, HP, Shoot, Fire Rate, Explosion Scale, Particles Range:
BOSSES = {
    'b': ['B', 'Images/Bosses/', 1, [W, X, Y, Z], [2, 5], 5, False, None, 2.0, (160, 190)]
}
# Bosses Bullets - Image, Image Quantity, Scale, Animation Delay, Movement Type, Velocity, Angle, Sound, Explosion Sound:
BOSSES_BULLETS = {
    'a1': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [1, 5], 15, False],
    'a2': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [3, 6], 30, False],
    'a3': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, 5], 45, False],
    'a4': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, 3], 60, False],
    'a5': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, 1], 75, False],
    'a6': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, 0], 90, False],

    'b0': ['Images/Bosses_Bullets/', 3, 0.2, 8, 1, [0, 6], 0, False],
    'b1': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-1, 5], -15, False],
    'b2': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-3, 6], -30, False],
    'b3': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-5, 5], -45, False],
    'b4': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-5, 3], -60, False],
    'b5': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-5, 1], -75, False],
    'b6': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-5, 0], -90, False],

    'c0': ['Images/Bosses_Bullets/', 3, 0.2, 8, 1, [0, -6], -180, False],
    'c1': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [1, -5], -165, False],
    'c2': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [3, -6], -150, False],
    'c3': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, -5], -135, False],
    'c4': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, -3], -120, False],
    'c5': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [5, -1], -105, False],

    'd1': ['Images/Bosses_Bullets/', 3, 0.2, 8, 1, [-5, -1], 105, False],
    'd2': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-5, -3], 120, False],
    'd3': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-5, -5], 135, False],
    'd4': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-3, -6], 150, False],
    'd5': ['Images/Bosses_Bullets/', 3, 0.2, 8, 2, [-1, -5], 165, False]
}
# List of Enemies per Level:
'''
ENEMIES_LVL1 = ['a', 'a', 'a', 'a', 'a', 'a',
                'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd',
                'b',
                'a', 'b', 'a',
                'f1', 'f1', 'f1', 'f2', 'f2', 'f1', 'f2',
                'e', 'e', 'e', 'a', 'a', 'd', 'd',
                'c', 'c', 'b', 'a', 'f1', 'f2', 'f1',
                'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd',
                'b', 'c', 'b', 'a', 'a', 'a', 'c',
                'c', 'a', 'c', 'a', 'c', 'a', 'c',
                'f1', 'f2', 'f1', 'f2', 'f1', 'f2',
                'f1', 'f2', 'f1', 'f2', 'f1', 'f2',
                'b', 'b', 'b', 'b',
                'e', 'b', 'e', 'a', 'a', 'e', 'b', 'e', 'b', 'e',
                'f1', 'f2', 'f1', 'e', 'f2', 'f1', 'f2',
                'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd', 'd',
                'c', 'b', 'c', 'a', 'a', 'c', 'b', 'c', 'e', 'e',
                ]'''
ENEMIES_LVL1 = ['e', 'e', 'a']
# Sounds:
pygame.mixer.init()
SOUNDS2 = {
    'menu_movement': ['menu_movement.mp3', 0.6]
}

SOUNDS = {
    'menu_bg': 'Sounds/menu_bg.mp3',
    'menu_movement': pygame.mixer.Sound('Sounds/menu_movement.mp3'),
    'menu_selection': pygame.mixer.Sound('Sounds/menu_selection.mp3'),
    'menu_back': pygame.mixer.Sound('Sounds/menu_back.mp3'),
    'level1_bg': 'Sounds/level1_bg.mp3',
    'player_laser': pygame.mixer.Sound('Sounds/player_laser.mp3'),
    'player_hit': pygame.mixer.Sound('Sounds/player_hit.mp3'),
    'player_explosion': pygame.mixer.Sound('Sounds/player_explosion.wav'),
    'enemy_laser': pygame.mixer.Sound('Sounds/enemy_laser.wav'),
    'enemy_hit': pygame.mixer.Sound('Sounds/player_hit.mp3'),
    'enemy_explosion': pygame.mixer.Sound('Sounds/player_explosion.wav'),
    'boss_laser': pygame.mixer.Sound('Sounds/player_laser.mp3'),
    'boss_explosion': pygame.mixer.Sound('Sounds/boss_explosion.mp3'),
    'boss_bg': 'Sounds/boss_bg.mp3',
    'win_bg': 'Sounds/win_bg.mp3',
    'win_fireworks': pygame.mixer.Sound('Sounds/win_fireworks.mp3'),
    'game_over_bg': 'Sounds/game_over_bg.mp3'
}
# Volume:
VOL_LVL = 5
VOL_CONSTANT = VOL_LVL/5

VOL_MENU_BG = 0.02
VOL_MENU_MOVEMENT = 0.6
VOL_MENU_SELECTION = 0.4
VOL_MENU_BACK = 0.4
VOL_LEVEL1_BG = 0.3
VOL_PLAYER_LASER = 0.04
VOL_PLAYER_HIT = 0.1
VOL_PLAYER_EXPLOSION = 0.15
VOL_ENEMY_LASER = 0.25
VOL_ENEMY_HIT = 0.1
VOL_ENEMY_EXPLOSION = 0.1
VOL_BOSS_LASER = 0.3
VOL_BOSS_EXPLOSION = 0.15
VOL_BOSS_BG = 0.15
VOL_WIN_BG = 0.1
VOL_WIN_FIREWORKS = 0.06
VOL_GAME_OVER_BG = 0.15

VOLUMES = [
    VOL_MENU_BG,
    VOL_MENU_MOVEMENT,
    VOL_MENU_SELECTION,
    VOL_MENU_BACK,
    VOL_LEVEL1_BG,
    VOL_PLAYER_LASER,
    VOL_PLAYER_HIT,
    VOL_PLAYER_EXPLOSION,
    VOL_ENEMY_LASER,
    VOL_ENEMY_HIT,
    VOL_ENEMY_EXPLOSION,
    VOL_BOSS_LASER,
    VOL_BOSS_EXPLOSION,
    VOL_BOSS_BG,
    VOL_WIN_BG,
    VOL_WIN_FIREWORKS,
    VOL_GAME_OVER_BG,
]

