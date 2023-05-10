# Scripts:
from constants import *
from base_state import BaseState

# Modules:
import pygame
from text_creator import TextCreator


class Controls:
    def __init__(self):
        #self.width, self.height = [520, 530]
        #self.rect_x, self.rect_y = WIDTH / 2 - self.width / 2, HEIGHT / 2 - 200
        self.border_width = 5
        # Set up colors
        self.fill_color = "black"
        self.border_color = "white"

        # Screen Text and Options:
        self.screen = "CONTROLS"
        self.index = 0
        self.font_size = 22
        self.margin = 30
        self.left_x, self.left_y = WIDTH/3, HEIGHT/3
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

    def handle_action(self):
        self.screen = "PAUSE"
        #self.screen_done = True

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self):
        # Render Pause Menu Text:
        for text in self.controls_options:
            text.render_text(self.index)
