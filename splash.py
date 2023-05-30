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
        self.pos_y = 2 / 5 * HEIGHT
        self.splash = []
        # Gradually give Image Opacity:
        self.empty_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        self.alpha = 0

        # Time on Screen:
        self.time_text = 0
        self.time_render = 45
        self.time_on_screen = self.time_render + 130
        self.time_start_fadeout = self.time_on_screen + 160
        self.time_next_screen = self.time_start_fadeout + 140

    def render_image(self, alpha_value):
        self.empty_surface.set_alpha(self.alpha)
        self.empty_surface.blit(self.image, (0, 0))
        SCREEN.blit(self.empty_surface, self.rect.center)
        self.alpha += alpha_value

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))
        # Render Text:
        if self.time_render <= self.time_text < self.time_on_screen:
            self.render_image(2)
        elif self.time_on_screen <= self.time_text < self.time_start_fadeout:
            SCREEN.blit(self.empty_surface, self.rect.center)
        elif self.time_start_fadeout <= self.time_text < self.time_next_screen:
            self.render_image(-2)
        elif self.time_text >= self.time_next_screen:
            self.screen_done = True
            menu_bg.play_bg_music(-1)
        self.time_text += 1
