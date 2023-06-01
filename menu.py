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

        # Logo:
        self.image = pygame.image.load(f'{LOGO_PATH}').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = [WIDTH / 2 - 380, HEIGHT / 11]

        # Screen Text and Options:
        self.screen = "MENU"
        self.options_qty = 3
        self.text = ["PLAY", "OPTIONS", "CREDITS", "QUIT"]
        self.menu = []
        self.allow_movement = False
        for index, text in enumerate(self.text):
            self.menu.append(TextCreator(index, text, self.font_type, 48, 52, self.base_color, self.hover_color, self.pos, self.text[0], 70))

        # Initialize Objects:
        self.background = BGCreator(*BACKGROUNDS['main_menu'])
        self.options = Options()
        self.controls = Controls()
        self.credits = Credits()
        self.pointer = Pointer()

        # Empty Surface:
        self.empty_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        self.alpha = 0

        # Time on Screen:
        self.time = 0
        self.time_start_render = 40     # 40 ms
        self.time_finish_render = self.time_start_render + 215      # 215 ms
        self.time_render_options = self.time_finish_render + 60     # 60 ms

        # Title and Icon:
        pygame.display.set_caption("Menu")
        icon = pygame.image.load(ICON_PATH)
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

    def render_logo(self):
        self.empty_surface.set_alpha(self.alpha)
        self.empty_surface.fill((255, 255, 255, self.alpha), special_flags=pygame.BLEND_RGBA_MULT)
        self.empty_surface.blit(self.image, (0, 0))
        SCREEN.blit(self.empty_surface, self.rect.center)

    def get_event(self, event):
        # Main Menu Movement:
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN and self.allow_movement:
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
        self.background.draw()
        # Render Menu:
        if self.screen == "MENU":
            if self.time_start_render < self.time <= self.time_finish_render:
                if self.alpha <= 215:
                    self.render_logo()
                    self.alpha += 1
            elif self.time_finish_render < self.time <= self.time_render_options:
                SCREEN.blit(self.empty_surface, self.rect.center)
            elif self.time > self.time_render_options:
                SCREEN.blit(self.empty_surface, self.rect.center)
                for text in self.menu:
                    text.render_text(self.index)
                self.pointer.draw_rotated(self.menu[self.index].text_position, self.screen)
                self.allow_movement = True
            self.time += 1
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
