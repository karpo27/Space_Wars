# Scripts
from constants import *
from game_effects import *

# Modules
import pygame
from pygame import mixer
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel, hp, lives, explosion_scale):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel = self.vel_x, self.vel_y = vel

        # HP:
        self.hp = hp
        self.lives = lives
        self.hp_animation = False

        # State:
        self.state = "alive"
        self.invulnerable = False
        self.invulnerable_ref_time = 120
        self.invulnerable_rate = 120

        # Initial Movement Animation:
        self.enter_animation = True
        self.y_enter = 5 / 6 * HEIGHT
        self.vel_enter_y = 0.2

        # Bullet:
        self.ref_time = 30
        self.fire_rate = 30
        self.reload_speed = 1

        # Explosion:
        self.explosion_scale = explosion_scale

        # Rotation:
        self.angle = 0

    def get_hit(self):
        print(self.invulnerable)
        print(self.invulnerable_rate)
        if not self.invulnerable:
            self.hp_animation = True
            self.hp -= 1
            self.invulnerable = True
            self.invulnerable_rate = 0

            if self.hp < 0:
                self.destroy()

    def destroy(self):
        self.kill()
        explosion = Explosion(self.rect.x, self.rect.y, self.explosion_scale)
        EXPLOSION_GROUP.add(explosion)
        if self.lives > 0:
            self.lives -= 1
            self.hp = 3
        else:
            self.state = "dead"

    def update(self):
        # Enter Level Animation:
        if self.enter_animation:
            if self.rect.y > self.y_enter:
                self.rect.y -= self.vel_enter_y
            else:
                self.enter_animation = False
        # Press Keyboard:
        else:
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

            # Player Keyboard Movement - (LEFT, RIGHT, UP, DOWN)
            elif key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.vel_x
            elif key[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.vel_x
            elif key[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.vel_y
            elif key[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.vel_y

            # Player Bullet Keyboard
            if key[pygame.K_SPACE]:
                # Create Player Bullet Object
                if self.fire_rate >= self.ref_time:
                    PlayerBullet(self.rect.center, *PLAYER_BULLETS['player_bullet_d'])
                    self.fire_rate = 0

        # Invulnerability:
        if self.invulnerable:
            if self.invulnerable_rate >= self.invulnerable_ref_time:
                self.invulnerable = False
            else:
                self.invulnerable_rate += 1

        # Reset Fire Bullet Variables:
        if self.fire_rate < self.ref_time:
            self.fire_rate += self.reload_speed


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, pos, image, vel, sound, col_sound):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Movement:
        self.vel = self.vel_x, self.vel_y = vel

        # Sound:
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

        # Groups:
        PLAYER_BULLETS_GROUP.add(self)

    def update(self):
        # Player Bullet Movement:
        self.rect.y -= self.vel_y

        if self.rect.bottom < 0:
            self.kill()
