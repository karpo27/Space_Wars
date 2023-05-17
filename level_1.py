# Scripts:
import constants
from game_effects import *
from base_state import BaseState
from pause import *
from background_creator import *
from player import *
from ui import UI
from enemies import *
from boss import *
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

        # Initialize Classes:
        self.player = Player(*PLAYER_ATTRIBUTES)
        self.ui = UI(self.player)

        # Create Sprites Group:
        self.player_group = pygame.sprite.Group()

        # Add Player Sprites to group:
        self.player_group.add(self.player)

        # Define Number of Enemies to spawn in Level 1:
        self.enemies = [ENEMIES['enemy_f1'], ENEMIES['enemy_c'], ENEMIES['enemy_d'], ENEMIES['enemy_e']]
        #self.enemies = []
        #self.boss = [BOSSES['boss_b']]
        self.boss = []

    def handle_action(self):
        self.next_state = "PAUSE"
        self.screen_done = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        # Press Mouse:
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

        # Spawn Enemies According to Level:
        if len(ENEMIES_GROUP) < len(self.enemies):
            if event.type == Enemy.spawn_enemy:
                k = self.enemies[len(ENEMIES_GROUP)]
                # Generate Enemies
                new_enemy = Enemy(*k)
                ENEMIES_GROUP.add(new_enemy)

        # Spawn Boss According to Level:
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
        # Check Collisions:
        check_collision(PLAYER_BULLETS_GROUP, ENEMIES_GROUP, True, False)  # Player Bullet vs Enemy
        check_collision(PLAYER_BULLETS_GROUP, BOSSES_GROUP, True, False)  # Player Bullet vs Boss
        check_collision(ENEMIES_BULLETS_GROUP, self.player_group, True, False)  # Enemy Bullet vs Player
        check_collision(BOSSES_BULLETS_GROUP, self.player_group, True, False)  # Boss Bullet vs Player
        check_collision(ENEMIES_GROUP, self.player_group, False, False)  # Enemy Body vs Player Body
        check_collision(BOSSES_GROUP, self.player_group, False, False)  # Boss Body vs Player Body

        # Draw Background:
        background_lvl_1.update()

        # Draw UI:
        self.ui.draw(SCREEN)

        # Update Sprites Group:
        self.player_group.update()
        PLAYER_BULLETS_GROUP.update()
        ENEMIES_GROUP.update()
        ENEMIES_BULLETS_GROUP.update()
        BOSSES_GROUP.update()
        BOSSES_BULLETS_GROUP.update()

        # Draw Sprite Groups:
        ENEMIES_BULLETS_GROUP.draw(SCREEN)
        ENEMIES_GROUP.draw(SCREEN)
        BOSSES_BULLETS_GROUP.draw(SCREEN)
        BOSSES_GROUP.draw(SCREEN)

        PLAYER_BULLETS_GROUP.draw(SCREEN)
        self.player_group.draw(SCREEN)

        EXPLOSION_GROUP.draw(SCREEN)
        PARTICLES_GROUP.draw(SCREEN)
        EXPLOSION_GROUP.update()
        PARTICLES_GROUP.update()

        # Extras:
        speakers.action(speakers.x, speakers.y, speakers.state)

