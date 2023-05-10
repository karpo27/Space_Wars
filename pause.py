# Scripts:
from constants import *
from base_state import BaseState
from options import Options
from controls import Controls
from background_creator import *
import constants

# Modules:
import pygame
from text_creator import TextCreator


class Pause(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.rect_x, self.rect_y = WIDTH / 2, HEIGHT / 2 - 160
        self.border_width = 5
        self.screen = "PAUSE"
        self.options_qty = 2
        self.index = 0
        self.margin = 70
        self.pause_options = [
            TextCreator(0, "RESUME", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.rect_x, self.rect_y), "", self.margin),
            TextCreator(1, "OPTIONS", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.rect_x, self.rect_y), "", self.margin),
            TextCreator(2, "QUIT", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.rect_x, self.rect_y), "", self.margin)
        ]

        # Initialize Classes:
        self.options = Options()
        self.controls = Controls()

    def handle_action(self):
        if self.screen == "PAUSE":
            if self.index == 0:
                self.next_state = "LEVEL_1"
                self.screen_done = True
            elif self.index == 1:
                self.index = 0
                self.screen = "OPTIONS"
            elif self.index == 2:
                self.index = 0
                self.next_state = "MENU"
                self.screen_done = True
        elif self.screen == "OPTIONS":
            if self.index == 0:
                pass
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
            elif self.index == 2:
                self.index = 1
                self.screen = "OPTIONS"
        elif self.screen == "CONTROLS":
            self.index = 1
            self.screen = "PAUSE"

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
        # Draw Scrolling Background
        background_lvl_1.update()

        if self.screen == "PAUSE":
            for text in self.pause_options:
                text.render_text(self.index)
        if self.screen == "OPTIONS":
            for text in self.options.options:
                text.render_text(self.index)
        elif self.screen == "CONTROLS":
            self.controls.draw()
