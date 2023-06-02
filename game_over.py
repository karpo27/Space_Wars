# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator
from pointer import Pointer
from sound import menu_bg, menu_selection
from hud import score

# Modules:
import pygame


class GameOver(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.pos = self.pos_x, self.pos_y = WIDTH / 2, HEIGHT / 3
        self.game_over = []
        # Effects:
        self.text_size = 10
        self.ref_time = 3
        self.increase_rate = 3
        self.game_over = TextCreator(self.index + 1, "GAME OVER", self.font_type, self.text_size, 90, self.base_color, self.hover_color, self.pos, "", 40)

    def handle_action(self):
        self.next_state = "MENU"
        self.screen_done = True
        menu_selection.play_sound()
        menu_bg.play_bg_music(-1)

    def update_text_size(self):
        if self.text_size < 110 and self.increase_rate >= self.ref_time:
            self.text_size += 1
            self.increase_rate = 0
            self.game_over = TextCreator(self.index + 1, "GAME OVER", self.font_type, self.text_size, 90, self.base_color, self.hover_color, self.pos, "", 40)
        # Reset Fire Bullet Variables:
        if self.increase_rate < self.ref_time:
            self.increase_rate += 1

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))

        # Render Game Over:
        self.update_text_size()
        self.game_over.render_text(self.index)

        # Render Back Text and Score:
        self.render_back_text(score)
