# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator

# Modules:
import pygame


class Splash(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "MENU"

        # Screen Text:
        self.pos_y = 2/5 * HEIGHT
        self.splash = [TextCreator(0, "Karpo27 Game", self.font_type, 48, 48, "white", "blue",
                                   (self.pos_x, self.pos_y), "", 70)
                       ]
        # Time Parameters:
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 1000:
            self.screen_done = True

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))

        # Render Splash Text:
        for text in self.splash:
            text.render_text(self.index)

