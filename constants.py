# Modules:
import pygame

# Create the screen:
SIZE = WIDTH, HEIGHT = (1000, 800)
SCREEN = pygame.display.set_mode(SIZE)

# Icon Window:
ICON = 'Images/Screen/icon.png'

# Define Clock for Screen FPS:
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)

# Mouse Button Constants:
LEFT = 1
RIGHT = 3

# Create Sprites Group:
PLAYER_BULLETS_GROUP = pygame.sprite.Group()
ENEMIES_GROUP = pygame.sprite.Group()
ENEMIES_BULLETS_GROUP = pygame.sprite.Group()

# Player - Image, Pos, Velocity, HP, Fire Rate:
PLAYER_ATTRIBUTES = [
    'Images/Player/player_img.png', [WIDTH/2, 19/18 * HEIGHT], [5, 5], 3, 3, (0.8, 0.8)
]

# Player Bullet - Image, Velocity, Bullet Sound, Explosion Sound:
PLAYER_BULLETS = {
    'player_bullet_d': ['Images/Player_Bullet/bullets.png', [0, 0.8 * dt], 'Sounds/laser.wav', 'Sounds/explosion.wav']
}

# Enemies - Category, Image, Scale, Movement Type, Velocity, HP, Shoots, Bullet Type, Fire Rate, Explosion Scale
ENEMIES = {
    'enemy_a': ['A', 'Images/Enemies/enemy_A.png', (0.6, 0.6), 2, [1, 2], 2, True, ('a1', 'a2'), 200, (0.8, 0.8)],
    'enemy_b': ['B', 'Images/Enemies/enemy_B.png', (0.8, 0.8), 2, [1, 2], 6, True, ('b1', 'b2', 'b3'), 200, (1.5, 1.5)],
    'enemy_c': ['C', 'Images/Enemies/enemy_C.png', (0.8, 0.8), 2, [1, 2], 3, True, ('c1', 'c2'), 200, (0.9, 0.9)],
    'enemy_d': ['D', 'Images/Enemies/enemy_D.png', (0.4, 0.4), 3, [2, 1], 1, True, 'd', 100, (0.6, 0.6)],
    'enemy_e': ['E', 'Images/Enemies/enemy_E.png', (0.8, 0.8), 1, [0, 4], 2, False, None, 0, (1.4, 1.4)],
    'enemy_f1': ['F', 'Images/Enemies/enemy_F.png', (0.7, 0.7), 1, [1, 2], 3, True, 'f', 100, (1.1, 1.1)],
    'enemy_f2': ['F', 'Images/Enemies/enemy_F.png', (0.7, 0.7), 1, [-1, 2], 3, True, 'f', 100, (1.1, 1.1)]
}

# Enemies Bullets - Image, Movement Type, Velocity, Angle, Sound, Explosion Sound
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

