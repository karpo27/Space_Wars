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
        for enemy in ENEMIES_LVL1:
            self.enemies.append(ENEMIES[f'{enemy}'])
        self.boss = [BOSSES['b']]
        self.boss_to_spawn = True

        # Define time delay between enemies to spawn:
        self.time_to_spawn = 5000
        self.enemy_event = pygame.USEREVENT + 0
        pygame.time.set_timer(self.enemy_event, self.time_to_spawn)

    def handle_pause(self):
        self.next_state = "PAUSE"
        self.screen_done = True

    def reset_enemy_timer(self, time):
        self.time_to_spawn = time
        pygame.time.set_timer(self.enemy_event, self.time_to_spawn)

    def spawn_enemy(self):
        k = self.enemies[self.enemy_index]
        self.enemies_group.add(Enemy(*k, self.ui, self.enemies_bullets_group, self.effects_group))
        self.enemy_index += 1

    def spawn_boss(self):
        if self.boss_to_spawn:
            k = self.boss[0]
            self.enemies_group.add(Boss(*k, self.ui, self.enemies_bullets_group, self.effects_group))
            self.boss_to_spawn = False

    def check_win(self):
        if self.player.state == "alive" and not self.boss_to_spawn and len(self.enemies_group) == 0:
            self.next_state = "WIN"
            self.screen_done = True

    def check_game_over(self):
        if self.player.state == "dead":
            self.next_state = "GAME_OVER"
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
                self.handle_pause()

        # Spawn Enemies According to Level:
        if event.type == self.enemy_event:
            if 0 <= self.enemy_index <= (len(self.enemies) - 1) * 1/3:
                self.time_to_spawn = 5000
                self.spawn_enemy()
                self.reset_enemy_timer(self.time_to_spawn)
            elif (len(self.enemies) - 1) * 1/3 < self.enemy_index <= (len(self.enemies) - 1) * 2/3:
                self.time_to_spawn = 2500
                self.spawn_enemy()
                self.reset_enemy_timer(self.time_to_spawn)
            elif (len(self.enemies) - 1) * 2/3 < self.enemy_index <= (len(self.enemies) - 1):
                self.time_to_spawn = 500
                self.spawn_enemy()
                self.reset_enemy_timer(self.time_to_spawn)
        # Spawn Boss if there's no more enemies:
        if self.enemy_index == len(self.enemies) and len(self.enemies_group) == 0:
            self.spawn_boss()

        # Check Win Condition:
        self.check_win()
        # Check Game Over Condition:
        self.check_game_over()

    def draw(self, surface):
        # Check Collisions:
        check_collision(self.player_bullets_group, self.enemies_group, True, False, "bullet")  # Player Bullet vs Enemy
        check_collision(self.enemies_bullets_group, self.player_group, True, False, "bullet")  # Enemy Bullet vs Player
        check_collision(self.enemies_group, self.player_group, False, False, "body")  # Enemy Body vs Player Body

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
