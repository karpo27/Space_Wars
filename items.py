# Scripts:
from constants import *

# Modules:
import pygame
import random
import secrets


class Item(pygame.sprite.Sprite):
    def __init__(self, img_path, scale, vel, bounce):
        super().__init__()
        # Image:
        self.img_path = img_path
        self.image = pygame.image.load(f'{self.img_path}.png').convert_alpha()
        self.scale = scale
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(int(0 + self.rect.width/2), int(WIDTH - self.rect.width/2)), -40]

        # Movement:
        self.vel = self.vel_x, self.vel_y = vel
        self.vel_x = self.vel_x * secrets.choice([-1, 1])
        self.bounce = bounce

    def move_x(self):
        self.rect.x += self.vel_x
        if self.bounce:
            if self.rect.left <= 0:
                self.vel_x = self.vel_x * -1
            elif self.rect.right >= WIDTH:
                self.vel_x = self.vel_x * -1

    def move_y(self):
        self.rect.y += self.vel_y

    def handle_movement(self):
        if self.rect.top > HEIGHT:
            self.kill()
        else:
            self.move_x()
            self.move_y()

    def update(self):
        # Movement:
        self.handle_movement()


class HP(Item):
    def __init__(self, img_path, scale, vel, bounce):
        super().__init__(img_path, scale, vel, bounce)


class Life(Item):
    def __init__(self, img_path, scale, vel, bounce):
        super().__init__(img_path, scale, vel, bounce)
