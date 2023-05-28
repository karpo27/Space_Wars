# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator
from pointer import Pointer
from sound import menu_bg, menu_selection

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
        self.back = TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color, (WIDTH / 2, 9 / 10 * HEIGHT), "", 50)
        self.back_ref_time = 600
        self.back_time = 0

        # Initialize Classes:
        self.pointer = Pointer()

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

        # Render Back Text:
        if self.back_time >= self.back_ref_time:
            self.back.render_text(self.index)
            self.pointer.draw_rotated(self.back.text_position, "GAME OVER")
        else:
            self.back_time += 1
