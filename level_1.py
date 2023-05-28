# Scripts:
from game_effects import Explosion, Particle
from base_state import BaseState
from sound import boss_bg, win_bg, game_over_bg
from pause import *
from bg_creator import BGCreator
from player import *
from ui import UI
from enemies import *
from boss import *
from collisions import *

# Modules:
import pygame

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

        # Initialize Objects:
        self.background = BGCreator(*BACKGROUNDS['level_1'])
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
        pygame.mixer.music.pause()

    def reset_enemy_timer(self, time):
        self.time_to_spawn = time
        pygame.time.set_timer(self.enemy_event, self.time_to_spawn)

    def spawn_enemy(self):
        if 0 <= self.enemy_index <= (len(self.enemies) - 1) * 1 / 3:
            self.time_to_spawn = 4000
            self.reset_enemy_timer(self.time_to_spawn)
        elif (len(self.enemies) - 1) * 1 / 3 < self.enemy_index <= (len(self.enemies) - 1) * 2 / 3:
            self.time_to_spawn = 3000
            self.reset_enemy_timer(self.time_to_spawn)
        elif (len(self.enemies) - 1) * 2 / 3 < self.enemy_index <= (len(self.enemies) - 1):
            self.time_to_spawn = 1500
        self.reset_enemy_timer(self.time_to_spawn)
        k = self.enemies[self.enemy_index]
        self.enemies_group.add(Enemy(*k, self.ui, self.enemies_bullets_group, self.effects_group))
        self.enemy_index += 1

    def spawn_boss(self):
        if self.boss_to_spawn:
            k = self.boss[0]
            self.enemies_group.add(Boss(*k, self.ui, self.enemies_bullets_group, self.effects_group))
            self.boss_to_spawn = False
            boss_bg.play_bg_music(-1, 7000)

    def check_win(self):
        if self.player.state == "alive" and not self.boss_to_spawn and len(self.enemies_group) == 0:
            self.next_state = "WIN"
            self.screen_done = True
            win_bg.play_bg_music(-1)

    def check_game_over(self):
        if self.player.state == "dead":
            self.next_state = "GAME_OVER"
            self.screen_done = True
            game_over_bg.play_bg_music(-1)

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            # Pause Menu Selection:
            if event.key == pygame.K_ESCAPE:
                self.handle_pause()

        # Spawn Enemies According to Level:
        if event.type == self.enemy_event and self.enemy_index < len(self.enemies):
            self.spawn_enemy()

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
