# Scripts
from constants import *
from background import *
from game_objects import *


# Modules
import pygame
from pygame import mixer
import random

# Initialize Pygame
pygame.init()

# Game Loop
def run_level_1():
    running = True
    while running:
        # Set screen FPS
        clock.tick(FPS)

        # Draw Scrolling Background
        background.show()

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

run_level_1()