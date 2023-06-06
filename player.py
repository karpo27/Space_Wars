# Scripts:
from constants import *
from character import Character
from bullet import Bullet
from game_effects import Explosion, Particle, HitParticle, Propulsion
from sound import player_laser, player_explosion, player_item_hp, player_item_life, enemy_hit

# Modules:
import pygame
import random
import math


class Player(Character):
    def __init__(self, category, img_path, scale, pos, vel, hp, lives, state, fire_rate, explo_scale, part_range, propulsion_scale, bullet_group, effects_group):
        super().__init__(category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group)
        # Image:
        self.pos = pos
        self.rect.center = self.pos

        # Start Movement Animation:
        self.start_animation = True
        self.y_start = 5/6 * HEIGHT
        # End Movement Animation:
        self.y_end = -1/7 * HEIGHT

        # HP:
        self.lives = lives
        self.hp_animation = False

        # State:
        self.state = state

        # Blink:
        self.blinks = True

        # Propulsion:
        self.propulsion_scale = propulsion_scale

    def get_hit(self, pos, col_type):
        if col_type == "hp item":
            if self.hp < 3:
                self.hp += 1
            player_item_hp.play_sound()
        elif col_type == "life item":
            self.lives += 1
            player_item_life.play_sound()
        else:
            if not self.invulnerable:
                # Hit Particles:
                if self.hp > 1 and col_type == "bullet":
                    for num_particles in range(random.randrange(6, 16)):
                        HitParticle(pos, (0, 255, 0), (134, 238, 144), 1, self.effects_group)
                # HP:
                self.hp_animation = True
                self.hp -= 1
                self.invulnerable = True
                self.invulnerable_rate = 0
                self.blink_rate = 0
                enemy_hit.play_sound()
                if self.hp < 0:
                    self.destroy()

    def destroy(self):
        # Explosion:
        self.effects_group.add(Explosion(self.rect.center, self.explosion_scale))
        player_explosion.play_sound()
        # Particles:
        for num_particles in range(random.randrange(self.part_min, self.part_max)):
            Particle(self.rect.center, self.effects_group)
        # Lives and State:
        if self.lives > 0:
            self.lives -= 1
            self.hp = 3
            self.rect.center = self.pos
            self.start_animation = True
        else:
            self.kill()
            self.state = "dead"

    def animate_start(self):
        if self.rect.y > self.y_start:
            self.rect.y -= 1
        else:
            self.start_animation = False

    def animate_end(self):
        if self.rect.bottom > self.y_end:
            self.rect.y -= 3
            # Propulsion:
            self.effects_group.add(Propulsion(self.rect.midbottom, self.propulsion_scale))
        else:
            self.end_animation = False
            self.state = "winner"

    def handle_action(self):
        if not self.keyboard_blocked:
            key = pygame.key.get_pressed()
            # Player Keyboard Diagonal Movement - (UP-LEFT, DOWN-LEFT, UP-RIGHT, DOWN-RIGHT):
            if key[pygame.K_LEFT] and key[pygame.K_UP] and self.rect.left > 0 and self.rect.top > 0:
                self.rect.x -= math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y -= math.sqrt((self.vel_y ** 2) / 2)
            elif key[pygame.K_LEFT] and key[pygame.K_DOWN] and self.rect.left > 0 and self.rect.bottom < HEIGHT:
                self.rect.x -= math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y += math.sqrt((self.vel_y ** 2) / 2)
            elif key[pygame.K_RIGHT] and key[pygame.K_UP] and self.rect.right < WIDTH and self.rect.top > 0:
                self.rect.x += math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y -= math.sqrt((self.vel_y ** 2) / 2)
            elif key[pygame.K_RIGHT] and key[pygame.K_DOWN] and self.rect.right < WIDTH and self.rect.bottom < HEIGHT:
                self.rect.x += math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y += math.sqrt((self.vel_y ** 2) / 2)
            # Player Keyboard Movement - (LEFT, RIGHT, UP, DOWN):
            elif key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.vel_x
            elif key[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.vel_x
            elif key[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.vel_y
            elif key[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.vel_y
            # Player Bullet Keyboard:
            if key[pygame.K_SPACE]:
                # Create Player Bullet Object:
                if self.fire_rate >= self.ref_time:
                    PlayerBullet(self.rect.center, *PLAYER_BULLETS['A'], self.bullet_group)
                    player_laser.play_sound()
                    self.fire_rate = 0

    def reset_variables(self):
        # Reset Fire Bullet Variables:
        if self.fire_rate < self.ref_time:
            self.fire_rate += 1


class PlayerBullet(Bullet):
    def __init__(self, pos, img_path, img_qty, scale, animation_delay, movement, vel, angle, bounce, group):
        super().__init__(pos, img_path, img_qty, scale, animation_delay, movement, vel, angle, bounce, group)

    def handle_movement(self):
        if self.rect.bottom < 0:
            self.kill()
        else:
            self.move_y()
