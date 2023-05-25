# Scripts:
import constants
from base_state import BaseState
from submenus import Options, Controls, Credits
from pointer import Pointer
from background_creator import *
from text_creator import *

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
        self.text = ["PLAY", "OPTIONS", "CREDITS", "QUIT"]
        self.menu = []
        for index, text in enumerate(self.text):
            self.menu.append(TextCreator(index, text, self.font_type, 48, 52, self.base_color, self.hover_color, self.pos, self.text[0], 70))

        self.title = TextCreator(0, "GAME PROJECT", self.font_type, 94, 94, self.base_color, self.hover_color,
                                 (WIDTH/2, HEIGHT/3), "GAME PROJECT", 70)
        # Initialize Classes:
        self.background = BackgroundCreator(*BACKGROUNDS['main_menu'])
        self.options = Options()
        self.controls = Controls()
        self.credits = Credits()
        self.pointer = Pointer()

        # Background Music:
        pygame.mixer.music.load(SOUNDS['menu_background'])
        pygame.mixer.music.set_volume(0.02)
        pygame.mixer.music.play(-1)

        # Title and Icon:
        pygame.display.set_caption("Menu")
        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

    def handle_action(self):
        if self.screen == "MENU":
            if self.index == 0:
                pygame.mixer.music.load(SOUNDS['level1_background'])
                pygame.mixer.music.set_volume(0.3)
                pygame.mixer.music.play()
                self.screen_done = True
            elif self.index == 1:
                self.index = 0
                self.screen = "OPTIONS"
                self.options_qty = 2
                SOUNDS['menu_selection'].play().set_volume(0.3)
            elif self.index == 2:
                self.options_qty = 0
                self.screen = "CREDITS"
                SOUNDS['menu_selection'].play().set_volume(0.3)
            elif self.index == 3:
                self.quit = True
        elif self.screen == "OPTIONS":
            if self.index == 0:
                self.options_qty = 2
                SOUNDS['menu_selection'].play().set_volume(0.3)
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
                SOUNDS['menu_selection'].play().set_volume(0.3)
                self.options_qty = 0
            elif self.index == 2:
                self.index = 1
                self.screen = "MENU"
                self.options_qty = 3
                SOUNDS['menu_back'].play().set_volume(0.3)
        elif self.screen == "CREDITS":
            self.index = 2
            self.screen = "MENU"
            self.options_qty = 3
            SOUNDS['menu_back'].play().set_volume(0.3)
        elif self.screen == "CONTROLS":
            self.index = 1
            self.screen = "OPTIONS"
            self.options_qty = 2
            SOUNDS['menu_back'].play().set_volume(0.3)

    def get_event(self, event):
        # Main Menu Movement:
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.index += 1
                SOUNDS['menu_movement'].play().set_volume(0.5)
            elif event.key == pygame.K_UP:
                self.index -= 1
                SOUNDS['menu_movement'].play().set_volume(0.5)
            elif event.key == pygame.K_RETURN:
                self.handle_action()

        # Player Icon Movement Boundaries:
        if self.index > self.options_qty:
            self.index = 0
        elif self.index < 0:
            self.index = self.options_qty

    def draw(self, surface):
        # Draw Background:
        self.background.update()

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
        elif self.screen == "AUDIO":
            pass
        elif self.screen == "CONTROLS":
            for text in self.controls.controls:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.controls.controls[self.index].text_position, self.screen)
