# Scripts:
import constants
from game_objects import *
from base_state import BaseState
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


class Level1(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "GAME_OVER"

        # Screen and Options:
        self.options_qty = 3
        self.index = 0
        self.screen = "LEVEL"

        # Define Number of Enemies to spawn in Level 1:
        self.enemies_lvl_1 = []
        self.bosses_lvl_1 = [bosses['boss_b']]

    def handle_action(self):
        if self.screen == "LEVEL":
            self.screen = "PAUSE"
        elif self.screen == "PAUSE":
            self.screen = "LEVEL"

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        # Press Mouse
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
            mouse_pos = pygame.mouse.get_pos()
            if speakers.off_rect.collidepoint(mouse_pos):
                if speakers.state == "off":
                    speakers.state = "on"
                else:
                    speakers.state = "off"
        elif event.type == pygame.KEYDOWN:
            # Pause Menu Selection:
            if event.key == pygame.K_ESCAPE:
                self.handle_action()
            if event.key == pygame.K_DOWN and self.screen == "PAUSE":
                pass

        # Spawn Enemies According to Level
        if len(enemies_group) < len(self.enemies_lvl_1):
            if event.type == Enemy.spawn_enemy:
                k = self.enemies_lvl_1[len(enemies_group)]
                # Generate Enemies
                new_enemy = Enemy(*k)
                enemies_group.add(new_enemy)

        # Spawn Boss According to Level
        if len(bosses_group) < len(self.bosses_lvl_1):
            if event.type == Enemy.spawn_enemy:
                k = self.bosses_lvl_1[len(bosses_group)]
                # Generate Boss
                new_boss = Boss(*k)
                bosses_group.add(new_boss)

        # Check Collisions
        check_collision(player_bullet_group, enemies_group, True, False)  # Check Collisions Player Bullets vs Enemies
        check_collision(player_bullet_group, bosses_group, True, False)  # Check Collisions Player Bullet vs Bosses
        check_collision(player_group, enemies_group, False, False)  # Check Collisions Player Body vs Enemy Body
        check_collision(player_group, bosses_group, False, False)  # Check Collisions Player Body vs Boss Body
        check_collision(enemies_bullet_group, player_group, True, False)  # Check Collisions Enemy Bullet vs Player
        check_collision(bosses_bullet_group, player_group, True, False)  # Check Collisions Boss Bullet vs Player
        check_collision(enemies_group, player_group, False, False)  # Check Collisions Enemy Body vs Player Body
        check_collision(bosses_group, player_group, False, False)  # Check Collisions Boss Body vs Player Body

        # Go to Game Over / Continue Screen
        if player.lives < 1:
            pass

        # Consume Life to Keep Playing
        if player.hp == 0:
            player.lives -= 1
            # player.hp = 3

    def draw(self, surface):
        if self.screen == "LEVEL":
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
        elif self.screen == "PAUSE":
            pause_menu.draw()

        # Extras
        speakers.action(speakers.x, speakers.y, speakers.state)

    '''
    def run_level_1(self):
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
                if pygame.display.get_surface() == SCREEN:
                    pygame.display.quit()
                    #pygame.quit()
                    #sys.exit()

            # Extras
            speakers.action(speakers.x, speakers.y, speakers.state)

            # Apply changes
            pygame.display.update()
            '''

