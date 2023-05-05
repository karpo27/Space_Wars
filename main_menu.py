# Scripts:
import sys
from sounds import *
from text_creator import *
import level_1
from player import *

# Modules:
import pygame

# Initialize Fonts:
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

        # Movement:
        self.indicator = "main menu"
        self.ref_time = 16
        self.movement_rate = 16
        self.allow_movement_speed = 1

    def update(self) -> None:
        # Render Main Menu Text:
        title_text.update()
        play_text.update()
        options_text.update()
        credits_text.update()
        quit_text.update()

        for text in [play_text, options_text, credits_text, quit_text]:
            text.change_color(self.pos_y)

        # Player Icon Rotation Animation:
        player.rotate(play_text.text_position, self.pos_y)

        '''
        rot_player_img = pygame.transform.rotozoom(self.image, self.angle, 1)
        rot_player_img_rect = rot_player_img.get_rect()
        rot_player_img_position = (
            play_text.text_position[0] - self.rect.x - rot_player_img_rect.width/2,
            play_text.text_position[1] + self.pos_y - rot_player_img_rect.height/2
        )
        SCREEN.blit(rot_player_img, rot_player_img_position)
        self.angle += 2.2
        '''

        # Keyboard Actions:
        key = pygame.key.get_pressed()
        # Main Menu Movement:
        if key[pygame.K_DOWN] and self.movement_rate >= self.ref_time:
            self.pos_y += self.margin
            self.movement_rate = 0
            #channel2.play(sounds['main_menu'][1])
        elif key[pygame.K_UP] and self.movement_rate >= self.ref_time:
            self.pos_y -= self.margin
            self.movement_rate = 0
            #channel2.play(sounds['main_menu'][1])
        # Main Menu Selection:
        elif key[pygame.K_RETURN] and self.movement_rate >= self.ref_time:
            if self.pos_y == self.init_pos_y:  # Position: Play
                self.indicator = "play"
                level_1.run_level_1()
                self.movement_rate = 0
            elif self.pos_y == self.init_pos_y + self.margin:  # Position: Options
                self.indicator = "options"
                self.movement_rate = 0
            elif self.pos_y == self.init_pos_y + 2 * self.margin:  # Position: Credits
                self.indicator = "credits"
                self.movement_rate = 0
            elif self.pos_y == self.init_pos_y + 3 * self.margin:  # Position: Quit
                pygame.quit()
                sys.exit()

        # Reset Variables:
        if self.movement_rate < self.ref_time:
            self.movement_rate += self.allow_movement_speed

        # Player Icon Movement Boundaries:
        if self.pos_y > self.init_pos_y + 3 * self.margin:
            self.pos_y = self.init_pos_y
        if self.pos_y < self.init_pos_y:
            self.pos_y = self.init_pos_y + 3 * self.margin


# Initialize Classes:
main_menu = MainMenu()

# Create Sprites Group:
main_menu_group = pygame.sprite.GroupSingle()

