# Scripts
from constants import *
from bg_creator import *

# Modules
import pygame
import random

# Initialize Pygame
pygame.init()

class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.sprites = []
        for i in range(1, 6):
            images = pygame.image.load(f'Images/Explosion/explosion_{i}.png').convert_alpha()
            images = pygame.transform.scale(images, (images.get_width() * scale, images.get_height() * scale))
            self.sprites.append(images)

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect(x=x, y=y)
        self.counter = 0

    def update(self):
        explosion_delay = 8
        # Update Explosion Animation
        self.counter += 1

        if self.counter >= explosion_delay and self.index < len(self.sprites) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.sprites[self.index]

        # If the Animation is Complete, Reset the Index
        if self.index >= len(self.sprites) - 1 and self.counter >= explosion_delay:
            self.kill()


class Particle(pygame.sprite.Sprite):
    def __init__(self, pos, group):
        super().__init__()
        # Size, Color, Speed, Timer:
        self.width = random.randrange(1, 6)
        self.height = self.width
        self.size = self.width, self.height
        self.image = pygame.Surface(self.size)
        self.color = (random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel_x = random.randrange(-12, 12)
        self.vel_y = random.randrange(-12, 12)
        self.kill_timer = 55

        # Groups:
        group.add(self)

    def update(self):
        # Movement:
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Timer
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1


class HitParticle(pygame.sprite.Sprite):
    def __init__(self, pos, color_1, color_2, factor, group):
        super().__init__()
        # Size, Color, Speed, Timer:
        self.width = random.randrange(1, 5)
        self.height = self.width
        self.size = self.width, self.height
        self.image = pygame.Surface(self.size)
        self.color = random.choices([color_1, color_2])[0]
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel_x = random.randrange(-4, 4)
        self.vel_y = random.randrange(1, 4) * factor
        self.kill_timer = 18

        # Groups:
        group.add(self)

    def update(self):
        # Movement:
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        # Timer
        if self.kill_timer == 0:
            self.kill()
        else:
            self.kill_timer -= 1
