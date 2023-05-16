# Scripts
from constants import *

# Modules
import pygame


class UI:
    def __init__(self, player):
        self.player = player

        # HP Bar:
        self.hp_bar_pos = (1 / 43 * WIDTH, 16 / 17 * HEIGHT)
        self.hp_bar_size = (108, 30)
        self.hp_bar_border_color = (255, 255, 255)  # White
        self.hp_bar_low_color = (255, 49, 49)  # Neon Red
        self.hp_bar_med_color = (255, 165, 0)  # Orange
        self.hp_bar_full_color = (15, 255, 80)  # Neon Green
        self.line_width = 2
        self.border_radius = 4
        self.hp_ref = 27.5
        self.dhp = 0.5

    def show_text(self):
        pass

    def show_bar(self):
        x_1, y_1 = (self.hp_bar_pos[0] + 1 / 3 * self.hp_bar_size[0], self.hp_bar_pos[1])
        x_2, y_2 = (x_1, y_1 + self.hp_bar_size[1] - 1)

        x_3, y_3 = (self.hp_bar_pos[0] + 2 / 3 * self.hp_bar_size[0], y_1)
        x_4, y_4 = (x_3, y_2)

        d_inner_pos = 4
        d_inner_size = 8.5
        inner_pos_1 = (self.hp_bar_pos[0] + 5, self.hp_bar_pos[1] + d_inner_pos)
        inner_pos_2 = (self.hp_bar_pos[0] + self.hp_bar_pos[0] + 1 / 6 * self.hp_bar_size[0], self.hp_bar_pos[1] + d_inner_pos)
        inner_pos_3 = (self.hp_bar_pos[0] + self.hp_bar_pos[0] + 1 / 2 * self.hp_bar_size[0], self.hp_bar_pos[1] + d_inner_pos)
        inner_size_1 = (1 / 3 * self.hp_bar_size[0] - d_inner_size + 1, self.hp_bar_size[1] - d_inner_size)
        inner_size_2 = (1 / 3 * self.hp_bar_size[0] - d_inner_size + 1, self.hp_bar_size[1] - d_inner_size)
        inner_size_3 = (1 / 3 * self.hp_bar_size[0] - d_inner_size, self.hp_bar_size[1] - d_inner_size)

        pygame.draw.line(SCREEN, self.hp_bar_border_color, (x_1, y_1), (x_2, y_2), self.line_width)
        pygame.draw.line(SCREEN, self.hp_bar_border_color, (x_3, y_3), (x_4, y_4), self.line_width)
        pygame.draw.rect(SCREEN, self.hp_bar_border_color, (*self.hp_bar_pos, *self.hp_bar_size), self.line_width, 4)

        if self.player.hp == 3:
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_1, *inner_size_1))
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_2, *inner_size_2))
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_3, *inner_size_3))
        elif self.player.hp == 2:
            if self.player.hp_animation:
                self.hp_ref -= self.dhp
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_2, *inner_size_2))
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_3, self.hp_ref, inner_size_3[1]))
                if self.hp_ref == 0:
                    self.player.hp_animation = False
                    self.hp_ref = 27.5
            else:
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_2, *inner_size_2))

        elif self.player.hp == 1:
            if self.player.hp_animation:
                self.hp_ref -= self.dhp
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_2, self.hp_ref, inner_size_2[1]))
                if self.hp_ref == 0:
                    self.player.hp_animation = False
                    self.hp_ref = 27.5
            else:
                pygame.draw.rect(SCREEN, self.hp_bar_low_color, (*inner_pos_1, *inner_size_1))

        elif self.player.hp == 0:
            if self.player.hp_animation:
                self.hp_ref -= self.dhp
                pygame.draw.rect(SCREEN, self.hp_bar_low_color, (*inner_pos_1, self.hp_ref, inner_size_1[1]))
                if self.hp_ref == 0:
                    self.player.hp_animation = False
                    self.hp_ref = 27.5

    def draw(self):
        self.show_bar()
