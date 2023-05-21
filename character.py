# Scripts
from constants import *

# Modules
import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group):
        super().__init__()
        # Image:
        self.category = category
        self.img_path = img_path
        self.image = pygame.image.load(f'{self.img_path}{self.category}.png').convert_alpha()
        self.scale_x, self.scale_y = scale[0], scale[1]
        self.image = pygame.transform.scale(self.image,
                                            (self.image.get_width() * self.scale_x, self.image.get_height() * self.scale_y))
        self.image_copy = self.image
        self.rect = self.image.get_rect()

        # Movement:
        self.vel = self.vel_x, self.vel_y = vel

        # Rotation:
        self.angle = 0

        # HP:
        self.hp = hp

        # State:
        self.invulnerable = False
        self.invulnerable_ref_time = 120
        self.invulnerable_rate = 120

        # Blink:
        self.empty_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        self.blink_ref_time = self.invulnerable_ref_time / 20
        self.blink_rate = 0

        # Bullet:
        self.bullet_group = bullet_group
        self.ref_time = fire_rate
        self.fire_rate = fire_rate

        # Explosion:
        self.effects_group = effects_group
        self.explosion_scale = explo_scale
        self.part_min, self.part_max = part_range

    def move_x(self):
        self.rect.x += self.vel_x

    def move_y(self):
        self.rect.y += self.vel_y

    def move_y_angle(self):
        pass

    def move_x_beam(self):
        pass

    def rotate(self):
        rotated_surface = pygame.transform.rotozoom(self.image_copy, self.angle, 1)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center)
        return rotated_surface, rotated_rect

    def spawn_bullet(self):
        pass

    def get_hit(self, pos, col_type):
        pass

    def destroy(self):
        pass

    def blink_image(self):
        if self.blink_rate < self.blink_ref_time:
            self.image = self.empty_surface
        elif self.blink_ref_time <= self.blink_rate < 2 * self.blink_ref_time:
            self.image = pygame.image.load(f'{self.img_path}{self.category}.png').convert_alpha()
        else:
            self.blink_rate = 0

    def update(self):
        pass
