# Scripts
from constants import *

# Modules
import pygame

# Initialize Fonts
pygame.font.init()


class TextCreator:
    def __init__(self, index, text, font, font_size, hover_font_size, base_color, hover_color, pos, align_text, margin):
        # Text Font, Size and Color
        self.text = text
        self.font = font
        self.font_size = font_size
        self.hover_font_size = hover_font_size
        self.base_color = base_color
        self.hover_color = hover_color

        self.font_and_size = pygame.font.Font(self.font, self.font_size)
        self.text_and_color = self.font_and_size.render(self.text, True, self.base_color)
        self.text_rect = self.text_and_color.get_rect()

        # Text Align and Position
        self.pos = pos
        self.margin = margin
        self.index = index
        if align_text:
            self.text_width, self.text_height = self.font_and_size.size(align_text)
        else:
            self.text_width, self.text_height = self.font_and_size.size(text)

        self.text_position = [self.pos[0] - self.text_width / 2, self.pos[1] - self.text_height / 2 + self.margin * self.index]

    def render_text(self, index):
        if index == self.index:
            self.font_and_size = pygame.font.Font(self.font, self.hover_font_size)
            self.text_and_color = self.font_and_size.render(self.text, True, self.hover_color)
            SCREEN.blit(self.text_and_color, self.text_position)
        else:
            self.font_and_size = pygame.font.Font(self.font, self.font_size)
            self.text_and_color = self.font_and_size.render(self.text, True, self.base_color)
            SCREEN.blit(self.text_and_color, self.text_position)


# Initialize Classes:


audio = TextCreator(0, "AUDIO", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "AUDIO", 70)
keybindings = TextCreator(1, "KEYBINDINGS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "AUDIO", 70)
back = TextCreator(2, "BACK", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193), (WIDTH / 2, 3 / 5 * HEIGHT), "AUDIO", 70)

#pause_resume = TextCreator("RESUME", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH/2, 3/5 * HEIGHT), "", 0, 0)
#pause_options = TextCreator("OPTIONS", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH/2, 3/5 * HEIGHT), "", 70, 1)
#pause_quit = TextCreator("QUIT", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193), (WIDTH/2, 3/5 * HEIGHT), "", 70, 2)

