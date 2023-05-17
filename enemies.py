# Scripts
from constants import *
from game_effects import Explosion, Particle

# Modules
import pygame
from pygame import mixer
import random


class Enemy(pygame.sprite.Sprite):
    # Define time delay between enemies to spawn:
    time_to_spawn = random.randint(2000, 5000)
    spawn_enemy = pygame.USEREVENT + 0
    pygame.time.set_timer(spawn_enemy, time_to_spawn)

    def __init__(self, category, img_path, scale, movement, vel, hp, shoots, bullet, fire_rate, explosion_scale):
        super().__init__()
        self.category = category
        self.image = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale[0], self.image.get_height() * scale[1]))
        self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0, 3/4 * WIDTH), -80]

        # Movement:
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.counter = 0
        self.angle = 0

        # HP:
        self.hp = hp

        # Bullet:
        self.shoots = shoots
        self.bullet = bullet
        self.ref_time = fire_rate
        self.fire_rate = fire_rate
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

    def spawn_bullet(self):
        if self.rect.top > 0:
            # Create Enemy Bullet Object (fix later side of the bullet)
            if self.shoots and self.fire_rate >= self.ref_time:
                for bullet_type in self.bullet:
                    EnemyBullet(self.rect.center, *ENEMIES_BULLETS[f'e_bullet_{bullet_type}'])
                    self.fire_rate = 0
            # Reset Variables
            elif self.fire_rate < self.ref_time:
                self.fire_rate += self.reload_speed

    def get_hit(self):
        self.hp -= 1

        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
        explosion = Explosion(self.rect.x, self.rect.y, self.explosion_scale)
        EXPLOSION_GROUP.add(explosion)
        for num_particles in range(random.randrange(5, 30)):
            Particle(self.rect.center)

    def update(self):
        if self.rect.top > HEIGHT:
            self.kill()
        else:
            if self.movement == 1:
                self.move_hor_vert()
            elif self.movement == 2:
                self.move_hor_zigzag()
            elif self.movement == 3:
                self.image, self.rect = self.move_hor_vert_sin()

        # Enemy Bullet:
        self.spawn_bullet()


class EnemyBullet(pygame.sprite.Sprite):
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

        # Groups:
        ENEMIES_BULLETS_GROUP.add(self)

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



