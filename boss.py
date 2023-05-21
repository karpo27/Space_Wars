# Scripts
from constants import *
from character import Character
from game_effects import Explosion, Particle, HitParticle

# Modules
import pygame
from pygame import mixer
import random
import secrets


class Boss(Character):

    def __init__(self, category, img_path, scale, action, vel, hp, fire_rate, explo_scale, part_range, ui, bullet_group, effects_group):
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
        self.movement_action = "Y-ANGLE"
        # self.movement_action = secrets.choice(self.movements_type)
        self.movement_ref_time = 800
        self.movement_rate = 0
        # X:
        self.ref_time = fire_rate
        self.fire_rate = self.ref_time
        self.ref_time_2 = 20
        self.fire_rate_2 = self.ref_time_2
        # X-BEAM:
        self.limit_left = WIDTH/8
        self.limit_right = 7/9 * WIDTH
        self.x_beam_pos = secrets.choice([self.limit_left, self.limit_right])
        self.x_beam_align = False

        # HP:
        self.half_hp = self.hp/2

        # Bullet:
        self.index = 0
        self.bullet = self.action[self.movement_action]
        self.bullet_type_qty = 1
        self.bullet_type_counter = 0

        # Explosion:
        self.effects_group = effects_group
        self.explosion_scale = explo_scale
        self.part_min, self.part_max = part_range

        # Score:
        self.ui = ui
        self.score = hp * 10

    def move_x(self, limit_left, limit_right):
        if self.rect.left <= limit_left:
            self.vel_x = self.vel_x * -1
        elif self.rect.right >= limit_right:
            self.vel_x = self.vel_x * -1
        self.rect.x += self.vel_x

    def move_y(self, value):
        self.rect.y += self.vel_y + value

    def move_y_angle(self):
        self.move_y(2)
        self.angle += 4
        return self.rotate()

    def move_x_beam(self, pos):
        if pos < self.rect.x:
            self.rect.x -= self.vel_x
        else:
            self.rect.x += self.vel_x

    def rotate(self):
        rotated_surface = pygame.transform.rotozoom(self.image_copy, self.angle, 1)
        rotated_rect = rotated_surface.get_rect(center=self.rect.center)
        return rotated_surface, rotated_rect

    def spawn_bullet(self, ref_qty):
        if self.rect.top > 0:
            # Create Enemy Bullet:
            if self.fire_rate >= self.ref_time:
                if ref_qty >= self.bullet_type_qty:
                    if self.fire_rate_2 >= self.ref_time_2:
                        for bullet_type in self.bullet[self.index]:
                            BossBullet(self.rect.center, *BOSSES_BULLETS[f'{bullet_type}'], self.bullet_group)
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
        # Enter Level Animation
        if self.enter_animation:
            if self.rect.y <= self.y_enter:
                self.rect.y += self.vel_enter_y
            else:
                self.enter_animation = False
        # Perform Action:
        else:
            if not self.next_action:
                if self.movement_action == "X":
                    if self.hp > self.half_hp:
                        self.spawn_bullet(1)
                    else:
                        self.spawn_bullet(3)
                    self.move_x(0, WIDTH)
                    # Reset Movement Variables:
                    '''
                    if self.movement_rate < self.movement_ref_time:
                        self.movement_rate += 1
                    elif self.movement_rate >= self.movement_ref_time:
                        self.next_action = True
                        self.movement_rate = 0
                    '''
                elif self.movement_action == "Y":
                    self.move_y(1)
                elif self.movement_action == "Y-ANGLE":
                    self.image, self.rect = self.move_y_angle()
                elif self.movement_action == "X-BEAM":
                    if not self.x_beam_align:
                        if self.limit_left < self.rect.x < self.limit_right - self.rect.width/2:
                            self.move_x_beam(self.x_beam_pos)
                        else:
                            self.x_beam_align = True
                    else:
                        self.move_x(0, WIDTH)
                        self.spawn_bullet(5)
            else:
                self.movement_action = secrets.choice(list(self.action.keys()))
                self.next_action = False

        # Reset Animation when leaving Screen:
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.enter_animation = True
            self.rect.center = [WIDTH/2, -HEIGHT/4]
            self.angle = 0
            self.image, self.rect = self.rotate()


class BossBullet(pygame.sprite.Sprite):

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

        # Movement:
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.angle = angle

        # Sound:
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

        # Group:
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

