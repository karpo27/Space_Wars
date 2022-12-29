# Scripts


# Modules
import pygame
import random

# Initialize Pygame
pygame.init()

# Create the screen
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Game_Project")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('player_img.png')
l_player = 64
player_x = 370
player_y = 480
player_xΔ = 0
player_yΔ = 0

# Enemy
enemy_img = pygame.image.load('enemy_img.png')
l_enemy = 64
enemy_x = random.randint(0, width - l_enemy)
enemy_y = random.randint(50, height / 4)
enemy_xΔ = 0.3
enemy_yΔ = 40


def show_player(x, y):
    screen.blit(player_img, (x, y))


def show_enemy(x, y):
    screen.blit(enemy_img, (x, y))

# Game Loop
running = True
while running:
    # Set background color - RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Player Keyboard Movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_xΔ = -0.3
            elif event.key == pygame.K_RIGHT:
                player_xΔ = 0.3
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                player_yΔ = -0.3
            elif event.key == pygame.K_DOWN:
                player_yΔ = 0.3
        if event.type == pygame.KEYUP:
            if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                player_xΔ = 0
            elif event.key in (pygame.K_UP, pygame.K_DOWN):
                player_yΔ = 0

    # Movement Boundaries
    player_x += player_xΔ
    player_y += player_yΔ

    if player_x <= 0:
        player_x = 0
    elif player_x >= width - l_player:
        player_x = width - l_player

    enemy_x += enemy_xΔ

    if enemy_x <= 0:
        enemy_xΔ = 0.3
        enemy_y += enemy_yΔ
    elif enemy_x >= width - l_enemy:
        enemy_xΔ = -0.3
        enemy_y += enemy_yΔ

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)

    # Apply changes
    pygame.display.update()



pygame.quit()

if __name__ == '__main__':
    pass


