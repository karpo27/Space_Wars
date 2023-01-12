# Modules
import pygame

# Create the screen
SIZE = WIDTH, HEIGHT = (1000, 800)
SCREEN = pygame.display.set_mode(SIZE)

# Define Clock for Screen FPS
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)

# Mouse Button Constants
LEFT = 1
RIGHT = 3

# Constants for Images:
C_32 = 32
C_64 = 64

# Images

background_img = {
    'level_1': 'Images/Levels_Background/space_bg.jpg'
}

# Size: 64 x 64
enemies_img = {
    'common': 'Images/Enemies/enemy_common.png'
}

# Size: 32 x 32
enemies_bullet_img = {
    'common': 'Images/Enemies_Bullet/enemy_bullet.png'
}

# Sounds
