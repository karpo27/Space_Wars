# Scripts:
import constants
from base_state import BaseState
from options import Options
from audio import Audio
from controls import Controls
from credits import Credits
from pointer import Pointer
from background_creator import *
from text_creator import *
from sounds import *

# Modules:
import pygame


class Menu(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "LEVEL_1"

        # Screen Text and Options:
        self.screen = "MENU"
        self.options_qty = 3
        self.index = 0
        self.pos_x, self.pos_y = WIDTH/2, 3/5 * HEIGHT
        self.margin = 70
        self.title = TextCreator(0, "GAME PROJECT", 'freesansbold.ttf', 94, 94, (255, 255, 255), (193, 225, 193),
                                 (WIDTH/2, HEIGHT/3), "GAME PROJECT", self.margin)
        self.menu = [
            TextCreator(0, "PLAY", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "PLAY", self.margin),
            TextCreator(1, "OPTIONS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "PLAY", self.margin),
            TextCreator(2, "CREDITS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "PLAY", self.margin),
            TextCreator(3, "QUIT", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (self.pos_x, self.pos_y), "PLAY", self.margin)
        ]
        # Initialize Classes:
        self.options = Options()
        self.audio = Audio()
        self.controls = Controls()
        self.credits = Credits()
        self.pointer = Pointer()

        # Title and Icon:
        pygame.display.set_caption("Menu")
        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

    def handle_action(self):
        if self.screen == "MENU":
            if self.index == 0:
                self.screen_done = True
            elif self.index == 1:
                self.index = 0
                self.screen = "OPTIONS"
                self.options_qty = 2
            elif self.index == 2:
                self.options_qty = 0
                self.screen = "CREDITS"
            elif self.index == 3:
                self.quit = True
        elif self.screen == "OPTIONS":
            if self.index == 0:
                self.options_qty = 2
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
            elif self.index == 2:
                self.index = 1
                self.screen = "MENU"
                self.options_qty = 3
        elif self.screen == "CREDITS":
            self.index = 2
            self.screen = "MENU"
            self.options_qty = 3
        elif self.screen == "CONTROLS":
            self.index = 1
            self.screen = "OPTIONS"
            self.options_qty = 2

    def get_event(self, event):
        # Main Menu Movement:
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.index += 1
                # channel2.play(sounds['main_menu'][1])
            elif event.key == pygame.K_UP:
                self.index -= 1
                # channel2.play(sounds['main_menu'][1])
            elif event.key == pygame.K_RETURN:
                self.handle_action()

        # Player Icon Movement Boundaries:
        if self.index > self.options_qty:
            self.index = 0
        elif self.index < 0:
            self.index = self.options_qty

    def draw(self, surface):
        # Draw Background:
        background_main_menu.update()

        # Render Main Menu:
        if self.screen == "MENU":
            self.title.render_text(-1)
            for text in self.menu:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.menu[self.index].text_position, self.screen)
        elif self.screen == "OPTIONS":
            for text in self.options.options:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.options.options[self.index].text_position, self.screen)
        elif self.screen == "CREDITS":
            for text in self.credits.credits:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.credits.credits[self.index].text_position, self.screen)
        elif self.screen == "CONTROLS":
            for text in self.controls.controls:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.controls.controls[self.index].text_position, self.screen)
