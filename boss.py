# Scripts
from constants import *
from character import Character
from enemies import EnemyBullet
from game_effects import Explosion, Particle, HitParticle
from sound import boss_laser, boss_explosion, player_hit, boss_bg
from hud import score

# Modules
import pygame
import random
import secrets


class Boss(Character):
    def __init__(self, category, img_path, scale, action, vel, hp, shoot, fire_rate, explo_scale, part_range, bullet_group, effects_group):
        super().__init__(category, img_path, scale, vel, hp, fire_rate, explo_scale, part_range, bullet_group, effects_group)
        # Image:
        self.rect.center = [WIDTH/2, -HEIGHT/4]

        # Initial Movement Animation:
        self.start_animation = True
        self.y_start = HEIGHT / 25
        self.vel_start_y = 1

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

        # State:
        self.invulnerable = True
        self.invulnerable_ref_time = 300
        self.invulnerable_rate = 0

        # Explosion:
        self.destroy_animation = False
        self.explosion_index = 0
        self.explosion_ref_time = 22
        self.explosion_rate = 22

        # Score:
        self.enemy_score = hp * 10

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
                        boss_laser.play_sound()
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
        print(self.invulnerable)
        if not self.invulnerable:
            # Hit Particles:
            if self.hp > 1:
                for num_particles in range(random.randrange(6, 18)):
                    HitParticle(pos, (0, 0, 255), (135, 206, 250), -1, self.effects_group)
                player_hit.play_sound()
            # HP:
            self.hp -= 1
            if self.hp == 0:
                self.vel_x, self.vel_y = 0, 0
                self.angle = 0
                self.destroy_animation = True
                # Score:
                score.update_score(self.enemy_score)
        print(self.hp)

    def destroy(self):
        pygame.mixer.music.fadeout(3000)
        if self.explosion_index < 14:
            if self.explosion_rate >= self.explosion_ref_time:
                # Explosion:
                if self.explosion_index == 13:
                    explosion_scale = self.explosion_scale
                    explosion_pos = [self.rect.width/2, self.rect.height/2]
                else:
                    explosion_scale = secrets.choice([0.6, 0.7, 0.8, 0.9, 1])
                    explosion_pos = [random.randint(0, int(self.rect.width)), random.randint(0, int(self.rect.height))]
                self.effects_group.add(Explosion([self.rect.right - explosion_pos[0], self.rect.bottom - explosion_pos[1]], explosion_scale))
                boss_explosion.play_sound()
                # Particles:
                for num_particles in range(random.randrange(self.part_min, self.part_max)):
                    Particle([self.rect.right - explosion_pos[0], self.rect.bottom - explosion_pos[1]], self.effects_group)
                self.explosion_index += 1
                self.explosion_rate = 0
            else:
                self.explosion_rate += 1
        else:
            self.kill()

    def animate_start(self):
        if self.rect.y <= self.y_start:
            self.rect.y += self.vel_start_y
        else:
            self.start_animation = False

    def handle_action(self):
        # Explosion Animation:
        if self.destroy_animation:
            self.destroy()
        else:
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
            self.start_animation = True
            self.invulnerable = True
            self.invulnerable_rate = 0
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
