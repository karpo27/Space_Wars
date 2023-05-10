# Scripts:
from constants import *
from base_state import BaseState

# Modules:
import pygame
from text_creator import TextCreator


class Controls:
    def __init__(self):
        # Screen Text and Options:
        self.index = 0
        self.font_size = 26
        self.margin = 40
        self.left_x, self.left_y = WIDTH/3, HEIGHT/3 - 80
        self.right_x = self.left_x + 300
        self.padding_x, self.padding_y = 0, 50
        self.controls_options = [
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
            TextCreator(7, "", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 1 / 3 * HEIGHT), "W / ARROW UP", self.margin)
        ]

    def draw(self):
        # Render Pause Menu Text:
        for text in self.controls_options:
            text.render_text(self.index)
