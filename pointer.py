# Scripts:
from constants import *

# Modules:
import pygame


class Pointer:
    def __init__(self):
        # Player Icon:
        self.image = pygame.image.load('Images/Player/player_img.png').convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.pos_x, self.pos_y = 70, 30
        self.angle = 0

    def draw_rotated(self, position, menu):
        # Render Player Icon Rotation:
        if menu in ["MENU", "CREDITS"]:
            self.pos_x = 70
        else:
            self.pos_x = 80

        rotated_surface = pygame.transform.rotozoom(self.image, self.angle, 1)
        rotated_rect = rotated_surface.get_rect()
        rotated_surface_position = (
            position[0] - self.rect.x - rotated_rect.width/2,
            position[1] + self.pos_y - rotated_rect.height/2
        )
        SCREEN.blit(rotated_surface, rotated_surface_position)
        self.angle += 2.2
