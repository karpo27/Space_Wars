# Scripts
from constants import *
from character import Character
from game_effects import Explosion, Particle, HitParticle

# Modules
import pygame
from pygame import mixer
import random


class Enemy(Character):
    # Define time delay between enemies to spawn:
    time_to_spawn = random.randint(2000, 5000)
    spawn_enemy = pygame.USEREVENT + 0
    pygame.time.set_timer(spawn_enemy, time_to_spawn)

    def __init__(self, category, img_path, scale, movement, vel, hp, shoots, bullet, fire_rate, explo_scale, part_range, ui, bullet_group, effects_group):
        super().__init__(category, img_path, scale, movement, vel, hp, bullet, fire_rate, explo_scale, part_range, bullet_group, effects_group)
        # Image:
        self.rect.center = [random.randint(int(0 + self.rect.width/2), int(WIDTH - self.rect.width/2)), -80]

        # Movement:
        self.counter = 0

        # Bullet:
        self.shoots = shoots

        # Score:
        self.ui = ui
        self.score = hp * 10

    def movement_1(self):
        self.move_x()
        self.move_y()
        if self.rect.left <= 0:
            self.vel_x = self.vel_x * -1
        elif self.rect.right >= WIDTH:
            self.vel_x = self.vel_x * -1

    def movement_2(self):
        if self.rect.y < HEIGHT/8:
            self.move_y()
        else:
            if self.counter == 121:
                self.counter = 0
            if 60 < self.counter < 121:
                self.rect.x += self.vel_x
                self.counter += 1
            else:
                self.rect.x -= self.vel_x
                self.counter += 1

    def movement_3(self):
        if self.rect.y < HEIGHT/3:
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

    def movement_4(self):
        if self.rect.y < HEIGHT/4:
            self.rect.y += self.vel_y
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0:
                self.vel_x = self.vel_x * -1
            elif self.rect.right >= WIDTH:
                self.vel_x = self.vel_x * -1

    def movement_5(self):
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
            # Create Enemy Bullet:
            if self.shoots and self.fire_rate >= self.ref_time:
                for bullet_type in self.bullet:
                    EnemyBullet(self.rect.center, *ENEMIES_BULLETS[f'{bullet_type}'], self.bullet_group)
                    self.fire_rate = 0
            # Reset Variables:
            elif self.fire_rate < self.ref_time:
                self.fire_rate += 1

    def get_hit(self, pos, col_type):
        # Hit Particles:
        if self.hp > 1:
            for num_particles in range(random.randrange(6, 18)):
                HitParticle(pos, (0, 0, 255), (135, 206, 250), -1, self.effects_group)
        # HP:
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
        # Explosion:
        self.effects_group.add(Explosion(self.rect.x, self.rect.y, self.explosion_scale))
        # Particles:
        for num_particles in range(random.randrange(self.part_min, self.part_max)):
            Particle(self.rect.center, self.effects_group)
        # Score:
        self.ui.update_score(self.score)

    def update(self):
        if self.rect.top > HEIGHT:
            self.kill()
        else:
            if self.movement == 1:
                self.movement_1()
            elif self.movement == 2:
                self.movement_2()
            elif self.movement == 3:
                self.movement_3()
            elif self.movement == 4:
                self.movement_4()
            elif self.movement == 5:
                self.image, self.rect = self.movement_5()

        # Enemy Bullet:
        self.spawn_bullet()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, pos, img_path, movement, vel, angle, sound, col_sound, group):
        super().__init__()
        self.sprites = []
        for i in range(1, 4):
            images = pygame.image.load(f'{img_path}{i}.png').convert_alpha()
            images = pygame.transform.scale(images, (images.get_width() * 0.2, images.get_height() * 0.2))
            self.sprites.append(images)

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.counter = 0
        self.image_copy = self.image

        # Movement
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.angle = angle

        # Sound
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

        # Groups:
        group.add(self)

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
        # Animation:
        animation_delay = 8
        self.counter += 1

        if self.counter >= animation_delay and self.index < len(self.sprites) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.sprites[self.index]
            self.image_copy = self.image

        # Movement:
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



