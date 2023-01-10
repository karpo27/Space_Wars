# Scripts
from game_objects import *

# Modules
import pygame
from pygame import mixer
import random

# Initialize Pygame
pygame.init()


def run_level_1():
    # Game Loop
    run = True
    while run:
        # Set screen FPS
        clock.tick(FPS)

        # Draw Scrolling Background
        background.show()

        # Enter Level Animation
        if player.y < Player.y_enter - Player.Δd:
            pygame.event.set_blocked([pygame.KEYDOWN, pygame.KEYUP])
            player.show_image(player.x, Player.y_enter - Player.Δd)
            Player.Δd += 1.9
        else:
            Player.y_enter = 0
            Player.Δd = 0
            pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])
            player.show_image(player.x, player.y)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

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
                        # Get current (x, y) coordinate of Player
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

            # Define Number of Enemies to spawn in Level 1: 10
            enemies_lvl_1 = ['common', 'common']
            n_enemies = len(enemies_lvl_1)
            if len(Enemy.enemy_list) < n_enemies:
                #for i in range(len(enemies_lvl_1)):
                if event.type == Enemy.spawn_enemy:
                    enemy.generate_enemies(1)

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

        # Enemies Movement
        for i in range(len(Enemy.enemy_list)):
            enemy.x[i] += enemy.Δx[i]

            if enemy.x[i] <= 0:
                enemy.Δx[i] = 0.3 * dt
                enemy.y[i] += enemy.Δy[i]
            elif enemy.x[i] >= WIDTH - enemy.l_image:
                enemy.Δx[i] = -0.3 * dt
                enemy.y[i] += enemy.Δy[i]

            # Collision Detection (fix problem at intersection of objects when pressing "spacebar")
            collision = pygame.Rect.colliderect(
                p_bullet.image.get_rect(x=p_bullet.x, y=p_bullet.y),
                enemy.image.get_rect(x=enemy.x[i], y=enemy.y[i])
            )
            if collision:
                # The collision will affect only if this:
                if enemy.y[i] + enemy.l_image >= 0:
                    p_bullet.y = player.y
                    p_bullet.state = "ready"
                    score.value += 1
                    p_bullet.col_sound.play()

            # Show Enemies Images
            enemy.show_image(enemy.x[i], enemy.y[i], i)

        # Player Bullet Movement
        if p_bullet.state == "fire":
            p_bullet.fire_bullet(p_bullet.x, p_bullet.y)
            p_bullet.y -= p_bullet.Δy
        if p_bullet.y <= 0 - p_bullet.l_image:
            p_bullet.state = "ready"

        player.draw_hp_bar(Player.hp)
        score.show(score.x, score.y)
        speakers.action(speakers.x, speakers.y, speakers.state)

        # Apply changes
        pygame.display.update()


run_level_1()