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
    'main_menu': ['Images/Main_Menu/main_menu_img.png', 0.45, 'Sounds/main_menu_music.mp3'],
    'level_1': ['Images/Levels_Background/level_1.jpg', 0.8, 'Sounds/background.wav'],
    'win': ['Images/Levels_Background/win.jpg', 0, 'Sounds/background.wav']
}
# Player - Image, Pos, Velocity, HP, Lives, State, Explosion Scale, Particles Range:
PLAYER_ATTRIBUTES = [
    'Images/Player/player_img.png', [WIDTH / 2, 19 / 18 * HEIGHT], [5, 5], 3, 2, "alive", (0.85, 0.85), (22, 38)
]
# Player Bullet - Path, Velocity, Bullet Sound, Explosion Sound:
PLAYER_BULLETS = {
    'player_bullet_d': ['Images/Player_Bullet/', [0, 13], 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
# Enemies - Category, Path, Scale, Movement Type, Velocity, HP, Shoots, Bullet Type, Fire Rate, Explosion Scale, Particles Range:
ENEMIES = {
    'a': ['A', 'Images/Enemies/', (0.6, 0.6), 3, [1, 2], 2, True, ('a1', 'a2'), 200, (0.8, 0.8), (6, 24)],
    'b': ['B', 'Images/Enemies/', (0.8, 0.8), 2, [1, 2], 6, True, ('b1', 'b2', 'b3', 'b4', 'b5', 'b6'), 200, (1.5, 1.5), (16, 30)],
    'c': ['C', 'Images/Enemies/', (0.8, 0.8), 4, [2, 2], 3, True, ('c1', 'c2'), 200, (0.9, 0.9), (9, 26)],
    'd': ['D', 'Images/Enemies/', (0.4, 0.4), 5, [3, 1], 1, True, 'd', 100, (0.6, 0.6), (6, 24)],
    'e': ['E', 'Images/Enemies/', (0.8, 0.8), 1, [0, 5], 2, False, None, 0, (1.4, 1.4), (5, 22)],
    'f1': ['F', 'Images/Enemies/', (0.7, 0.7), 1, [1, 2], 3, True, ('f', 'd'), 100, (1.1, 1.1), (9, 26)],
    'f2': ['F', 'Images/Enemies/', (0.7, 0.7), 1, [-1, 2], 3, True, ('f', 'd'), 100, (1.1, 1.1), (9, 26)]
}
# Enemies Bullets - Path, Movement Type, Velocity, Angle, Sound, Explosion Sound:
ENEMIES_BULLETS = {
    'a1': ['Images/Enemies_Bullets/', 2, [-1, 5], -10, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'a2': ['Images/Enemies_Bullets/', 2, [1, 5], 10, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b1': ['Images/Enemies_Bullets/', 2, [-6, 6], -45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b2': ['Images/Enemies_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b3': ['Images/Enemies_Bullets/', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b4': ['Images/Enemies_Bullets/', 2, [-7, 7], -45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b5': ['Images/Enemies_Bullets/', 1, [0, 7], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b6': ['Images/Enemies_Bullets/', 2, [7, 7], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'c1': ['Images/Enemies_Bullets/', 1, [0, 8], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'c2': ['Images/Enemies_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'd': ['Images/Enemies_Bullets/', 1, [0, 8], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'f': ['Images/Enemies_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
# Bosses - Category, Path, Scale, Action {Movement: Bullet Type}, Velocity, HP, Fire Rate, Explosion Scale, Particles Range:
BOSSES = {
    'a': ['A', 'Images/Bosses/', (0.6, 0.6), 1, [0, 0], 100, ('a3', 'a2'), 200, (0.8, 0.8), (60, 80)],
    'b': ['B', 'Images/Bosses/',
          (1.1, 1.1),
          {"X": [['a2', 'b0', 'b2'], ['a1', 'b1'], ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'b0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6'],
                 ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']],
           "Y": [],
           "Y-ANGLE": [],
           "X-BEAM": [['b0']]
           },
          [1, 4],
          5,
          80,
          (2.0, 2.0),
          (160, 190)],
    'c': ['C', 'Images/Bosses/', (0.8, 0.8), 1, [0, 0], 150, ('c1', 'c2'), 200, (0.9, 0.9),
          (60, 80)],
}
# Bosses Bullets - Image, Movement Type, Velocity, Angle, Sound, Explosion Sound:
BOSSES_BULLETS = {
    'a1': ['Images/Bosses_Bullets/', 2, [1, 5], 15, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'a2': ['Images/Bosses_Bullets/', 2, [3, 6], 30, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'a3': ['Images/Bosses_Bullets/', 2, [5, 5], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'a4': ['Images/Bosses_Bullets/', 2, [5, 3], 60, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'a5': ['Images/Bosses_Bullets/', 2, [5, 1], 75, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'a6': ['Images/Bosses_Bullets/', 2, [5, 0], 90, 'Sounds/laser.wav', 'Sounds/explosion.wav'],

    'b0': ['Images/Bosses_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b1': ['Images/Bosses_Bullets/', 2, [-1, 5], -15, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b2': ['Images/Bosses_Bullets/', 2, [-3, 6], -30, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b3': ['Images/Bosses_Bullets/', 2, [-5, 5], -45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b4': ['Images/Bosses_Bullets/', 2, [-5, 3], -60, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b5': ['Images/Bosses_Bullets/', 2, [-5, 1], -75, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b6': ['Images/Bosses_Bullets/', 2, [-5, 0], -90, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b7': ['Images/Bosses_Bullets/', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b8': ['Images/Bosses_Bullets/', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],

    'c1': ['Images/Bosses_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'c2': ['Images/Bosses_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'c3': ['Images/Bosses_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'c4': ['Images/Bosses_Bullets/', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
# List of Enemies per Level:
ENEMIES_LVL1 = ['a', 'b', 'c', 'd', 'e', 'f1']
#ENEMIES_LVL1 = []
