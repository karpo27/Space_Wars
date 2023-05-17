# Scripts:
from constants import *
from base_state import BaseState

# Modules:
from text_creator import TextCreator


class Options(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.text = ["AUDIO", "CONTROLS", "BACK"]
        self.options = []
        for index, text in enumerate(self.text):
            self.options.append(
                TextCreator(index, text, self.font_type, 48, 52, self.base_color, self.hover_color, self.pos,
                            self.text[0], 70))


class Controls(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.pos_left = self.left_x, self.left_y = WIDTH / 3, HEIGHT / 3 - 80
        self.pos_right = self.left_x + 300, self.left_y
        self.text_left = ["Forward", "Back", "Left", "Right", "Fire", "Switch Weapon"]
        self.text_right = ["W / ARROW UP", "S / ARROW DOWN", "A / ARROW LEFT", "D / ARROW RIGHT", "SPACE", "ENTER"]
        self.controls = []
        self.controls.append(TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color,
                                         (WIDTH / 2, 5 / 6 * HEIGHT), "", 50))
        for index, text in enumerate(self.text_left):
            self.controls.append(
                TextCreator(index + 1, text, self.font_type, 26, 52, self.base_color, self.hover_color, self.pos_left,
                            self.text_left[0], 40))
        for index, text in enumerate(self.text_right):
            self.controls.append(
                TextCreator(index + 1, text, self.font_type, 26, 52, self.base_color, self.hover_color, self.pos_right,
                            self.text_right[0], 40))


class Credits(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.pos = self.pos_x, self.pos_y = WIDTH/2, HEIGHT/3
        self.text = ["May 2023", "Game Project is a Python game developed by me: Julian Giudice (github.com/karpo27).",
                     "It's my first game since I started learning Python 6 months ago.",
                     "I want to thank Pygame for allowing me to use this module,",
                     "and allow so many users to code their games.",
                     "I'll keep coding and trying myself harder to incorporate to the IT world."]
        self.credits = []
        self.credits.append(TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color,
                                        (WIDTH/2, 5/6 * HEIGHT), "", 50))
        for index, text in enumerate(self.text):
            self.credits.append(
                TextCreator(index + 1, text, self.font_type, 22, 52, self.base_color, self.hover_color, self.pos,
                            "", 40))


