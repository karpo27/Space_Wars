# Scripts:
import constants
from base_state import BaseState
from options import Options
from audio import Audio
from controls import Controls
from credits import Credits
from sounds import *
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
        self.options_qty = 3
        self.index = 0
        self.screen = "MENU"
        self.title = TextCreator(0, "GAME PROJECT", 'freesansbold.ttf', 94, 94, (255, 255, 255), (193, 225, 193),
                                 (WIDTH / 2, 1 / 3 * HEIGHT), "GAME PROJECT", 70)
        self.menu = [
            TextCreator(0, "PLAY", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70),
            TextCreator(1, "OPTIONS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70),
            TextCreator(2, "CREDITS", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70),
            TextCreator(3, "QUIT", 'freesansbold.ttf', 48, 52, (255, 255, 255), (193, 225, 193),
                        (WIDTH / 2, 3 / 5 * HEIGHT), "PLAY", 70)
        ]

        # Initialize Classes:
        self.options = Options()
        self.audio = Audio()
        self.controls = Controls()
        self.credits = Credits()

        # Title and Icon:
        pygame.display.set_caption("Main Menu")
        icon = pygame.image.load(ICON)
        pygame.display.set_icon(icon)

        # Player Icon:
        self.image = pygame.image.load('Images/Player/player_img.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_x, self.pos_y = 70, 30
        self.angle = 0
        self.init_pos_y = 30

    def handle_action(self):
        if self.screen == "MENU":
            if self.index == 0:
                self.screen_done = True
            elif self.index == 1:
                self.index = 0
                self.screen = "OPTIONS"
                self.rect.center = self.pos_x, self.pos_y = 85, 30
                self.options_qty = 2
            elif self.index == 2:
                self.options_qty = 0
                self.screen = "CREDITS"
                self.rect.center = self.pos_x, self.pos_y = 70, 30
            elif self.index == 3:
                self.quit = True
        elif self.screen == "OPTIONS":
            if self.index == 0:
                self.rect.center = self.pos_x, self.pos_y = 85, 30
                self.options_qty = 2
            elif self.index == 1:
                self.screen = "CONTROLS"
                self.index = 0
            elif self.index == 2:
                self.index = 1
                self.screen = "MENU"
                self.rect.center = self.pos_x, self.pos_y = 70, 30
                self.options_qty = 3
        elif self.screen == "CREDITS":
            self.index = 2
            self.screen = "MENU"
            self.rect.center = self.pos_x, self.pos_y = 70, 30
            self.options_qty = 3
        elif self.screen == "CONTROLS":
            self.index = 1
            self.screen = "OPTIONS"
            self.rect.center = self.pos_x, self.pos_y = 85, 30
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

    def rotate_pointer(self, position):
        # Render Player Icon Rotation:
        rot_player_img = pygame.transform.rotozoom(self.image, self.angle, 1)
        rot_player_img_rect = rot_player_img.get_rect()
        rot_player_img_position = (
            position.text_position[0] - self.rect.x - rot_player_img_rect.width / 2,
            position.text_position[1] + self.init_pos_y - rot_player_img_rect.height / 2
        )
        SCREEN.blit(rot_player_img, rot_player_img_position)
        self.angle += 2.2

    def draw(self, surface):
        # Draw Scrolling Background:
        background_main_menu.update()

        # Render Main Menu Text:
        if self.screen == "MENU":
            self.title.render_text(-1)
            for text in self.menu:
                text.render_text(self.index)
            self.rotate_pointer(self.menu[self.index])
        elif self.screen == "OPTIONS":
            for text in self.options.options:
                text.render_text(self.index)
            self.rotate_pointer(self.menu[self.index])
        elif self.screen == "CREDITS":
            for text in self.credits.credits:
                text.render_text(self.index)
            self.rotate_pointer(self.credits.credits[self.index])
        elif self.screen == "CONTROLS":
            self.controls.draw()

