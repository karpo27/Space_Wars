# Scripts
from constants import *
from character import Character
from bullet import Bullet
from enemies import EnemyBullet
from game_effects import Explosion, Particle, HitParticle

# Modules
import pygame
from pygame import mixer
import random
import secrets


class Boss(Character):
    def __init__(self, category, img_path, scale, action, vel, hp, shoot, fire_rate, explo_scale, part_range, ui, bullet_group, effects_group):
        super().__init__(category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group)
        # Image:
        self.rect.center = [WIDTH/2, -HEIGHT/4]

        # Initial Movement Animation:
        self.enter_animation = True
        self.y_enter = HEIGHT/25
        self.vel_enter_y = 1

        # Action:
        self.next_action = False
        self.action = action
        self.action_copy = self.action.copy()
        self.movement_action = secrets.choice(self.action_copy)
        self.action_copy.remove(self.movement_action)
        self.movement_duration = self.movement_action['duration']
        self.movement_rate = 0
        self.ref_time = self.movement_action['fire_rate']
        self.fire_rate = self.ref_time
        self.ref_time_2 = self.movement_action['fire_rate_2']
        self.fire_rate_2 = self.ref_time_2

        # HP:
        self.half_hp = self.hp/2

        # Bullet:
        self.shoot = shoot
        self.index = 0
        self.bullet = self.movement_action['bullet']
        self.bullet_qty = self.movement_action['qty'][0]
        self.bullet_type_qty = 1
        self.bullet_type_counter = 0
        self.reset_shoot()

        # Explosion:

        # Score:
        self.ui = ui
        self.score = hp * 10

    def reset_movement_action(self):
        if len(self.action_copy) == 0:
            self.action_copy = self.action.copy()
        self.movement_action = secrets.choice(self.action_copy)
        self.action_copy.remove(self.movement_action)
        self.reset_shoot()
        self.movement_duration = self.movement_action['duration']
        self.movement_rate = 0
        self.ref_time = self.movement_action['fire_rate']
        self.fire_rate = self.ref_time
        self.ref_time_2 = self.movement_action['fire_rate_2']
        self.fire_rate_2 = self.ref_time_2
        self.index = 0
        self.bullet = self.movement_action['bullet']
        if self.hp < self.half_hp:
            self.bullet_qty = self.movement_action['qty'][1]
        else:
            self.bullet_qty = self.movement_action['qty'][0]
        self.bullet_type_qty = 1
        self.bullet_type_counter = 0
        self.next_action = False

    def movement_w(self):
        if self.rect.left == 0 or self.rect.right == WIDTH:
            self.shoot = True
        self.move_x()
        self.restrict_x(0, WIDTH)

    def movement_x(self):
        self.move_x()
        self.restrict_x(0, WIDTH)

    def movement_y(self):
        self.move_y()

    def movement_z(self):
        self.move_y()
        self.angle -= 4
        return self.rotate()

    def reset_shoot(self):
        if self.movement_action in [X, Y, Z]:
            self.shoot = True
        else:
            self.shoot = False

    def spawn_bullet(self):
        if self.rect.top > 0:
            # Create Enemy Bullet:
            if self.shoot and self.fire_rate >= self.ref_time:
                if self.bullet_qty >= self.bullet_type_qty:
                    if self.fire_rate_2 >= self.ref_time_2:
                        for bullet_type in self.bullet[self.index]:
                            EnemyBullet(self.rect.center, *BOSSES_BULLETS[f'{bullet_type}'], self.bullet_group)
                        SOUNDS['enemy_laser'].play().set_volume(VOL_ENEMY_LASER)
                        self.fire_rate_2 = 0
                        self.bullet_type_qty += 1
                    else:
                        self.fire_rate_2 += 1
                else:
                    # Reset Fire Rate:
                    self.bullet_type_qty = 1
                    self.index += 1
                    self.fire_rate = 0
            else:
                self.fire_rate += 1
        # Reset Index:
        if self.index == len(self.bullet):
            self.index = 0

    def get_hit(self, pos, col_type):
        # Hit Particles:
        if self.hp > 1:
            for num_particles in range(random.randrange(6, 18)):
                HitParticle(pos, (0, 0, 255), (135, 206, 250), -1, self.effects_group)
            SOUNDS['player_hit'].play().set_volume(VOL_PLAYER_HIT)
        # HP:
        self.hp -= 1
        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
        # Explosion:
        self.effects_group.add(Explosion(self.rect.x, self.rect.y, self.explosion_scale))
        SOUNDS['boss_explosion'].play().set_volume(VOL_BOSS_EXPLOSION)
        # Particles:
        for num_particles in range(random.randrange(self.part_min, self.part_max)):
            Particle(self.rect.center, self.effects_group)
        # Score:
        self.ui.update_score(self.score)

    def animate(self):
        if self.rect.y <= self.y_enter:
            self.rect.y += self.vel_enter_y
        else:
            self.enter_animation = False

    def handle_action(self):
        if not self.next_action:
            if self.movement_action == X:
                self.movement_x()
            elif self.movement_action == Y:
                self.movement_y()
            elif self.movement_action == Z:
                self.image, self.rect = self.movement_z()
            elif self.movement_action == W:
                self.movement_w()
            # Boss Bullet:
            if self.hp < self.half_hp:
                self.bullet_qty = self.movement_action['qty'][1]
            self.spawn_bullet()
        else:
            self.reset_movement_action()

    def reset_variables(self):
        # Reset Animation when leaving Screen:
        if self.rect.top > HEIGHT:
            self.enter_animation = True
            self.rect.center = [WIDTH/2, -HEIGHT/4]
            self.angle = 0
            self.image, self.rect = self.rotate()
            self.movement_rate = 0
            self.next_action = True
        else:
            # Reset Movement Variables:
            if self.movement_rate < self.movement_duration:
                self.movement_rate += 1
            elif self.movement_rate >= self.movement_duration:
                self.movement_rate = 0
                self.next_action = True

