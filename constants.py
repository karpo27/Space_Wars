# Modules:
import pygame

# Create the screen:
SIZE = WIDTH, HEIGHT = (1000, 800)
SCREEN = pygame.display.set_mode(SIZE)

# Icon Window:
ICON = 'Images/Screen/icon.png'

# Define Clock for Screen FPS:
#clock = pygame.time.Clock()
#FPS = 60
#dt = clock.tick(FPS)

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
    'Images/Player/player_img.png', [WIDTH/2, 19/18 * HEIGHT], [5, 5], 3, 2, "alive", (0.85, 0.85), (22, 38)
]
# Player Bullet - Path, Velocity, Bullet Sound, Explosion Sound:
PLAYER_BULLETS = {
    'player_bullet_d': ['Images/Player_Bullet/', [0, 13], 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
# Enemies - Category, Image, Scale, Movement Type, Velocity, HP, Shoots, Bullet Type, Fire Rate, Explosion Scale, Particles Range:
ENEMIES = {
    'enemy_a': ['A', 'Images/Enemies/enemy_A.png', (0.6, 0.6), 2, [1, 2], 2, True, ('a1', 'a2'), 200, (0.8, 0.8), (10, 28)],
    'enemy_b': ['B', 'Images/Enemies/enemy_B.png', (0.8, 0.8), 2, [1, 2], 6, True, ('b1', 'b2', 'b3'), 200, (1.5, 1.5), (20, 35)],
    'enemy_c': ['C', 'Images/Enemies/enemy_C.png', (0.8, 0.8), 2, [1, 2], 3, True, ('c1', 'c2'), 200, (0.9, 0.9), (12, 30)],
    'enemy_d': ['D', 'Images/Enemies/enemy_D.png', (0.4, 0.4), 3, [2, 1], 1, True, 'd', 100, (0.6, 0.6), (8, 27)],
    'enemy_e': ['E', 'Images/Enemies/enemy_E.png', (0.8, 0.8), 1, [0, 4], 2, False, None, 0, (1.4, 1.4), (10, 28)],
    'enemy_f1': ['F', 'Images/Enemies/enemy_F.png', (0.7, 0.7), 1, [1, 2], 3, True, 'f', 100, (1.1, 1.1), (12, 30)],
    'enemy_f2': ['F', 'Images/Enemies/enemy_F.png', (0.7, 0.7), 1, [-1, 2], 3, True, 'f', 100, (1.1, 1.1), (12, 30)]
}
# Enemies Bullets - Image, Movement Type, Velocity, Angle, Sound, Explosion Sound:
ENEMIES_BULLETS = {
    'e_bullet_a1': ['Images/Enemies_Bullets/enemy_bullet_F.png', 2, [-1, 5], -10, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_a2': ['Images/Enemies_Bullets/enemy_bullet_F.png', 2, [1, 5], 10, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_b1': ['Images/Enemies_Bullets/enemy_bullet_F.png', 2, [-6, 6], -45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_b2': ['Images/Enemies_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_b3': ['Images/Enemies_Bullets/enemy_bullet_F.png', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_c1': ['Images/Enemies_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_c2': ['Images/Enemies_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_d': ['Images/Enemies_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'e_bullet_f': ['Images/Enemies_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
# Bosses - Category, Image, Scale, Movement Actions, Velocity, HP, Bullet Type, Bullet Pattern Counter, Fire Cycles, Explosion Scale, Particles Range:
BOSSES = {
    'boss_a': ['Images/Bosses/Captain_Death_Ship.png', (0.6, 0.6), 1, [0, 0], 100, ('a3', 'a2'), 200, (0.8, 0.8), (60, 80)],
    'boss_b': ['Images/Bosses/General_Bugfix_Ship.png', (1.1, 1.1),
               [1, 2],
               [-1, 0],
               1,
               [['a2', 'b0', 'b2'], ['a1', 'b1'], ['b0'], ['b1'], ['b2'], ['b3'], ['b4'], ['b5'], ['b6'], ['b0'], ['a1'], ['a2'], ['a3'], ['a4'], ['a5'], ['a6'], ['b0', 'b1', 'b2', 'b3', 'b4', 'b5', 'b6', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6']], 200,
               [(0, 5), (100, 4), (200, 2), (205, 2), (210, 2), (215, 2), (220, 2), (225, 2), (230, 2), (240, 2), (245, 2), (250, 2), (255, 2), (260, 2), (265, 2), (270, 2), (280, 3)],
               (2.0, 2.0),
               (160, 190)],
    'boss_c': ['Images/Bosses/Crimson_Emperor_Ship.png', (0.8, 0.8), 1, [0, 0], 150, ('c1', 'c2'), 200, (0.9, 0.9), (60, 80)],
}
# Bosses Bullets - Image, Movement Type, Velocity, Angle, Sound, Explosion Sound:
BOSSES_BULLETS = {
    'b_bullet_a1': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [1, 5], 15, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_a2': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [3, 5], 30, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_a3': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [5, 5], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_a4': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [5, 3], 60, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_a5': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [5, 1], 75, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_a6': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [5, 0], 90, 'Sounds/laser.wav', 'Sounds/explosion.wav'],

    'b_bullet_b0': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 5], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b1': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-1, 5], -15, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b2': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-3, 5], -30, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b3': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-5, 5], -45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b4': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-5, 3], -60, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b5': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-5, 1], -75, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b6': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-5, 0], -90, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b7': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b8': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],

    'b_bullet_c1': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c2': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c3': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c4': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
# List of Enemies per Level:
ENEMIES_LVL1 = ['a', 'b', 'c', 'd', 'e', 'f1', 'f2']
#ENEMIES_LVL1 = []
