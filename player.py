# Scripts
from constants import *
from game_effects import *

# Modules
import pygame
from pygame import mixer
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, img_path, pos, vel, hp, lives, state, explo_scale, part_range, bullet_group, effects_group):
        super().__init__()
        self.img_path = img_path
        self.image = pygame.image.load(self.img_path).convert_alpha()
        self.rect = self.image.get_rect()
        self.pos = pos
        self.rect.center = self.pos
        self.vel = self.vel_x, self.vel_y = vel

        # HP:
        self.hp = hp
        self.lives = lives
        self.hp_animation = False

        # State:
        self.state = state
        self.invulnerable = False
        self.invulnerable_ref_time = 120
        self.invulnerable_rate = 120

        # Blink:
        self.empty_surface = pygame.Surface(self.image.get_size(), pygame.SRCALPHA)
        self.blink_ref_time = self.invulnerable_ref_time/20
        self.blink_rate = 0

        # Initial Movement Animation:
        self.enter_animation = True
        self.y_enter = 5/6 * HEIGHT
        self.vel_enter_y = 0.2

        # Bullet:
        self.bullet_group = bullet_group
        self.ref_time = 30
        self.fire_rate = 30
        self.reload_speed = 1

        # Rotation:
        self.angle = 0

        # Effects:
        self.effects_group = effects_group
        self.explosion_scale = explo_scale
        self.part_min, self.part_max = part_range

    def get_hit(self):
        if not self.invulnerable:
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

    def blink_image(self):
        if self.blink_rate < self.blink_ref_time:
            self.image = self.empty_surface
        elif self.blink_ref_time <= self.blink_rate < 2 * self.blink_ref_time:
            self.image = pygame.image.load(self.img_path).convert_alpha()
        else:
            self.blink_rate = 0

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
                    PlayerBullet(self.rect.center, *PLAYER_BULLETS['player_bullet_d'], self.bullet_group)
                    self.fire_rate = 0

        # Invulnerability:
        if self.invulnerable:
            if self.invulnerable_rate >= self.invulnerable_ref_time:
                self.invulnerable = False
                self.image = pygame.image.load(self.img_path).convert_alpha()
            else:
                self.invulnerable_rate += 1
                self.blink_rate += 1
                self.blink_image()

        # Reset Fire Bullet Variables:
        if self.fire_rate < self.ref_time:
            self.fire_rate += self.reload_speed


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, pos, path, vel, sound, col_sound, group):
        super().__init__()
        self.sprites = []
        for i in range(1, 6):
            images = pygame.image.load(path + f'{i}.png').convert_alpha()
            images = pygame.transform.scale(images, (images.get_width() * 0.4, images.get_height() * 0.4))
            self.sprites.append(images)

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.counter = 0

        # Movement:
        self.vel = self.vel_x, self.vel_y = vel

        # Sound:
        #self.sound = mixer.Sound(sound)
        #self.col_sound = mixer.Sound(col_sound)

        # Groups:
        group.add(self)

    def update(self):
        # Player Bullet Movement:
        self.rect.y -= self.vel_y

        # Animation
        animation_delay = 6
        self.counter += 1

        if self.counter >= animation_delay and self.index < len(self.sprites) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.sprites[self.index]

        if self.rect.bottom < 0:
            self.kill()