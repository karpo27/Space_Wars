# Scripts:
from constants import SCREEN
from splash import Splash
from game import Game
from main_menu import Menu
from level_1 import Level1
from pause import Pause
from game_over import GameOver

# Modules:
import sys
import pygame

# Set Game States and Initialize Objects:
states = {
    'SPLASH': Splash(),
    'MENU': Menu(),
    'LEVEL_1': Level1(),
    'PAUSE': Pause(),
    'GAME_OVER': GameOver(),
}

# Initialize game Object and run Game:
if __name__ == '__main__':
    game = Game(SCREEN, states, 'SPLASH')
    game.run()

