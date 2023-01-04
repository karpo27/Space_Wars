# Scripts
from constants import *
from background import *
from main_menu import *

# Modules
import pygame
from pygame import mixer
import random


# Initialize Pygame
pygame.init()

# Define Clock for Screen FPS
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)

# Title and Icon
pygame.display.set_caption("Game_Project")
icon = pygame.image.load('Images/Screen/icon.png')
pygame.display.set_icon(icon)


class Player:
    def __init__(self):
        self.image = pygame.image.load('Images/Player/player_img.png')
        self.l_image = 64
        self.x = WIDTH/2 - self.l_image/2
        self.y = 8/9 * HEIGHT
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
main_menu = MainMenu()



# Game Loop
running = True
while running:
    # Set screen FPS
    clock.tick(FPS)

    # Draw Scrolling Background
    main_menu.show()
    #background.show()


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press Keyboard
        if event.type == pygame.KEYDOWN:
            # Player Keyboard Movement
            if event.key == pygame.K_LEFT:
                player.Δx = -0.3 * dt
            elif event.key == pygame.K_RIGHT:
                player.Δx = 0.3 * dt
            elif event.key == pygame.K_UP:
                player.Δy = -0.3 * dt
            elif event.key == pygame.K_DOWN:
                player.Δy = 0.3 * dt
            # Player Bullet Keyboard
            elif event.key == pygame.K_SPACE:
                if p_bullet.state == "ready":
                    p_bullet.sound.play()
                    p_bullet.sound.set_volume(speakers.initial_sound)
                    # Get current (x, y) coordinate of player
                    p_bullet.x = player.x
                    p_bullet.y = player.y
                    p_bullet.fire_bullet(p_bullet.x, p_bullet.y)

        # Release Keyboard
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player.Δx = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                player.Δy = 0

        # Press Mouse
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_pos = pygame.mouse.get_pos()
            if speakers.off_rect.collidepoint(mouse_pos):
                if speakers.state == "off":
                    speakers.state = "on"
                else:
                    speakers.state = "off"

    # Player Movement Boundaries
    player.x += player.Δx
    player.y += player.Δy

    if player.x <= 0:
        player.x = 0
    if player.y <= 0:
        player.y = 0
    if player.x >= WIDTH - player.l_image:
        player.x = WIDTH - player.l_image
    if player.y >= HEIGHT - player.l_image:
        player.y = HEIGHT - player.l_image

    # Enemy Movement
    enemy.x += enemy.Δx

    if enemy.x <= 0:
        enemy.Δx = 0.3 * dt
        enemy.y += enemy.Δy
    if enemy.x >= WIDTH - enemy.l_image:
        enemy.Δx = -0.3 * dt
        enemy.y += enemy.Δy

    # Player Bullet Movement
    if p_bullet.y <= 0:
        p_bullet.y = 480
        p_bullet.state = "ready"
    if p_bullet.state == "fire":
        p_bullet.fire_bullet(p_bullet.x, p_bullet.y)
        p_bullet.y -= p_bullet.Δy

    # Collision Detection (fix problem at intersection of objects when pressing "spacebar")
    collision = pygame.Rect.colliderect(
        p_bullet.image.get_rect(x=p_bullet.x, y=p_bullet.y),
        enemy.image.get_rect(x=enemy.x, y=enemy.y)
    )
    if collision:
        p_bullet.y = player.y
        p_bullet.state = "ready"
        score.value += 1
        p_bullet.col_sound.play()

    player.show_image(player.x, player.y)
    enemy.show_image(enemy.x, enemy.y)
    score.show(score.x, score.y)
    speakers.action(speakers.x, speakers.y, speakers.state)

    # Apply changes
    pygame.display.update()


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
