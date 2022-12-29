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

# Player Bullet
bullet_img = pygame.image.load('bullets.png')
l_bullet = 64
bullet_rect = pygame.Surface(l_bullet, l_bullet)
bullet_x = 0
bullet_y = 480
bullet_xΔ = 0
bullet_yΔ = 1.5
bullet_state = "ready"  # At this state we can't see bullet on screen

# Enemy
enemy_img = pygame.image.load('enemy_img.png')
l_enemy = 64
enemy_rect = pygame.Surface(l_enemy, l_enemy)
enemy_x = random.randint(0, width - l_enemy)
enemy_y = random.randint(50, height / 4)
enemy_xΔ = 0.3
enemy_yΔ = 40


def show_player(x, y):
    screen.blit(player_img, (x, y))


def show_enemy(x, y):
    screen.blit(enemy_img, (x, y))


def fire_bullet(x, y):
    global bullet_state
    bullet_state = "fire"
    screen.blit(bullet_img, (x + 16, y + 10))


# Game Loop
running = True
while running:
    # Set background color - RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Press Keyboard
        if event.type == pygame.KEYDOWN:
            # Player Keyboard Movement
            if event.key == pygame.K_LEFT:
                player_xΔ = -0.3
            elif event.key == pygame.K_RIGHT:
                player_xΔ = 0.3
            elif event.key == pygame.K_UP:
                player_yΔ = -0.3
            elif event.key == pygame.K_DOWN:
                player_yΔ = 0.3
            # Player Bullet Keyboard
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    # Get current x coordinate of player
                    bullet_x = player_x
                    bullet_y = player_y
                    fire_bullet(bullet_x, bullet_y)

        # Release Keyboard
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

    # Player Bullet Movement
    if bullet_y <= 0:
        bullet_y = 480
        bullet_state = "ready"
    if bullet_state == "fire":
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bullet_yΔ

    # Collision Detection

    if pygame.Rect.colliderect(bullet_rect.get_rect(), enemy_rect.get_rect()):
        print("collision")

    show_player(player_x, player_y)
    show_enemy(enemy_x, enemy_y)

    # Apply changes
    pygame.display.update()



pygame.quit()

if __name__ == '__main__':
    pass


