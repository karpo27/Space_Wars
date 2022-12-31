# Scripts


# Modules
import pygame
from pygame import mixer
import random
import math

# Initialize Pygame
pygame.init()

# Define Clock for Screen FPS
clock = pygame.time.Clock()
FPS = 60
dt = clock.tick(FPS)

# Create the screen
size = width, height = (1000, 800)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Game_Project")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('player_img.png')
l_player = 64
player_x = width / 2 - l_player / 2
player_y = 8 / 9 * height
player_Δx = 0
player_Δy = 0

# Player Bullet
bullet_img = pygame.image.load('bullets.png')
l_bullet = 64
bullet_x = 0
bullet_y = 480
bullet_Δx = 0
bullet_Δy = 1.2 * dt
bullet_state = "ready"  # At this state we can't see bullet on screen

# Enemy
enemy_img = pygame.image.load('enemy_img.png')
l_enemy = 64
enemy_x = random.randint(0, width - l_enemy)
enemy_y = random.randint(50, height / 4)
enemy_Δx = 0.3 * dt
enemy_Δy = 40

# Space Background
space_bg = pygame.image.load('space_bg.jpg')
bg_height = space_bg.get_height()
mixer.music.load('Sounds/background.wav')
mixer.music.play(-1)    # (-1) for playing on loop

# Define Scrolling
scroll = 0
tiles = math.ceil(height / bg_height)

# Score
score_value = 0
font = pygame.font.Font('freesansbold.ttf', 32)
score_pos = text_x, text_y = (10, 10)


def show_player(x, y):
    screen.blit(player_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


def show_enemy(x, y):
    screen.blit(enemy_img, (x, y))


def show_score(x, y):
    score = font.render("Score: " + str(score_value), True, (255, 255, 255))
    screen.blit(score, (x, y))


# Game Loop
running = True
while running:
    # Set screen FPS
    clock.tick(FPS)

    # Draw Scrolling Background
    screen.blit(space_bg, (0, -height + scroll))  # Position 2
    screen.blit(space_bg, (0, scroll))  # Position 1

    # Scroll Movement Speed
    scroll += 0.8

    # Reset Scroll
    if scroll >= bg_height:
        scroll = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press Keyboard
        if event.type == pygame.KEYDOWN:
            # Player Keyboard Movement
            if event.key == pygame.K_LEFT:
                player_Δx = -0.3 * dt
            elif event.key == pygame.K_RIGHT:
                player_Δx = 0.3 * dt
            elif event.key == pygame.K_UP:
                player_Δy = -0.3 * dt
            elif event.key == pygame.K_DOWN:
                player_Δy = 0.3 * dt
            # Player Bullet Keyboard
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_sound = mixer.Sound('Sounds/laser.wav')
                    bullet_sound.play()
                    # Get current (x, y) coordinate of player
                    bullet_x = player_x
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)

        # Release Keyboard
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_Δx = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                player_Δy = 0

    # Player Movement Boundaries
    player_x += player_Δx
    player_y += player_Δy

    if player_x <= 0:
        player_x = 0
    if player_y <= 0:
        player_y = 0
    if player_x >= width - l_player:
        player_x = width - l_player
    if player_y >= height - l_player:
        player_y = height - l_player

    # Enemy Movement
    enemy_x += enemy_Δx

    if enemy_x <= 0:
        enemy_Δx = 0.3 * dt
        enemy_y += enemy_Δy
    if enemy_x >= width - l_enemy:
        enemy_Δx = -0.3 * dt
        enemy_y += enemy_Δy

    # Player Bullet Movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_Δy

    # Collision Detection (fix problem at intersection of objects when pressing "spacebar")
    collision = pygame.Rect.colliderect(
        bullet_img.get_rect(x=bullet_x, y=bullet_y),
        enemy_img.get_rect(x=enemy_x, y=enemy_y)
    )
    if collision:
        bullet_y = player_y
        bullet_state = "ready"
        score_value += 1
        bullet_col_sound = mixer.Sound('Sounds/explosion.wav')
        bullet_col_sound.play()

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)
    show_score(text_x, text_y)

    # Apply changes
    pygame.display.update()

if __name__ == '__main__':
    pass
