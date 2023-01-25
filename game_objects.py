# Scripts
from constants import *
from background import *

# Modules
import pygame
from pygame import mixer
import math

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
            mixer.music.set_volume(0.0)
            #player_bullet.sound.set_volume(self.initial_sound)
            #player_bullet.col_sound.set_volume(self.initial_sound)
            #e_bullet_F.col_sound.set_volume(self.initial_sound)
        elif state == "on":
            SCREEN.blit(self.on_image, (x, y))
            mixer.music.set_volume(0.08)
            #player_bullet.sound.set_volume(0.08)
            #player_bullet.col_sound.set_volume(0.08)
            #e_bullet_F.col_sound.set_volume(0.08)


class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.position = self.x, self.y = (10, 10)

    def show(self, x, y):
        score_screen = self.font.render("Score: " + str(self.value), True, (255, 255, 255))
        SCREEN.blit(score_screen, (x, y))


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


# Initialize Classes:
speakers = Speakers()
score = Score()
explosion_group = pygame.sprite.Group()
background = Background()

# Create Sprites Group:


# Add Some Sprites to group



if __name__ == '__main__':
    pass
