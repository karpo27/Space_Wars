# Scripts:
from constants import *

# Modules:
import pygame


class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, img_path, img_qty, scale, animation_delay, movement, vel, angle, bounce, group):
        super().__init__()
        # Image:
        self.sprites = []
        for i in range(1, img_qty + 1):
            images = pygame.image.load(f'{img_path}{i}.png').convert_alpha()
            images = pygame.transform.scale(images, (images.get_width() * scale[0], images.get_height() * scale[1]))
            self.sprites.append(images)

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.image_copy = self.image

        # Animation:
        self.animation_delay = animation_delay
        self.counter = 0

        # Movement:
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.bounce = bounce

        # Rotation:
        self.angle = angle

        # Groups:
        group.add(self)

    def move_x(self):
        self.rect.x += self.vel_x
        if self.bounce:
            if self.rect.left < 0:
                self.vel_x = self.vel_x * -1
            elif self.rect.right > WIDTH:
                self.vel_x = self.vel_x * -1

    def move_y(self):
        self.rect.y += self.vel_y

    def rotate(self):
        rotated_surface = pygame.transform.rotozoom(self.image_copy, self.angle, 1)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center)
        return rotated_surface, rotated_rect

    def handle_movement(self):
        pass

    def animate(self):
        self.counter += 1
        if self.counter >= self.animation_delay and self.index < len(self.sprites) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.sprites[self.index]
            self.image_copy = self.image

    def update(self):
        # Animation:
        self.animate()
        # Movement:
        self.handle_movement()
