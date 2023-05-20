# Scripts
from constants import *
from game_effects import Explosion, Particle, HitParticle

# Modules
import pygame
from pygame import mixer
import random


class Enemy(pygame.sprite.Sprite):
    # Define time delay between enemies to spawn:
    time_to_spawn = random.randint(2000, 5000)
    spawn_enemy = pygame.USEREVENT + 0
    pygame.time.set_timer(spawn_enemy, time_to_spawn)

    def __init__(self, category, img_path, scale, movement, vel, hp, shoots, bullet, fire_rate, explo_scale, part_range, ui, bullet_group, effects_group):
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
        self.bullet_group = bullet_group
        self.shoots = shoots
        self.bullet = bullet
        self.ref_time = fire_rate
        self.fire_rate = fire_rate
        self.reload_speed = 1

        # Explosion:
        self.effects_group = effects_group
        self.explosion_scale = explo_scale
        self.part_min, self.part_max = part_range

        # Score:
        self.ui = ui
        self.score = hp * 10

    def move_hor_vert(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y
        if self.rect.left <= 0:
            self.vel_x = self.vel_x * -1
        elif self.rect.right >= WIDTH:
            self.vel_x = self.vel_x * -1

    def move_hor_zigzag(self):
        if self.rect.y < HEIGHT/8:
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

    def move_hor_zigzag_2(self):
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

    def move_hor_zigzag_3(self):
        if self.rect.y < HEIGHT/4:
            self.rect.y += self.vel_y
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0:
                self.vel_x = self.vel_x * -1
            elif self.rect.right >= WIDTH:
                self.vel_x = self.vel_x * -1

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
                    EnemyBullet(self.rect.center, *ENEMIES_BULLETS[f'e_bullet_{bullet_type}'], self.bullet_group)
                    self.fire_rate = 0
            # Reset Variables
            elif self.fire_rate < self.ref_time:
                self.fire_rate += self.reload_speed

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
                self.move_hor_vert()
            elif self.movement == 2:
                self.move_hor_zigzag()
            elif self.movement == 3:
                self.image, self.rect = self.move_hor_vert_sin()
            elif self.movement == 4:
                self.move_hor_zigzag_2()
            elif self.movement == 5:
                self.move_hor_zigzag_3()

        # Enemy Bullet:
        self.spawn_bullet()


class EnemyBullet(pygame.sprite.Sprite):
    def __init__(self, pos, path, movement, vel, angle, sound, col_sound, group):
        super().__init__()
        self.sprites = []
        for i in range(1, 4):
            images = pygame.image.load(path + f'{i}.png').convert_alpha()
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



