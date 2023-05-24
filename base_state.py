# Scripts:
from constants import WIDTH, HEIGHT

# Modules:
import pygame


class BaseState(object):
    def __init__(self):
        # Game State:
        self.screen_done = False
        self.quit = False
        self.next_state = None
        self.persist = {}

        # Text Properties:
        self.index = 0
        self.pos = self.pos_x, self.pos_y = WIDTH/2, 3/5 * HEIGHT
        self.font_type = 'freesansbold.ttf'
        self.base_color = "white"
        self.hover_color = (193, 225, 193)

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
