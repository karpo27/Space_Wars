# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator
from sounds import set_bg_music

# Modules:
import pygame


class Splash(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "MENU"

        # Screen Text:
        self.pos_y = 2 / 5 * HEIGHT
        self.splash = []

        # Time on Screen:
        self.time_next_screen = 90     # 320
        # Text Time:
        self.time_fadeout = 70     # 240
        self.time_render = 30      # 150
        self.time_text = 0

    def update(self, dt):
        if self.time_render <= self.time_text < self.time_fadeout:
            self.splash.append(TextCreator(0, "Created by Julian Giudice", self.font_type, 28, 28, "white", "white",
                                           (self.pos_x, self.pos_y), "", 70))
        elif self.time_fadeout <= self.time_text < self.time_next_screen:
            self.splash.clear()
        elif self.time_text >= self.time_fadeout:
            self.screen_done = True
            set_bg_music(SOUNDS2['menu_bg'], VOL_MENU_BG, -1)
        self.time_text += 1

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))
        # Render Text:
        for text in self.splash:
            text.render_text(self.index)
