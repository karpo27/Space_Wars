# Scripts
from constants import *

# Modules
import pygame

# Initialize Fonts
pygame.font.init()


class TextCreator:
    def __init__(self, text, font, font_size, color, pos, align_text, margin, k):
        # Text Font, Size and Color
        self.text = text
        self.font = font
        self._font_size = font_size
        self._color = color

        self.font_and_size = pygame.font.Font(font, self._font_size)
        self.text_and_color = self.font_and_size.render(self.text, True, self._color)
        self.text_rect = self.text_and_color.get_rect()

        # Text Align and Position
        self.text_width, self.text_height = self.font_and_size.size(align_text)
        self.text_position = [pos[0] - self.text_width/2, pos[1] - self.text_height/2 + margin * k]

    def show(self):
        SCREEN.blit(self.text_and_color, self.text_position)

    @property
    def font_size(self):
        return self._font_size

    @font_size.setter
    def font_size(self, hover_size):
        self._font_size = hover_size
        self.font_and_size = pygame.font.Font(self.font, self._font_size)
        self.text_and_color = self.font_and_size.render(self.text, True, self._color)

    @property
    def color(self):
        return self._color

    @color.setter
    def color(self, hover_color):
        self._color = hover_color
        self.text_and_color = self.font_and_size.render(self.text, True, self._color)


# Initialize Classes:
title_text = TextCreator("GAME PROJECT", 'freesansbold.ttf', 94, (255, 255, 255), (WIDTH/2, 1/3 * HEIGHT), "GAME PROJECT", 0, 0)
play_text = TextCreator("PLAY", 'freesansbold.ttf', 48, (255, 255, 255), (WIDTH/2, 3/5 * HEIGHT), "PLAY", 0, 0)
load_text = TextCreator("LOAD", 'freesansbold.ttf', 48, (255, 255, 255), (WIDTH/2, 3/5 * HEIGHT), "PLAY", 70, 1)
options_text = TextCreator("OPTIONS", 'freesansbold.ttf', 48, (255, 255, 255), (WIDTH/2, 3/5 * HEIGHT), "PLAY", 70, 2)
quit_text = TextCreator("QUIT", 'freesansbold.ttf', 48, (255, 255, 255), (WIDTH/2, 3/5 * HEIGHT), "PLAY", 70, 3)

# Main Menu List:
main_menu_list = [play_text, load_text, options_text, quit_text]

