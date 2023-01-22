# Scripts
from constants import *

# Modules
import pygame
from pygame import mixer
import random


class Enemy(pygame.sprite.Sprite):
    # Define time delay between enemies to spawn
    time_to_spawn = random.randint(2000, 5000)
    spawn_enemy = pygame.USEREVENT + 0
    pygame.time.set_timer(spawn_enemy, time_to_spawn)

    def __init__(self, category, image, scale, movement, vel, hp, fire_rate):
        super().__init__()
        self.category = category
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale[0], self.image.get_height() * scale[1]))
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0, 3/4 * WIDTH), -80]
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.hp = hp

        # Bullet
        self.ref_time = fire_rate
        self.fire_rate = fire_rate
        self.reload_speed = 1

    def move_hor_vert(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.left <= -0.1 * WIDTH:
            self.rect.x += self.vel_x
        if self.rect.right >= 1.1 * WIDTH:
            self.rect.x -= self.vel_x

    def move_hor_zigzag(self):
        if self.rect.x < 1/4 * HEIGHT:
            self.rect.y += self.vel_y
        else:
            counter = 0
            if counter == 10:
                counter = 0
            if 5 < counter < 10:
                self.rect.x += self.vel_x
                counter += 1
            else:
                self.rect.x -= self.vel_x
                counter += 1

    def update(self):
        if self.rect.top > HEIGHT:
            self.kill()
        else:
            if self.movement == 1:
                Enemy.move_hor_vert(self)
            elif self.movement == 2:
                Enemy.move_hor_zigzag(self)

        # Enemy Bullet
        if self.rect.top > 0:
            # Create Enemy Bullet Object (add later f' self.cat)
            if self.fire_rate >= self.ref_time:
                enemy_bullet = EnemyBullet(
                    [self.rect.centerx, self.rect.centery],
                    *enemies_bullets['e_bullet_F']
                )

                enemies_bullet_group.add(enemy_bullet)
                self.fire_rate = 0

        # Reset Variables
        if self.fire_rate < self.ref_time:
            self.fire_rate += self.reload_speed


class EnemyBullet(pygame.sprite.Sprite):

    def __init__(self, pos, image, vel, sound, col_sound):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel = self.vel_x, self.vel_y = vel
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

    def update(self):
        # Enemy Bullet Movement
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.top > HEIGHT:
            self.kill()


# Create Sprites Group:
enemies_group = pygame.sprite.Group()
enemies_bullet_group = pygame.sprite.Group()

# Enemies - Category, Image, Scale, Movement Type, Velocity, HP, Fire Rate
enemies = {
    'enemy_f': [
        'F',
        'Images/Enemies/enemy_F.png',
        (0.8, 0.8),
        1,
        [round(0.04 * dt), 1],
        1,
        100
    ],
    'enemy_e': [
        'E',
        'Images/Enemies/enemy_E.png',
        (0.8, 0.8),
        1,
        [0, 4],
        1,
        180
    ],
    'enemy_d': [
        'D',
        'Images/Enemies/enemy_D.png',
        (0.8, 0.8),
        1,
        [round(0.03 * dt), 1.8],
        1,
        100
    ],
    'enemy_c': [
        'C',
        'Images/Enemies/enemy_C.png',
        (0.8, 0.8),
        2,
        [round(0.03 * dt), 1.8],
        1,
        200
    ]
}


enemies_bullets = {
    'e_bullet_F': [
        'Images/Enemies_Bullet/enemy_bullet_F.png',
        [0, round(0.12 * dt)],
        'Sounds/laser.wav',
        'Sounds/explosion.wav'
    ]
}

'''
e_bullet_E = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_E.png',
    [0, 0.22 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)

e_bullet_D = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_F.png',
    [0, 0.22 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)'''