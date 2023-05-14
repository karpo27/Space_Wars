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
        self.index = 1
        self.pos_x, self.pos_y = WIDTH/2, 3/5 * HEIGHT
        self.font_size = 48
        self.margin = 70
        self.game_over = [
            TextCreator(0, "GAME OVER", 'freesansbold.ttf', 94, 94, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin),
            TextCreator(1, "GO TO MENU", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "", self.margin)
        ]

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
