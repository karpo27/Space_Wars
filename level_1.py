# Scripts:
import constants
from game_objects import *
from pause_menu import *
from background_creator import *
from player import *
from enemies import *
from bosses import *
from collisions import *

# Modules:
import pygame
from pygame import mixer

# Initialize Pygame:
pygame.init()


def run_level_1():
    # Game Loop
    run = True
    while run:
        # Set screen FPS
        clock.tick(FPS)

        # Define Number of Enemies to spawn in Level 1: 10
        enemies_lvl_1 = []
        bosses_lvl_1 = [bosses['boss_b']]

        # Go to Game Over / Continue Screen
        if player.lives < 1:
            pass

        # Consume Life to Keep Playing
        if player.hp == 0:
            player.lives -= 1
            #player.hp = 3

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Press Mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse_pos = pygame.mouse.get_pos()
                if speakers.off_rect.collidepoint(mouse_pos):
                    if speakers.state == "off":
                        speakers.state = "on"
                    else:
                        speakers.state = "off"

            if event.type == pygame.KEYDOWN:
                # Pause Menu Selection:
                if event.key == pygame.K_ESCAPE:
                    if constants.game_screen == "play":
                        constants.game_screen = "pause menu"
                    elif constants.game_screen == "pause menu":
                        constants.game_screen = "play"

                if event.key == pygame.K_DOWN and constants.game_screen == "pause menu":
                    pass


            # Spawn Enemies According to Level
            if len(enemies_group) < len(enemies_lvl_1):
                if event.type == Enemy.spawn_enemy:
                    k = enemies_lvl_1[len(enemies_group)]
                    # Generate Enemies
                    new_enemy = Enemy(*k)
                    enemies_group.add(new_enemy)

            # Spawn Boss According to Level
            if len(bosses_group) < len(bosses_lvl_1):
                if event.type == Enemy.spawn_enemy:
                    k = bosses_lvl_1[len(bosses_group)]
                    # Generate Boss
                    new_boss = Boss(*k)
                    bosses_group.add(new_boss)

        # Check Collisions
        check_collision(player_bullet_group, enemies_group, True, False)    # Check Collisions Player Bullets vs Enemies
        check_collision(player_bullet_group, bosses_group, True, False)     # Check Collisions Player Bullet vs Bosses
        check_collision(player_group, enemies_group, False, False)          # Check Collisions Player Body vs Enemy Body
        check_collision(player_group, bosses_group, False, False)           # Check Collisions Player Body vs Boss Body

        check_collision(enemies_bullet_group, player_group, True, False)    # Check Collisions Enemy Bullet vs Player
        check_collision(bosses_bullet_group, player_group, True, False)     # Check Collisions Boss Bullet vs Player
        check_collision(enemies_group, player_group, False, False)          # Check Collisions Enemy Body vs Player Body
        check_collision(bosses_group, player_group, False, False)           # Check Collisions Boss Body vs Player Body

        if constants.game_screen == "play":
            # Draw Scrolling Background
            background_lvl_1.update()
            # Update Sprites Group
            player_group.update()
            player_bullet_group.update()
            enemies_group.update()
            enemies_bullet_group.update()
            bosses_group.update()
            bosses_bullet_group.update()

            # Draw Sprite Groups
            enemies_bullet_group.draw(SCREEN)
            enemies_group.draw(SCREEN)
            bosses_bullet_group.draw(SCREEN)
            bosses_group.draw(SCREEN)

            player_bullet_group.draw(SCREEN)
            player_group.draw(SCREEN)

            explosion_group.draw(SCREEN)

            explosion_group.update()
        elif constants.game_screen == "pause menu":
            pause_menu.update()
        elif constants.game_screen == "main menu":
            pygame.quit()
            #sys.exit()

        # Extras
        speakers.action(speakers.x, speakers.y, speakers.state)

        # Apply changes
        pygame.display.update()


#run_level_1()
