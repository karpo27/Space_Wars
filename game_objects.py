# Scripts
from constants import *
from background import *


# Modules
import pygame
from pygame import mixer
import random


# Initialize Pygame
pygame.init()


class Player:
    y_temp = 19/18 * HEIGHT
    Δd = 0

    def __init__(self):
        self.image = pygame.image.load('Images/Player/player_img.png')
        self.l_image = 64
        self.x = WIDTH/2 - self.l_image/2
        self.y = 5/6 * HEIGHT
        self.Δx = 0
        self.Δy = 0

    def show_image(self, x, y):
        SCREEN.blit(self.image, (x, y))


class PlayerBullet:
    def __init__(self):
        self.image = pygame.image.load('Images/Player/bullets.png')
        self.l_image = 64
        self.x = 0
        self.y = 480
        self.Δx = 0
        self.Δy = 1.2 * dt
        self.state = "ready"  # At this state we can't see bullet on screen
        self.sound = mixer.Sound('Sounds/laser.wav')
        self.col_sound = mixer.Sound('Sounds/explosion.wav')

    def fire_bullet(self, x, y):
        self.state = "fire"
        SCREEN.blit(self.image, (x + 16, y + 10))


class Enemy:
    def __init__(self):
        self.image = pygame.image.load('Images/Enemy/enemy_img.png')
        self.l_image = 64
        self.x = random.randint(0, WIDTH - self.l_image)
        self.y = random.randint(50, HEIGHT/4)
        self.Δx = 0.3 * dt
        self.Δy = 40

    def show_image(self, x, y):
        SCREEN.blit(self.image, (x, y))


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
            p_bullet.sound.set_volume(self.initial_sound)
            p_bullet.col_sound.set_volume(self.initial_sound)
        elif state == "on":
            SCREEN.blit(self.on_image, (x, y))
            mixer.music.set_volume(0.08)
            p_bullet.sound.set_volume(0.08)
            p_bullet.col_sound.set_volume(0.08)


class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.position = self.x, self.y = (10, 10)

    def show(self, x, y):
        score_screen = self.font.render("Score: " + str(self.value), True, (255, 255, 255))
        SCREEN.blit(score_screen, (x, y))


# Initialize Classes:
player = Player()
enemy = Enemy()
p_bullet = PlayerBullet()
speakers = Speakers()
score = Score()
background = Background()




class Game:
    def __init__(self):
        pass

    def process_events(self):
        pass

    def run_logic(self):
        pass

    def display_frame(self):
        pass


def main():
    pass


if __name__ == '__main__':
    pass
