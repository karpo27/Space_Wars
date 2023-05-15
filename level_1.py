# Scripts:
import constants
from game_effects import *
from base_state import BaseState
from pause import *
from background_creator import *
from player import *
from enemies import *
from boss import *

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

        # Initialize Classes:
        self.player = Player(*PLAYER_ATTRIBUTES)

        # Create Sprites Group:
        self.player_group = pygame.sprite.Group()

        # Add Player Sprites to group
        self.player_group.add(self.player)

        # Define Number of Enemies to spawn in Level 1:
        self.enemies = []
        self.boss = [BOSSES['boss_b']]


    def check_collision(self, group_1, group_2, do_kill_1, do_kill_2):
        collision = pygame.sprite.groupcollide(group_1, group_2, do_kill_1, do_kill_2)
        for group1, group2 in collision.items():
            group2[0].get_hit()

    def handle_action(self):
        self.next_state = "PAUSE"
        self.screen_done = True

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

        # Spawn Enemies According to Level
        if len(ENEMIES_GROUP) < len(self.enemies):
            if event.type == Enemy.spawn_enemy:
                k = self.enemies[len(ENEMIES_GROUP)]
                # Generate Enemies
                new_enemy = Enemy(*k)
                ENEMIES_GROUP.add(new_enemy)

        # Spawn Boss According to Level
        if len(BOSSES_GROUP) < len(self.boss):
            if event.type == Enemy.spawn_enemy:
                k = self.boss[len(BOSSES_GROUP)]
                # Generate Boss
                new_boss = Boss(*k)
                BOSSES_GROUP.add(new_boss)

        # Go to Game Over Screen:
        if self.player.state == "dead":
            self.screen_done = True

    def draw(self, surface):
        # Check Collisions
        self.check_collision(PLAYER_BULLETS_GROUP, ENEMIES_GROUP, True, False)  # Player Bullet vs Enemy
        self.check_collision(PLAYER_BULLETS_GROUP, BOSSES_GROUP, True, False)  # Player Bullet vs Boss
        self.check_collision(self.player_group, ENEMIES_GROUP, False, False)  # Player Body vs Enemy Body
        self.check_collision(self.player_group, BOSSES_GROUP, False, False)  # Player Body vs Boss Body
        self.check_collision(ENEMIES_BULLETS_GROUP, self.player_group, True, False)  # Enemy Bullet vs Player
        self.check_collision(BOSSES_BULLETS_GROUP, self.player_group, True, False)  # Boss Bullet vs Player
        self.check_collision(ENEMIES_GROUP, self.player_group, False, False)  # Enemy Body vs Player Body
        self.check_collision(BOSSES_GROUP, self.player_group, False, False)  # Boss Body vs Player Body

        # Draw Background
        background_lvl_1.update()
        # Update Sprites Group
        self.player_group.update()
        PLAYER_BULLETS_GROUP.update()
        ENEMIES_GROUP.update()
        ENEMIES_BULLETS_GROUP.update()
        BOSSES_GROUP.update()
        BOSSES_BULLETS_GROUP.update()

        # Draw Sprite Groups
        ENEMIES_BULLETS_GROUP.draw(SCREEN)
        ENEMIES_GROUP.draw(SCREEN)
        BOSSES_BULLETS_GROUP.draw(SCREEN)
        BOSSES_GROUP.draw(SCREEN)

        PLAYER_BULLETS_GROUP.draw(SCREEN)
        self.player_group.draw(SCREEN)

        explosion_group.draw(SCREEN)

        explosion_group.update()

        # Extras
        speakers.action(speakers.x, speakers.y, speakers.state)

