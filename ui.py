# Scripts:
from constants import *
from base_state import BaseState
from text_creator import TextCreator

# Modules:
import pygame


class UI(BaseState):
    def __init__(self, player):
        super().__init__()
        self.player = player

        # Score:
        self.score = 0
        self.score_pos = 1 / 43 * WIDTH + 55, 14 / 17 * HEIGHT + 22

        # Lives:
        self.image = player.image
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * 0.6, self.image.get_height() * 0.6))
        self.rect = self.image.get_rect()
        self.rect.center = 1 / 43 * WIDTH, 15 / 17 * HEIGHT
        self.lives_pos = 1 / 43 * WIDTH + 58, 15 / 17 * HEIGHT + 22

        # HP Bar:
        self.pos = (1 / 43 * WIDTH, 16 / 17 * HEIGHT)
        self.size = (108, 30)
        self.border_color = "white"  # White
        self.low_color = (255, 49, 49)  # Neon Red
        self.med_color = (255, 165, 0)  # Orange
        self.full_color = (15, 255, 80)  # Neon Green
        self.line_width = 2
        self.border_radius = 4
        self.ref = 27.5
        self.dhp = 0.5

    def update_score(self, value):
        self.score += value

    def show_score(self):
        text_score = TextCreator(0, f'Score: {str(self.score)}', self.font_type, 26, 26, self.base_color, None,
                                 self.score_pos, "", 0)
        text_score.render_text(-1)

    def show_lives(self):
        text_lives = TextCreator(0, f'x {str(self.player.lives)}', self.font_type, 26, 26, self.base_color, None,
                                 self.lives_pos, "", 0)
        text_lives.render_text(-1)
        SCREEN.blit(self.image, self.rect.center)

    def show_bar(self):
        x_1, y_1 = (self.pos[0] + 1 / 3 * self.size[0], self.pos[1])
        x_2, y_2 = (x_1, y_1 + self.size[1] - 1)

        x_3, y_3 = (self.pos[0] + 2 / 3 * self.size[0], y_1)
        x_4, y_4 = (x_3, y_2)

        d_inner_pos = 4
        d_inner_size = 8.5
        inner_pos_1 = (self.pos[0] + 5, self.pos[1] + d_inner_pos)
        inner_pos_2 = (self.pos[0] + self.pos[0] + 1 / 6 * self.size[0], self.pos[1] + d_inner_pos)
        inner_pos_3 = (self.pos[0] + self.pos[0] + 1 / 2 * self.size[0], self.pos[1] + d_inner_pos)
        inner_size_1 = (1 / 3 * self.size[0] - d_inner_size + 1, self.size[1] - d_inner_size)
        inner_size_2 = (1 / 3 * self.size[0] - d_inner_size + 1, self.size[1] - d_inner_size)
        inner_size_3 = (1 / 3 * self.size[0] - d_inner_size, self.size[1] - d_inner_size)

        if self.player.lives >= 0:
            pygame.draw.line(SCREEN, self.border_color, (x_1, y_1), (x_2, y_2), self.line_width)
            pygame.draw.line(SCREEN, self.border_color, (x_3, y_3), (x_4, y_4), self.line_width)
            pygame.draw.rect(SCREEN, self.border_color, (*self.pos, *self.size), self.line_width, 4)
            if self.player.hp == 3:
                pygame.draw.rect(SCREEN, self.full_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.full_color, (*inner_pos_2, *inner_size_2))
                pygame.draw.rect(SCREEN, self.full_color, (*inner_pos_3, *inner_size_3))
            elif self.player.hp == 2:
                if self.player.hp_animation:
                    self.ref -= self.dhp
                    pygame.draw.rect(SCREEN, self.full_color, (*inner_pos_1, *inner_size_1))
                    pygame.draw.rect(SCREEN, self.full_color, (*inner_pos_2, *inner_size_2))
                    pygame.draw.rect(SCREEN, self.full_color, (*inner_pos_3, self.ref, inner_size_3[1]))
                    if self.ref == 0:
                        self.player.hp_animation = False
                        self.ref = 27.5
                else:
                    pygame.draw.rect(SCREEN, self.med_color, (*inner_pos_1, *inner_size_1))
                    pygame.draw.rect(SCREEN, self.med_color, (*inner_pos_2, *inner_size_2))
            elif self.player.hp == 1:
                if self.player.hp_animation:
                    self.ref -= self.dhp
                    pygame.draw.rect(SCREEN, self.med_color, (*inner_pos_1, *inner_size_1))
                    pygame.draw.rect(SCREEN, self.med_color, (*inner_pos_2, self.ref, inner_size_2[1]))
                    if self.ref == 0:
                        self.player.hp_animation = False
                        self.ref = 27.5
                else:
                    pygame.draw.rect(SCREEN, self.low_color, (*inner_pos_1, *inner_size_1))
            elif self.player.hp == 0:
                if self.player.hp_animation:
                    self.ref -= self.dhp
                    pygame.draw.rect(SCREEN, self.low_color, (*inner_pos_1, self.ref, inner_size_1[1]))
                    if self.ref == 0:
                        self.player.hp_animation = False
                        self.ref = 27.5

    def draw(self, surface):
        self.show_score()
        self.show_bar()
        self.show_lives()
