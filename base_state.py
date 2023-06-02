# Scripts:
from constants import WIDTH, HEIGHT, SCREEN

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
        self.hover_color = "#f1d666"

        # Empty Surface:
        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]
        self.empty_surface = None
        self.alpha = 0

    def set_opacity(self):
        self.empty_surface.set_alpha(self.alpha)
        self.empty_surface.blit(self.image, (0, 0))
        SCREEN.blit(self.empty_surface, self.rect.center)

    def render_image(self):
        pass

    def startup(self, persistent):
        self.persist = persistent

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
