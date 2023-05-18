# Scripts
from constants import *
from background_creator import *

# Modules
import pygame
import random

# Initialize Pygame
pygame.init()


class Speakers:
    def __init__(self):
        self.on_image = pygame.image.load('Images/Speakers/speakers_on_img.png')
        self.off_image = pygame.image.load('Images/Speakers/speakers_off_img.png')
        self.position = self.x, self.y = (13/14 * WIDTH, 1/75 * HEIGHT)
        self.on_rect = self.on_image.get_rect(x=self.x, y=self.y)
        self.off_rect = self.off_image.get_rect(x=self.x, y=self.y)
        self.state = "off"      # This means game will begin with Speakers-Off as default
        self.initial_sound = 0.0

    def action(self, x, y, state):
        if state == "off":
            SCREEN.blit(self.off_image, (x, y))
            #mixer.music.set_volume(0.0)
        elif state == "on":
            SCREEN.blit(self.on_image, (x, y))
            #mixer.music.set_volume(0.06)


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y, scale):
        super().__init__()
        self.sprites = []
        for i in range(1, 6):
            images = pygame.image.load(f'Images/Explosion/explosion_{i}.png').convert_alpha()
            images = pygame.transform.scale(images, (images.get_width() * scale[0], images.get_height() * scale[1]))
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
        self.vel_x = random.randrange(-16, 16)
        self.vel_y = random.randrange(-16, 16)
        self.kill_timer = 60

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


# Initialize Classes:
speakers = Speakers()

if __name__ == '__main__':
    pass
