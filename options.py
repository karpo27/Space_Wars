# Scripts:
from constants import *

# Modules:
from text_creator import TextCreator


class Options:
    def __init__(self):
        # Screen Text and Options:
        self.index = 0
        self.pos_x, self.pos_y = WIDTH/2, 3/5 * HEIGHT
        self.font_size = 48
        self.margin = 70
        self.options = [
            TextCreator(0, "AUDIO", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH/2, 3/5 * HEIGHT), "AUDIO", 70),
            TextCreator(1, "CONTROLS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH/2, 3/5 * HEIGHT), "AUDIO", 70),
            TextCreator(2, "BACK", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH/2, 3/5 * HEIGHT), "AUDIO", 70)
        ]

