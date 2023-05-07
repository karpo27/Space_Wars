# Modules:
import pygame

# Create the screen:
SIZE = WIDTH, HEIGHT = (1000, 800)
SCREEN = pygame.display.set_mode(SIZE)
SCREEN_2 = pygame.display.set_mode(SIZE)

# Icon Window:
ICON = 'Images/Screen/icon.png'

# Define Clock for Screen FPS:
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)

# Mouse Button Constants:
LEFT = 1
RIGHT = 3

# Game State:
game_screen = "main menu"

# Constants for Images:
#C_32 = 32
#C_64 = 64

