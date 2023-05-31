# Scripts:
from constants import *

# Modules:
import pygame


class Character(pygame.sprite.Sprite):

    def __init__(self, category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group):
        super().__init__()
        # Image:
        self.category = category
        self.img_path = img_path
        self.image = pygame.image.load(f'{self.img_path}{self.category}.png').convert_alpha()
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.image_copy = self.image
        self.rect = self.image.get_rect()

        # Initial Movement Animation:
        self.start_animation = None
        # Final Movement Animation:
        self.end_animation = False

        # Movement:
        self.vel = self.vel_x, self.vel_y = vel
        self.counter = 0

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
        self.blinks = False
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

    def restrict_x(self, left_limit, right_limit):
        if self.rect.left <= left_limit:
            self.vel_x = self.vel_x * -1
        elif self.rect.right >= right_limit:
            self.vel_x = self.vel_x * -1

    def restrict_x_counter(self, limit):
        self.move_x()
        self.counter += 1
        if self.counter == limit:
            self.vel_x = self.vel_x * -1
            self.counter = 0

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

    def animate_start(self):
        pass

    def animate_end(self):
        pass

    def handle_action(self):
        pass

    def make_invulnerable(self):
        if self.invulnerable:
            if self.invulnerable_rate >= self.invulnerable_ref_time:
                self.invulnerable = False
                self.image = pygame.image.load(f'{self.img_path}{self.category}.png').convert_alpha()
            else:
                self.invulnerable_rate += 1
                if self.blinks:
                    self.blink_rate += 1
                    self.blink_image()

    def reset_variables(self):
        pass

    def update(self):
        if self.start_animation:
            self.animate_start()
        elif self.end_animation:
            self.animate_end()
        else:
            self.handle_action()
        self.make_invulnerable()
        self.reset_variables()
