# Scripts:
import sys
from sounds import *
from background_creator import *
from text_creator import *
import level_1
from player import *

# Modules:
import pygame

# Initialize Fonts:
pygame.init()
pygame.font.init()


class MainMenu(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
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

        # Text:
        self.margin = 70
        self.menu_qty = 3

        # Movement:
        self.indicator = "main menu"
        self.ref_time = 16
        self.movement_rate = 16
        self.allow_movement_speed = 1

    def run(self):
        # Game Loop:
        run = True
        while run:
            # Set screen FPS:
            clock.tick(FPS)

            # Draw Scrolling Background:
            background_main_menu.update()

            # Render Main Menu Text:
            if self.indicator == "main menu":
                title_text.update()
                play_text.update()
                options_text.update()
                credits_text.update()
                quit_text.update()
                for text in [play_text, options_text, credits_text, quit_text]:
                    text.change_color(self.pos_y)
            elif self.indicator == "options":
                audio_text.update()
                keybindings_text.update()
                back_text.update()
                for text in [audio_text, keybindings_text, back_text]:
                    text.change_color(self.pos_y)

            # Player Icon Rotation Animation:
            rot_player_img = pygame.transform.rotozoom(self.image, self.angle, 1)
            rot_player_img_rect = rot_player_img.get_rect()
            rot_player_img_position = (
                play_text.text_position[0] - self.rect.x - rot_player_img_rect.width / 2,
                play_text.text_position[1] + self.pos_y - rot_player_img_rect.height / 2
            )
            SCREEN.blit(rot_player_img, rot_player_img_position)
            self.angle += 2.2

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            # Keyboard Actions:
            key = pygame.key.get_pressed()
            # Main Menu Movement:
            if key[pygame.K_DOWN] and self.movement_rate >= self.ref_time:
                self.pos_y += self.margin
                self.movement_rate = 0
                # channel2.play(sounds['main_menu'][1])
            elif key[pygame.K_UP] and self.movement_rate >= self.ref_time:
                self.pos_y -= self.margin
                self.movement_rate = 0
                # channel2.play(sounds['main_menu'][1])

            # Main Menu Selection:
            elif key[pygame.K_RETURN] and self.movement_rate >= self.ref_time:
                if self.pos_y == self.init_pos_y:  # Position 1
                    if self.indicator == "main menu":
                        self.indicator = "play"
                        run = False
                        if level_1.game_state == "play":
                            level_1.run_level_1()
                        elif level_1.game_state == "paused":
                            pass
                    elif self.indicator == "options":
                        self.indicator = "audio"
                elif self.pos_y == self.init_pos_y + self.margin:  # Position 2
                    if self.indicator == "main menu":
                        self.indicator = "options"
                        self.rect.center = self.pos_x, self.pos_y = 85, 30
                        self.menu_qty = 2
                    elif self.indicator == "options":
                        self.indicator = "keybindings"
                elif self.pos_y == self.init_pos_y + 2 * self.margin:  # Position 3
                    if self.indicator == "main menu":
                        self.indicator = "credits"
                    elif self.indicator == "options":
                        self.indicator = "main menu"
                        self.rect.center = self.pos_x, self.pos_y = 70, 30
                        self.menu_qty = 3
                elif self.pos_y == self.init_pos_y + 3 * self.margin:  # Position 4
                    if self.indicator == "main menu":
                        pygame.quit()
                        sys.exit()
                self.movement_rate = 0

            # Reset Variables:
            if self.movement_rate < self.ref_time:
                self.movement_rate += self.allow_movement_speed

            # Player Icon Movement Boundaries:
            if self.pos_y > self.init_pos_y + self.menu_qty * self.margin:
                self.pos_y = self.init_pos_y
            if self.pos_y < self.init_pos_y:
                self.pos_y = self.init_pos_y + self.menu_qty * self.margin

            # Apply Changes:
            pygame.display.update()


# Initialize Classes:
main_menu = MainMenu()

# Run Main Menu:
main_menu.run()

