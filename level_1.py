# Scripts:
from game_effects import *
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
        if len(self.enemies_group) < len(self.enemies):
            if event.type == Enemy.spawn_enemy:
                k = self.enemies[len(self.enemies_group)]
                # Generate Enemies
                new_enemy = Enemy(*k, self.enemies_bullets_group, self.effects_group)
                self.enemies_group.add(new_enemy)

        # Spawn Boss According to Level:
        if len(self.bosses_group) < len(self.boss):
            if event.type == Enemy.spawn_enemy:
                k = self.boss[len(self.bosses_group)]
                # Generate Boss
                new_boss = Boss(*k, self.enemies_bullets_group, self.effects_group)
                self.enemies_group.add(new_boss)

        # Go to Game Over Screen:
        if self.player.state == "dead":
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

