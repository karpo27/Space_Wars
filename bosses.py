# Scripts
from constants import *
from game_objects import Explosion, explosion_group

# Modules
import pygame
from pygame import mixer
import random


class Boss(pygame.sprite.Sprite):

    def __init__(self, image, scale, movement, vel, hp, bullet, fire_delay, fire_cycles, explosion_scale):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale[0], self.image.get_height() * scale[1]))
        self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.center = [WIDTH/2, -1/4 * HEIGHT]

        # Initial Movement Animation
        self.enter_animation = True
        self.y_enter = 1/25 * HEIGHT
        self.vel_enter_y = 1

        # Movement
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.counter = 0
        self.angle = 0

        # HP
        self.hp = hp

        # Bullet
        self.bullet = bullet
        self.bullet_index = 0
        self.fire_delay = fire_delay
        self.ref_time = fire_delay
        self.fire_cycles = fire_cycles
        self.fire_cycles_counter = 0
        #self.bullet_pos = bullet_pos
        self.reload_speed = 1

        # Explosion
        self.explosion_scale = explosion_scale

    def move_hor_vert(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.left <= -0.1 * WIDTH:
            self.rect.x += self.vel_x
        if self.rect.right >= 1.1 * WIDTH:
            self.rect.x -= self.vel_x

    def move_hor_zigzag(self):
        if self.rect.y < 1/8 * HEIGHT:
            self.rect.y += self.vel_y
        else:
            if self.counter == 121:
                self.counter = 0
            if 60 < self.counter < 121:
                self.rect.x += self.vel_x
                self.counter += 1
            else:
                self.rect.x -= self.vel_x
                self.counter += 1

    def rotate(self):
        rotated_surface = pygame.transform.rotozoom(self.image_copy, self.angle, 1)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center)

        return rotated_surface, rotated_rect

    def move_hor_vert_sin(self):
        if 1/5 * WIDTH < self.rect.x < 11/15 * WIDTH:
            if self.angle == 0:
                self.rect.x += self.vel_x
            elif self.angle == -180:
                self.rect.x -= self.vel_x
        elif self.rect.x >= 11/15 * WIDTH:
            if self.angle > -180:
                self.rect.x += self.vel_x
                self.rect.y += self.vel_y
                self.angle -= 2
            elif self.angle == -180:
                self.rect.x -= self.vel_x
                self.rect.y += self.vel_y
        elif self.rect.x <= 1/5 * WIDTH:
            if self.angle < 0:
                self.rect.x -= self.vel_x
                self.rect.y += self.vel_y
                self.angle += 2
            elif self.angle == 0:
                self.rect.x += self.vel_x
                self.rect.y += self.vel_y

        return self.rotate()

    def get_hit(self):
        self.hp -= 1

        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
        explosion = Explosion(self.rect.x, self.rect.y, self.explosion_scale)
        explosion_group.add(explosion)

    def update(self):
        # Enter Level Animation
        if self.enter_animation:
            if self.rect.y <= self.y_enter:
                self.rect.y += self.vel_enter_y
            else:
                self.enter_animation = False

        else:
            if self.movement == 1:
                self.move_hor_vert()
            elif self.movement == 2:
                self.move_hor_zigzag()
            elif self.movement == 3:
                self.image, self.rect = self.move_hor_vert_sin()

            # Create Boss Bullet Object (fix later side of the bullet)
            if self.fire_delay >= self.ref_time:
                if self.fire_cycles_counter >= self.fire_cycles[self.bullet_index]:
                    for bullet_type in self.bullet[self.bullet_index]:
                        boss_bullet = BossBullet(
                            [self.rect.centerx, self.rect.centery],
                            *bosses_bullets[f'b_bullet_{bullet_type}']
                        )

                        bosses_bullet_group.add(boss_bullet)
                    self.bullet_index += 1
                else:
                    self.fire_cycles_counter += self.reload_speed
            # Reset Variables
            else:
                self.fire_delay += self.reload_speed

        if self.bullet_index == len(self.fire_cycles):
            self.bullet_index = 0
            self.fire_cycles_counter = 0
            self.fire_delay = 0


class BossBullet(pygame.sprite.Sprite):

    def __init__(self, pos, image, movement, vel, angle, sound, col_sound):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Movement
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.angle = angle

        # Sound
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

    def move_vertical(self):
        self.rect.y += self.vel_y

    def move_diagonal(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

    def rotate(self):
        rotated_surface = pygame.transform.rotozoom(self.image_copy, self.angle, 1)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center)

        return rotated_surface, rotated_rect

    def update(self):
        if self.rect.top > HEIGHT:
            self.kill()
        else:
            if self.movement == 1:
                self.move_vertical()
            elif self.movement == 2:
                self.image, self.rect = self.rotate()
                self.move_diagonal()
            elif self.movement == 3:
                pass


# Create Sprites Group:
bosses_group = pygame.sprite.Group()
bosses_bullet_group = pygame.sprite.Group()

# Bosses - Category, Image, Scale, Movement Type, Velocity, HP, Bullet Type, Fire Delay, Fire Cycles, Explosion Scale
bosses = {
    'boss_a': ['Images/Bosses/Captain_Death_Ship.png', (0.6, 0.6), 1, [0, 0], 100, ('a1', 'a2'), 200, (0.8, 0.8)],
    'boss_b': ['Images/Bosses/General_Bugfix_Ship.png', (1.1, 1.1), 1, [0, 0], 125, [('b1', 'b2', 'b3'), ('a1', 'a2')], 500, [0, 200], (2.0, 2.0)],
    'boss_c': ['Images/Bosses/Crimson_Emperor_Ship.png', (0.8, 0.8), 1, [0, 0], 150, ('c1', 'c2'), 200, (0.9, 0.9)],
}

# Bosses Bullets - Image, Movement Type, Velocity, Angle, Sound, Explosion Sound
bosses_bullets = {
    'b_bullet_a1': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-1, 5], -10, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_a2': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [1, 5], 10, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b1': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [-6, 6], -45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b2': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_b3': ['Images/Bosses_Bullets/enemy_bullet_F.png', 2, [6, 6], 45, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c1': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c2': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c3': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav'],
    'b_bullet_c4': ['Images/Bosses_Bullets/enemy_bullet_F.png', 1, [0, 6], 0, 'Sounds/laser.wav', 'Sounds/explosion.wav']
}
