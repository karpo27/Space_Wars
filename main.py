# Scripts:
from constants import SCREEN
from splash import Splash
from game import Game
from menu import Menu
from scene_1 import Scene1
from level_1 import Level1
from pause import Pause
from win import Win
from game_over import GameOver

# Modules:


# Set Game States and Initialize Objects:
states = {
    'SPLASH': Splash(),
    'MENU': Menu(),
    'SCENE_1': Scene1(),
    'LEVEL_1': Level1(),
    'PAUSE': Pause(),
    'WIN': Win(),
    'GAME_OVER': GameOver()
}

# Initialize game Object and run Game:
if __name__ == '__main__':
    game = Game(SCREEN, states, 'SPLASH')
    game.run()

