# Scripts:
from base_state import BaseState
from submenus import Options, Controls, Credits, audio
from pointer import Pointer
from sound import level1_bg, menu_movement, menu_selection, menu_back
from bg_creator import *
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
        # Initialize Objects:
        self.background = BGCreator(*BACKGROUNDS['main_menu'])
        self.options = Options()
        self.controls = Controls()
        self.credits = Credits()
        self.pointer = Pointer()

        # Title and Icon:
        pygame.display.set_caption("Menu")
        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

    def handle_movement(self, movement):
        self.index += movement
        if self.options_qty >= 1:
            menu_movement.play_sound()

    def handle_action(self):
        if self.screen == "MENU":
            if self.index == 0:
                level1_bg.play_bg_music(-1)
                self.screen_done = True
            elif self.index == 1:
                self.screen = "OPTIONS"
                self.index = 0
                self.options_qty = 2
                menu_selection.play_sound()
            elif self.index == 2:
                self.screen = "CREDITS"
                self.options_qty = 0
                menu_selection.play_sound()
            elif self.index == 3:
                self.quit = True
        elif self.screen == "OPTIONS":
            if self.index == 0:
                self.screen = "AUDIO"
                self.index = 0
                self.options_qty = 2
                menu_selection.play_sound()
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
                menu_selection.play_sound()
                self.options_qty = 0
            elif self.index == 2:
                self.screen = "MENU"
                self.index = 1
                self.options_qty = 3
                menu_back.play_sound()
        elif self.screen == "CREDITS":
            self.screen = "MENU"
            self.index = 2
            self.options_qty = 3
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
        # Main Menu Movement:
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
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
            for text in audio.audio:
                text.render_text(self.index)
            self.pointer.draw_rotated(audio.audio[self.index].text_position, self.screen)
        elif self.screen == "CONTROLS":
            for text in self.controls.controls:
                text.render_text(self.index)
            self.pointer.draw_rotated(self.controls.controls[self.index].text_position, self.screen)
