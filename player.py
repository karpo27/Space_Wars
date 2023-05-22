# Scripts:
from constants import *
from character import Character
from bullet import Bullet
from game_effects import *

# Modules:
import pygame
from pygame import mixer
import math


class Player(Character):
    def __init__(self, category, img_path, scale, pos, vel, hp, lives, state, fire_rate, explo_scale, part_range, bullet_group, effects_group):
        super().__init__(category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group)
        # Image:
        self.pos = pos
        self.rect.center = self.pos

        # Initial Movement Animation:
        self.enter_animation = True
        self.y_enter = 5 / 6 * HEIGHT
        self.vel_enter_y = 0.2

        # HP:
        self.lives = lives
        self.hp_animation = False

        # State:
        self.state = state

    def get_hit(self, pos, col_type):
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

            if self.hp < 0:
                self.destroy()

    def destroy(self):
        # Explosion:
        self.effects_group.add(Explosion(self.rect.x, self.rect.y, self.explosion_scale))
        # Particles:
        for num_particles in range(random.randrange(self.part_min, self.part_max)):
            Particle(self.rect.center, self.effects_group)
        # Lives and State:
        if self.lives > 0:
            self.lives -= 1
            self.hp = 3
            self.rect.center = self.pos
            self.enter_animation = True
        else:
            self.kill()
            self.state = "dead"

    def animate(self):
        if self.rect.y > self.y_enter:
            self.rect.y -= self.vel_enter_y
        else:
            self.enter_animation = False

    def handle_action(self):
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
