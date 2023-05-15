# Scripts:
from constants import *
from base_state import BaseState
from submenus import Options, Controls
from pointer import Pointer
from background_creator import *

# Modules:
import pygame
from text_creator import TextCreator


class Pause(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.pos_x, self.pos_y = WIDTH/2, 3/5 * HEIGHT
        self.border_width = 5
        self.screen = "PAUSE"
        self.options_qty = 2
        self.index = 0
        self.margin = 70
        self.pause = [
            TextCreator(0, "RESUME", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "RESUME", self.margin),
            TextCreator(1, "OPTIONS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "RESUME", self.margin),
            TextCreator(2, "BACK TO MENU", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "RESUME", self.margin)
        ]

        # Initialize Classes:
        self.options = Options()
        self.controls = Controls()
        self.pointer = Pointer()

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
                self.options_qty = 0
            elif self.index == 2:
                self.index = 1
                self.screen = "PAUSE"
        elif self.screen == "CONTROLS":
            self.index = 1
            self.screen = "OPTIONS"
            self.options_qty = 2

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
        # Draw Background
        background_lvl_1.update()

        # Render Pause Menu:
        if self.screen == "PAUSE":
            for text in self.pause:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.pause[self.index].text_position, self.screen)
        elif self.screen == "OPTIONS":
            for text in self.options.options:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.options.options[self.index].text_position, self.screen)
        elif self.screen == "AUDIO":
            pass
        elif self.screen == "CONTROLS":
            for text in self.controls.controls:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.controls.controls[self.index].text_position, self.screen)

