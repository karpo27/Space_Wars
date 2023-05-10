# Scripts:
from constants import *

# Modules:
from text_creator import TextCreator


class Credits:
    def __init__(self):
        # Screen Text and Options:
        self.index = 0
        self.pos_x, self.pos_y = WIDTH/2, HEIGHT/3
        self.font_size = 48
        self.margin = 40
        self.credits = [
            TextCreator(0, "BACK",
                        'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (WIDTH/2, 5/6 * HEIGHT), "", 50),
            TextCreator(1, "May 2023", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
            TextCreator(2, "Game Project is a Python game developed by me: Julian Giudice (github.com/karpo27).",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
            TextCreator(3, "It's my first game since I started learning Python 6 months ago.",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
            TextCreator(4,
                        "I want to thank Pygame for allowing me to use this module,",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
            TextCreator(5, "and allow so many users to code their games.",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
            TextCreator(6, "I'll keep coding and trying myself harder to incorporate to the IT world. ",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
        ]
