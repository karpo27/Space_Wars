# Scripts:
from constants import *

# Modules:
import pygame
from text_creator import TextCreator

# Initialize Pygame
pygame.init()


class PauseMenu:
    def __init__(self, dimensions, pos, fill_color, border_color, border_width):
        # Set up rectangle dimensions
        self.width, self.height = dimensions[0], dimensions[1]
        self.rect_x, self.rect_y = pos[0] - self.width/2, pos[1] - self.height/2
        self.border_width = border_width

        # Set up colors
        self.fill_color = fill_color
        self.border_color = border_color

        # Create Text:
        self.padding_x, self.padding_y = 0, 50
        self.pause_resume = TextCreator("RESUME", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193),
                                   (self.rect_x + self.width/2 + self.padding_x, self.rect_y + self.padding_y), "", 0, 0)
        self.pause_options = TextCreator("OPTIONS", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193),
                                    (self.rect_x + + self.width/2 + self.padding_x, self.rect_y + self.padding_y), "", 70, 1)
        self.pause_quit = TextCreator("QUIT", 'freesansbold.ttf', 48, (255, 255, 255), (193, 225, 193),
                                 (self.rect_x + self.width/2 + self.padding_x, self.rect_y + self.padding_y), "", 70, 2)

    def update(self):
        # Draw the rectangle and border
        pygame.draw.rect(SCREEN, self.fill_color, (self.rect_x, self.rect_y, self.width, self.height))
        pygame.draw.rect(SCREEN, self.border_color, (self.rect_x, self.rect_y, self.width, self.height), self.border_width)

        self.pause_resume.update()
        self.pause_options.update()
        self.pause_quit.update()


# Initialize Classes:
pause_menu = PauseMenu([300, 400], [WIDTH/2, HEIGHT/2], (0, 0, 0), (255, 255, 255), 5)

