# Scripts:
from constants import *
from base_state import BaseState

# Modules:
import pygame
from text_creator import TextCreator


class Controls(BaseState):
    def __init__(self):
        super().__init__()
        # Set up rectangle dimensions
        self.width, self.height = [300, 320]
        self.rect_x, self.rect_y = WIDTH / 2 - self.width / 2, HEIGHT / 2 - self.height / 2
        self.border_width = 5
        # Set up colors
        self.fill_color = "black"
        self.border_color = "white"

        # Screen Text and Options:
        self.index = 0
        self.margin = 30
        self.left_x, self.left_y = WIDTH/2, HEIGHT/3
        self.right_x = self.left_x + 100
        self.padding_x, self.padding_y = 0, 50
        self.controls_options = [
            TextCreator(0, "BACK",
                        'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 5 / 6 * HEIGHT), "", 50),
            TextCreator(1, "Forward", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(2, "Back", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(3, "Left", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(4, "Right", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(5, "Fire", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "Forward", self.margin),
            TextCreator(6, "Switch Weapon",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.left_x, self.left_y), "", self.margin),
            TextCreator(1, "W / ↑",
                        'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ↑", self.margin),
            TextCreator(2, "S / ↓", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ↑", self.margin),
            TextCreator(3, "A / ←", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ↑", self.margin),
            TextCreator(4, "D / →", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ↑", self.margin),
            TextCreator(5, "SPACE", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ↑", self.margin),
            TextCreator(6, "ENTER", 'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (self.right_x, self.left_y), "W / ↑", self.margin),
            TextCreator(7, "",
                        'freesansbold.ttf', 22, 94, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 1 / 3 * HEIGHT), "", self.margin),
        ]

    def handle_action(self):
        self.next_state = "PAUSE"
        self.screen_done = True

    def get_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        # Draw the Rectangle Screen and Border:
        pygame.draw.rect(SCREEN, self.fill_color, (self.rect_x, self.rect_y, self.width, self.height))
        pygame.draw.rect(SCREEN, self.border_color, (self.rect_x, self.rect_y, self.width, self.height), self.border_width)

        # Render Pause Menu Text:
        for text in self.controls_options:
            text.render_text(self.index)
