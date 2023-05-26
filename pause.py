# Scripts:
from constants import *
from base_state import BaseState
from submenus import Options, Audio, Controls
from pointer import Pointer
from bg_music import set_bg_music
from bg_creator import *

# Modules:
import pygame
from text_creator import TextCreator


class Pause(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.screen = "PAUSE"
        self.options_qty = 2
        self.text = ["RESUME", "OPTIONS", "BACK TO MENU"]
        self.pause = []
        for index, text in enumerate(self.text):
            self.pause.append(
                TextCreator(index, text, self.font_type, 48, 52, self.base_color, self.hover_color, self.pos,
                            self.text[0], 70))

        # Initialize Classes:
        self.background = BGCreator(*BACKGROUNDS['level_1'])
        self.options = Options()
        self.audio = Audio(self.volume)
        self.controls = Controls()
        self.pointer = Pointer()

    def handle_action(self):
        if self.screen == "PAUSE":
            if self.index == 0:
                self.next_state = "LEVEL_1"
                self.screen_done = True
                pygame.mixer.music.unpause()
            elif self.index == 1:
                self.screen = "OPTIONS"
                self.index = 0
                SOUNDS['menu_selection'].play().set_volume(VOL_MENU_SELECTION)
            elif self.index == 2:
                self.next_state = "MENU"
                self.index = 0
                self.screen_done = True
                SOUNDS['menu_selection'].play().set_volume(VOL_MENU_SELECTION)
                set_bg_music(SOUNDS['menu_bg'], VOL_MENU_BG, -1)
        elif self.screen == "OPTIONS":
            if self.index == 0:
                self.screen = "AUDIO"
                self.index = 0
                self.options_qty = 1
                SOUNDS['menu_selection'].play().set_volume(VOL_MENU_SELECTION)
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
                self.options_qty = 0
                SOUNDS['menu_selection'].play().set_volume(VOL_MENU_SELECTION)
            elif self.index == 2:
                self.screen = "PAUSE"
                self.index = 1
                SOUNDS['menu_back'].play().set_volume(VOL_MENU_BACK)
        elif self.screen == "AUDIO":
            self.screen = "OPTIONS"
            self.index = 0
            self.options_qty = 2
            SOUNDS['menu_back'].play().set_volume(VOL_MENU_BACK)
        elif self.screen == "CONTROLS":
            self.screen = "OPTIONS"
            self.index = 1
            self.options_qty = 2
            SOUNDS['menu_back'].play().set_volume(VOL_MENU_BACK)

    def get_event(self, event):
        # Pause Menu Movement:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.index += 1
                SOUNDS['menu_movement'].play().set_volume(VOL_MENU_MOVEMENT)
            elif event.key == pygame.K_UP:
                self.index -= 1
                SOUNDS['menu_movement'].play().set_volume(VOL_MENU_MOVEMENT)
            elif event.key == pygame.K_RETURN:
                self.handle_action()

        # Player Icon Movement Boundaries:
        if self.index > self.options_qty:
            self.index = 0
        elif self.index < 0:
            self.index = self.options_qty

    def draw(self, surface):
        # Draw Background
        self.background.update()

        # Render Pause Menu:
        if self.screen == "PAUSE":
            for text in self.pause:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.pause[self.index].text_position, self.screen)
        elif self.screen == "OPTIONS":
            for text in self.options.options:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.options.options[self.index].text_position, self.screen)
        elif self.screen == "AUDIO":
            for text in self.audio.audio:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.audio.audio[self.index].text_position, self.screen)
        elif self.screen == "CONTROLS":
            for text in self.controls.controls:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.controls.controls[self.index].text_position, self.screen)

