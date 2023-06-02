# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator
from sound import menu_bg

# Modules:
import pygame


class Splash(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "MENU"

        # Screen Text:
        self.image = pygame.image.load(f'{SPLASH_PATH}').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [WIDTH/2 - 180, HEIGHT/4]
        self.pos_y = 2/5 * HEIGHT
        # Empty Surface:
        self.empty_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)

        # Time on Screen:
        self.time_text = 0
        self.time_render = 0   # 40 ms
        self.time_on_screen = self.time_render + 0    # 130 ms
        self.time_start_fadeout = self.time_on_screen + 0     # 160 ms
        self.time_next_screen = self.time_start_fadeout + 0   # 140 ms

    def render_image(self):
        if self.time_render <= self.time_text < self.time_on_screen:
            self.set_opacity()
            self.alpha += 2
        elif self.time_on_screen <= self.time_text < self.time_start_fadeout:
            SCREEN.blit(self.empty_surface, self.rect.center)
        elif self.time_start_fadeout <= self.time_text < self.time_next_screen:
            self.set_opacity()
            self.alpha -= 2
        elif self.time_text >= self.time_next_screen:
            self.screen_done = True
            menu_bg.play_bg_music(-1)
        self.time_text += 1

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))
        # Render Text:
        self.render_image()
