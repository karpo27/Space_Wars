# Scripts:
from gameplay import Gameplay
from game_over import GameOver
from splash import Splash
from game import Game
from main_menu import Menu

# Modules:
import sys
import pygame

# Initialize Pygame:
pygame.init()

# Create the Screen:
SIZE = WIDTH, HEIGHT = (1000, 800)
SCREEN = pygame.display.set_mode(SIZE)

# Icon Window:
ICON = 'Images/Screen/icon.png'

# Set Game States and Initialize Objects:
states = {
    "SPLASH": Splash(),
    "MENU": Menu(),
    "GAMEPLAY": Gameplay(),
    "GAME_OVER": GameOver(),
}

# Initialize game Object and run Game:
game = Game(SCREEN, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()

