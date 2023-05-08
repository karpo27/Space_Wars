# Scripts:
from constants import *
import constants

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

        # Movement:
        self.ref_time = 16
        self.movement_rate = 16
        self.allow_movement_speed = 1

        # Create Text:
        self.margin = 70
        self.menu_qty = 2
        self.padding_x, self.padding_y = 0, 50
        self.init_pos_y = 30
        self.pos_y = 30
        self.pause_resume = TextCreator(0, "RESUME", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                                   (self.rect_x + self.width/2 + self.padding_x, self.rect_y + self.padding_y), "", 70)
        self.pause_options = TextCreator(1, "OPTIONS", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                                    (self.rect_x + + self.width/2 + self.padding_x, self.rect_y + self.padding_y), "", 70)
        self.pause_quit = TextCreator(2, "QUIT", 'freesansbold.ttf', 48, 48, (255, 255, 255), (193, 225, 193),
                                 (self.rect_x + self.width/2 + self.padding_x, self.rect_y + self.padding_y), "", 70)

    def update(self):
        # Draw the Rectangle Screen and Border:
        pygame.draw.rect(SCREEN, self.fill_color, (self.rect_x, self.rect_y, self.width, self.height))
        pygame.draw.rect(SCREEN, self.border_color, (self.rect_x, self.rect_y, self.width, self.height), self.border_width)

        # Render Pause Menu Text:
        self.pause_resume.update()
        self.pause_options.update()
        self.pause_quit.update()
        for text in [self.pause_resume, self.pause_options, self.pause_quit]:
            text.render_text(self.pos_y)

        # Keyboard Actions:
        key = pygame.key.get_pressed()
        # Main Menu Movement:
        if key[pygame.K_DOWN] and self.movement_rate >= self.ref_time:
            self.pos_y += self.margin
            self.movement_rate = 0
        elif key[pygame.K_UP] and self.movement_rate >= self.ref_time:
            self.pos_y -= self.margin
            self.movement_rate = 0

        # Pause Menu Selection:
        elif key[pygame.K_RETURN] and self.movement_rate >= self.ref_time:
            if self.pos_y == self.init_pos_y:  # Position 1
                constants.game_screen = "play"
            elif self.pos_y == self.init_pos_y + self.margin:  # Position 2
                constants.game_screen = "options"
            elif self.pos_y == self.init_pos_y + 2 * self.margin:  # Position 3
                constants.game_screen = "main menu"

        # Reset Variables:
        if self.movement_rate < self.ref_time:
            self.movement_rate += self.allow_movement_speed

        # Player Icon Movement Boundaries:
        if self.pos_y > self.init_pos_y + self.menu_qty * self.margin:
            self.pos_y = self.init_pos_y
        if self.pos_y < self.init_pos_y:
            self.pos_y = self.init_pos_y + self.menu_qty * self.margin


# Initialize Classes:
pause_menu = PauseMenu([300, 320], [WIDTH/2, HEIGHT/2], (0, 0, 0), (255, 255, 255), 5)

