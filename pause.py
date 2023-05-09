# Scripts:
from constants import *
from base_state import BaseState
import constants

# Modules:
import pygame
from text_creator import TextCreator


class Pause(BaseState):
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
        self.options_qty = 2
        self.index = 0
        self.margin = 70
        self.padding_x, self.padding_y = 0, 50
        self.pause_options = [
            TextCreator(0, "RESUME", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.rect_x + self.width / 2 + self.padding_x, self.rect_y + self.padding_y), "", self.margin),
            TextCreator(1, "OPTIONS", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.rect_x + self.width / 2 + self.padding_x, self.rect_y + self.padding_y), "", self.margin),
            TextCreator(2, "QUIT", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.rect_x + self.width / 2 + self.padding_x, self.rect_y + self.padding_y), "", self.margin)
        ]

    def handle_action(self):
        if self.index == 0:
            self.next_state = "LEVEL_1"
        elif self.index == 1:
            self.next_state = "CONTROLS"
        elif self.index == 2:
            self.next_state = "MENU"
        self.screen_done = True

    def get_event(self, event):
        # Pause Menu Movement:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.index += 1
            elif event.key == pygame.K_UP:
                self.index -= 1
            elif event.key == pygame.K_RETURN:
                self.handle_action()

        # Player Icon Movement Boundaries:
        if self.index > self.options_qty:
            self.index = 0
        elif self.index < 0:
            self.index = self.options_qty

    def draw(self, surface):
        # Draw the Rectangle Screen and Border:
        pygame.draw.rect(SCREEN, self.fill_color, (self.rect_x, self.rect_y, self.width, self.height))
        pygame.draw.rect(SCREEN, self.border_color, (self.rect_x, self.rect_y, self.width, self.height), self.border_width)

        # Render Pause Menu Text:
        for text in self.pause_options:
            text.render_text(self.index)
