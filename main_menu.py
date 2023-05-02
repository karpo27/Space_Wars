# Scripts:
import sys
from text_creator import *
import level_1

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
        self.font_size = 48
        self.color = (193, 225, 193)  # Pastel Green

        self.hover_font_size = 52
        self.hover_color = (255, 255, 255)  # White

        self.margin = 70

        # Movement:
        self.indicator = "main menu"
        self.ref_time = 16
        self.movement_rate = 16
        self.allow_movement_speed = 1

    def change_hover_text(self, text_list, state_list):
        for text, state in zip(text_list, state_list):
            if state == "hover":
                text.font_size = self.hover_font_size
                text.color = self.hover_color
            else:
                text.font_size = self.font_size
                text.color = self.color

    def update(self) -> None:
        # Render Main Menu Text:
        title_text.show()
        play_text.show()
        options_text.show()
        credits_text.show()
        quit_text.show()

        # Player Icon Rotation Animation:
        rot_player_img = pygame.transform.rotozoom(self.image, self.angle, 1)
        rot_player_img_rect = rot_player_img.get_rect()
        rot_player_img_position = (
            play_text.text_position[0] - self.rect.x - rot_player_img_rect.width/2,
            play_text.text_position[1] + self.pos_y - rot_player_img_rect.height/2
        )
        SCREEN.blit(rot_player_img, rot_player_img_position)
        self.angle += 2.2

        # Keyboard Actions:
        key = pygame.key.get_pressed()
        # Main Menu Movement:
        if key[pygame.K_DOWN] and self.movement_rate >= self.ref_time:
            self.pos_y += self.margin
            self.movement_rate = 0
        elif key[pygame.K_UP] and self.movement_rate >= self.ref_time:
            self.pos_y -= self.margin
            self.movement_rate = 0
        # Main Menu Selection:
        elif key[pygame.K_RETURN] and self.movement_rate >= self.ref_time:
            if self.pos_y == self.init_pos_y:  # Position: Play
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

        # Change Text Color when Hover:
        if self.pos_y == self.init_pos_y:
            self.change_hover_text(main_menu_list, ["hover", "", "", ""])
        if self.pos_y == self.init_pos_y + self.margin:
            self.change_hover_text(main_menu_list, ["", "hover", "", ""])
        if self.pos_y == self.init_pos_y + 2 * self.margin:
            self.change_hover_text(main_menu_list, ["", "", "hover", ""])
        if self.pos_y == self.init_pos_y + 3 * self.margin:
            self.change_hover_text(main_menu_list, ["", "", "", "hover"])


# Initialize Classes:
main_menu = MainMenu()

# Create Sprites Group:
main_menu_group = pygame.sprite.GroupSingle()

