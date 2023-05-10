# Scripts:
from splash import Splash
from game import Game
from main_menu import Menu
from level_1 import Level1
from pause import Pause
from game_over import GameOver

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
    "LEVEL_1": Level1(),
    "PAUSE": Pause(),
    "GAME_OVER": GameOver(),
}

# Initialize game Object and run Game:
game = Game(SCREEN, states, "SPLASH")
game.run()

pygame.quit()
sys.exit()

