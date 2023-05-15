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
        # self.font_size = 26
        # self.margin = 40
        self.pos_left = self.left_x, self.left_y = WIDTH / 3, HEIGHT / 3 - 80
        self.pos_right = self.left_x + 300, self.left_y
        self.text_left = ["Forward", "Back", "Left", "Right", "Fire", "Switch Weapon"]
        self.text_right = ["W / ARROW UP", "S / ARROW DOWN", "A / ARROW LEFT", "D / ARROW RIGHT", "SPACE", "ENTER"]
        self.controls = []
        self.controls.append(TextCreator(self.index, "BACK", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                                         (WIDTH / 2, 5 / 6 * HEIGHT), "", 50), )
        for index, text in enumerate(self.text_left):
            self.controls.append(
                TextCreator(index + 1, text, self.font_type, 26, 52, self.base_color, self.hover_color, self.pos_left,
                            self.text_left[0], 40))
        for index, text in enumerate(self.text_right):
            self.controls.append(
                TextCreator(index + 1, text, self.font_type, 26, 52, self.base_color, self.hover_color, self.pos_right,
                            self.text_right[0], 40))

        '''
        self.controls = [
            TextCreator(0, "BACK",
                        'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 5 / 6 * HEIGHT), "", 50),
            TextCreator(1, "Forward", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(2, "Back", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(3, "Left", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(4, "Right", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(5, "Fire", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(6, "Switch Weapon", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(1, "W / ARROW UP", 'freesansbold.ttf', self.font_size, 48, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ARROW UP", self.margin),
            TextCreator(2, "S / ARROW DOWN", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ARROW UP", self.margin),
            TextCreator(3, "A / ARROW LEFT", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ARROW UP", self.margin),
            TextCreator(4, "D / ARROW RIGHT", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ARROW UP", self.margin),
            TextCreator(5, "SPACE", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ARROW UP", self.margin),
            TextCreator(6, "ENTER", 'freesansbold.ttf', self.font_size, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ARROW UP", self.margin),
        ]
        '''
