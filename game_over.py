# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator
from pointer import Pointer

# Modules:
import pygame


class GameOver(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.pos = self.pos_x, self.pos_y = WIDTH / 2, HEIGHT / 3
        self.text = ["GAME OVER"]
        self.game_over = []
        self.game_over.append(TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color,
                                          (WIDTH / 2, 5 / 6 * HEIGHT), "", 50))
        self.game_over.append(
            TextCreator(self.index + 1, self.text[0], self.font_type, 90, 90, self.base_color, self.hover_color, self.pos,
                        "", 40))

        # Initialize Classes:
        self.pointer = Pointer()

    def handle_action(self):
        if self.index == 0:
            self.next_state = "LEVEL_1"
            self.screen_done = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.next_state = "MENU"
                self.screen_done = True

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))

        # Render Game Over:
        for text in self.game_over:
            text.render_text(self.index)
        self.pointer.draw_rotated(self.game_over[self.index].text_position, "GAME OVER")
