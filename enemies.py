# Scripts
from constants import *
from character import Character
from bullet import Bullet
from game_effects import Explosion, Particle, HitParticle
from sound import enemy_laser, enemy_explosion, enemy_e_flyby, player_hit

# Modules
import pygame
from pygame import mixer
import random


class Enemy(Character):
    def __init__(self, category, img_path, scale, movement, vel, hp, shoot, bullet, fire_rate, explo_scale, part_range, ui, bullet_group, effects_group):
        super().__init__(category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group)
        # Image:
        self.rect.center = [random.randint(int(0 + self.rect.width/2), int(WIDTH - self.rect.width/2)), -80]

        # Movement:
        self.movement = movement
        self.counter = 0

        # Bullet:
        self.shoot = shoot
        self.bullet = bullet

        # Score:
        self.ui = ui
        self.score = hp * 10

        # Sound:
        if self.category == 'E':
            enemy_e_flyby.play_sound()

    def movement_1(self):
        self.move_x()
        self.move_y()
        self.restrict_x(0, WIDTH)

    def movement_2(self, max_height):
        if self.rect.y < max_height:
            self.move_y()
        else:
            self.restrict_x_counter(100)
            self.restrict_x(0, WIDTH)

    def movement_3(self):
        if self.rect.y < HEIGHT/4:
            self.move_y()
        else:
            self.move_x()
            self.restrict_x(0, WIDTH)

    def movement_4(self, left_limit, right_limit):
        self.move_x()
        if self.rect.x >= right_limit:
            self.move_y()
            if self.angle > -180:
                self.angle -= 2
            elif self.angle == -180:
                self.vel_x = self.vel_x * -1
                self.angle = -540
        elif self.rect.x <= left_limit:
            self.move_y()
            if self.angle < -360:
                self.angle += 2
            elif self.angle == -360:
                self.vel_x = self.vel_x * -1
                self.angle = 0
        return self.rotate()

    def spawn_bullet(self):
        if self.rect.top > 0:
            # Create Enemy Bullet:
            if self.shoot and self.fire_rate >= self.ref_time:
                for bullet_type in self.bullet:
                    EnemyBullet(self.rect.center, *ENEMIES_BULLETS[f'{bullet_type}'], self.bullet_group)
                    self.fire_rate = 0
                enemy_laser.play_sound()
            # Reset Variables:
            elif self.fire_rate < self.ref_time:
                self.fire_rate += 1

    def get_hit(self, pos, col_type):
        # Hit Particles:
        if self.hp > 1:
            for num_particles in range(random.randrange(6, 18)):
                HitParticle(pos, (0, 0, 255), (135, 206, 250), -1, self.effects_group)
            player_hit.play_sound()
        # HP:
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
        # Explosion:
        self.effects_group.add(Explosion(self.rect.center, self.explosion_scale))
        enemy_explosion.play_sound()
        # Particles:
        for num_particles in range(random.randrange(self.part_min, self.part_max)):
            Particle(self.rect.center, self.effects_group)
        # Score:
        self.ui.update_score(self.score)

    def handle_action(self):
        if self.rect.top > HEIGHT:
            self.kill()
        else:
            if self.movement == 1:
                self.movement_1()
            elif self.movement == 2:
                self.movement_2(HEIGHT/8)
            elif self.movement == 3:
                self.movement_2(HEIGHT/3)
            elif self.movement == 4:
                self.movement_3()
            elif self.movement == 5:
                self.image, self.rect = self.movement_4(WIDTH/5, 11/15 * WIDTH)
        # Enemy Bullet:
        self.spawn_bullet()


class EnemyBullet(Bullet):
    def __init__(self, pos, img_path, img_qty, scale, animation_delay, movement, vel, angle, bounce, group):
        super().__init__(pos, img_path, img_qty, scale, animation_delay, movement, vel, angle, bounce, group)

    def handle_movement(self):
        if self.rect.top > HEIGHT or self.rect.bottom < 0:
            self.kill()
        else:
            if self.movement == 1:
                self.move_y()
            elif self.movement == 2:
                self.image, self.rect = self.rotate()
                self.move_x()
                self.move_y()
