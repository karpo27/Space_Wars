# Scripts
from constants import *

# Modules
import pygame

# Initialize Fonts
pygame.font.init()


class TextCreator:
    def __init__(self, text, font, font_size, base_color, hover_color, pos, align_text, margin, k):
        # Text Font, Size and Color
        self.text = text
        self.font = font
        self.font_size = font_size
        self.base_color = base_color
        self.hover_color = hover_color

        self.font_and_size = pygame.font.Font(self.font, self.font_size)
        self.text_and_color = self.font_and_size.render(self.text, True, self.base_color)
        self.text_rect = self.text_and_color.get_rect()

        # Text Align and Position
        self.pos = pos
        self.margin = margin
        self.k = k
        if align_text:
            self.text_width, self.text_height = self.font_and_size.size(align_text)
        else:
            self.text_width, self.text_height = self.font_and_size.size(text)

        self.text_position = [self.pos[0] - self.text_width/2, self.pos[1] - self.text_height/2 + self.margin * self.k]

    def update(self):
        SCREEN.blit(self.text_and_color, self.text_position)

    def change_color(self, position):
        if 30 + self.margin * self.k == position:
            self.font_and_size = pygame.font.Font(self.font, 52)
            self.text_and_color = self.font_and_size.render(self.text, True, self.hover_color)
        else:
            self.font_and_size = pygame.font.Font(self.font, self.font_size)
            self.text_and_color = self.font_and_size.render(self.text, True, self.base_color)


# Initialize Classes:
title = TextCreator("GAME PROJECT", 'freesansbold.ttf', 94, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 1 / 3 * HEIGHT), "GAME PROJECT", 0, 0)
play = TextCreator("PLAY", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 0, 0)
options = TextCreator("OPTIONS", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70, 1)
credits_game = TextCreator("CREDITS", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70, 2)
quit_game = TextCreator("QUIT", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70, 3)

audio = TextCreator("AUDIO", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "AUDIO", 0, 0)
keybindings = TextCreator("KEYBINDINGS", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "AUDIO", 70, 1)
back = TextCreator("BACK", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "AUDIO", 70, 2)

#pause_resume = TextCreator("RESUME", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH/2, 3/5 * HEIGHT), "", 0, 0)
#pause_options = TextCreator("OPTIONS", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH/2, 3/5 * HEIGHT), "", 70, 1)
#pause_quit = TextCreator("QUIT", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH/2, 3/5 * HEIGHT), "", 70, 2)

