# Scripts:
from game_effects import Explosion, Particle, Speakers
from base_state import BaseState
from pause import *
from background_creator import BackgroundCreator
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

        # Create Sprites Group:
        self.player_group = pygame.sprite.Group()
        self.player_bullets_group = pygame.sprite.Group()
        self.enemies_group = pygame.sprite.Group()
        self.bosses_group = pygame.sprite.Group()
        self.enemies_bullets_group = pygame.sprite.Group()
        self.effects_group = pygame.sprite.Group()

        # Initialize Classes:
        self.background = BackgroundCreator(*BACKGROUNDS['level_1'])
        self.player = Player(*PLAYER_ATTRIBUTES, self.player_bullets_group, self.effects_group)
        self.ui = UI(self.player)

        # Add Player Sprites to group:
        self.player_group.add(self.player)

        # Define Number of Enemies to spawn in Level 1:
        self.enemies = []
        self.enemy_index = 0
        for enemy_type in ENEMIES_LVL1:
            self.enemies.append(ENEMIES[f'enemy_{enemy_type}'])
        self.boss = [BOSSES['boss_b']]
        self.boss_to_spawn = True
        #self.boss = []

    def handle_pause(self):
        self.next_state = "PAUSE"
        self.screen_done = True

    def spawn_enemy(self):
        k = self.enemies[self.enemy_index]
        self.enemies_group.add(Enemy(*k, self.enemies_bullets_group, self.effects_group))
        self.enemy_index += 1

    def spawn_boss(self):
        k = self.boss[0]
        self.enemies_group.add(Boss(*k, self.enemies_bullets_group, self.effects_group))
        self.boss_to_spawn = False

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
                self.handle_pause()

        # Spawn Enemies According to Level:
        if self.enemy_index <= len(self.enemies) - 1:
            if event.type == Enemy.spawn_enemy:
                self.spawn_enemy()
        else:
            if len(self.enemies_group) == 0:
                if self.boss_to_spawn:
                    self.spawn_boss()

        # Go to Win Screen:
        if self.player.state == "alive" and self.boss_to_spawn == False and len(self.enemies_group) == 0:
            self.next_state = "WIN"
            self.screen_done = True
        # Go to Game Over Screen:
        elif self.player.state == "dead":
            self.next_state = "GAME_OVER"
            self.screen_done = True

    def draw(self, surface):
        # Check Collisions:
        check_collision(self.player_bullets_group, self.enemies_group, True, False)  # Player Bullet vs Enemy
        check_collision(self.enemies_bullets_group, self.player_group, True, False)  # Enemy Bullet vs Player
        check_collision(self.enemies_group, self.player_group, False, False)  # Enemy Body vs Player Body

        # Draw Background:
        self.background.update()

        # Draw UI:
        self.ui.draw(SCREEN)

        # Update Sprites Group:
        self.player_group.update()
        self.player_bullets_group.update()
        self.enemies_group.update()
        self.enemies_bullets_group.update()
        self.effects_group.update()

        # Draw Sprite Groups:
        self.enemies_bullets_group.draw(SCREEN)
        self.enemies_group.draw(SCREEN)
        self.player_bullets_group.draw(SCREEN)
        self.player_group.draw(SCREEN)
        self.effects_group.draw(SCREEN)

        # Extras:
        speakers.action(speakers.x, speakers.y, speakers.state)

