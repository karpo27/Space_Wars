# Scripts:
from constants import *
from base_state import BaseState
from submenus import Options, Controls, audio
from pointer import Pointer
from sound import menu_bg, menu_selection, menu_movement, menu_back
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

        # Initialize Objects:
        self.background = BGCreator(*BACKGROUNDS['level_1'])
        self.options = Options()
        self.controls = Controls()
        self.pointer = Pointer()

    def handle_movement(self, movement):
        self.index += movement
        if self.options_qty >= 1:
            menu_movement.play_sound()

    def handle_action(self):
        if self.screen == "PAUSE":
            if self.index == 0:
                self.next_state = "LEVEL_1"
                self.screen_done = True
                pygame.mixer.music.unpause()
            elif self.index == 1:
                self.screen = "OPTIONS"
                self.index = 0
                menu_selection.play_sound()
            elif self.index == 2:
                self.next_state = "MENU"
                self.index = 0
                self.screen_done = True
                menu_selection.play_sound()
                menu_bg.play_bg_music(-1)
        elif self.screen == "OPTIONS":
            if self.index == 0:
                self.screen = "AUDIO"
                self.index = 0
                self.options_qty = 2
                menu_selection.play_sound()
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
                self.options_qty = 0
                menu_selection.play_sound()
            elif self.index == 2:
                self.screen = "PAUSE"
                self.index = 1
                menu_back.play_sound()
        elif self.screen == "AUDIO":
            self.screen = "OPTIONS"
            self.index = 0
            self.options_qty = 2
            menu_back.play_sound()
        elif self.screen == "CONTROLS":
            self.screen = "OPTIONS"
            self.index = 1
            self.options_qty = 2
            menu_back.play_sound()

    def handle_left_audio(self):
        if self.index == 0:
            if audio.sound_volume > 0:
                audio.update_volume(-1, "sound")
        elif self.index == 1:
            if audio.music_volume > 0:
                audio.update_volume(-1, "music")

    def handle_right_audio(self):
        if self.index == 0:
            if audio.sound_volume < 10:
                audio.update_volume(1, "sound")
        elif self.index == 1:
            if audio.music_volume < 10:
                audio.update_volume(1, "music")

    def get_event(self, event):
        # Pause Menu Movement:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                self.handle_movement(1)
            elif event.key == pygame.K_UP:
                self.handle_movement(-1)
            elif event.key == pygame.K_RETURN:
                self.handle_action()
            elif event.key == pygame.K_LEFT and self.screen == "AUDIO":
                self.handle_left_audio()
            elif event.key == pygame.K_RIGHT and self.screen == "AUDIO":
                self.handle_right_audio()

        # Pointer Movement Boundaries:
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
            for text in audio.audio:
                text.render_text(self.index)
            self.pointer.draw_rotated(audio.audio[self.index].text_position, self.screen)
        elif self.screen == "CONTROLS":
            for text in self.controls.controls:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.controls.controls[self.index].text_position, self.screen)

