# Scripts:
from base_state import BaseState

# Modules:
import pygame


class Splash(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "MENU"

        self.title = self.font.render("Karpo27 Game", True, pygame.Color("blue"))
        self.title_rect = self.title.get_rect(center=self.screen_rect.center)
        self.time_active = 0

    def update(self, dt):
        self.time_active += dt
        if self.time_active >= 1000:
            self.screen_done = True

    def draw(self, surface):
        surface.fill(pygame.Color("black"))
        surface.blit(self.title, self.title_rect)
