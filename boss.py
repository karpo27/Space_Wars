# Scripts
from constants import *
from game_effects import Explosion, Particle

# Modules
import pygame
from pygame import mixer
import random
import secrets


class Boss(pygame.sprite.Sprite):

    def __init__(self, img_path, scale, movement, vel, hp, bullet, bullet_pattern_counter, fire_cycles, explo_scale, part_range, bullet_group, effects_group):
        super().__init__()
        self.image = pygame.image.load(img_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (self.image.get_width() * scale[0], self.image.get_height() * scale[1]))
        self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.center = [WIDTH/2, -1/4 * HEIGHT]

        # Initial Movement Animation:
        self.enter_animation = True
        self.y_enter = 1/25 * HEIGHT
        self.vel_enter_y = 1

        # Movement:
        self.movement = movement
        self.vel = self.vel_x, self.vel_y = vel
        self.counter = 0
        self.angle = 0
        self.movement_action = None
        self.next_action = True

        # HP:
        self.hp = hp

        # Bullet:
        self.bullet_group = bullet_group
        self.bullet = bullet
        self.bullet_index = 0
        self.bullet_pattern_counter = bullet_pattern_counter
        self.ref_time = bullet_pattern_counter
        self.fire_cycles = fire_cycles
        self.fire_cycles_counter = 0
        self.bullet_type_qty = 1
        self.bullet_type_counter = 0
        #self.bullet_pos = bullet_pos
        self.reload_speed = 1

        # Explosion:
        self.effects_group = effects_group
        self.explosion_scale = explo_scale
        self.part_min, self.part_max = part_range

    def move_hor(self, direction):
        if self.rect.x == 1/20 * WIDTH:
            '''
            if self.rect.x == WIDTH/2:
                self.next_action = True
                self.vel_x = 0
            else:
                self.vel_x = -self.vel_x
                self.rect.x += self.vel_x * direction'''
        else:
            self.rect.x += self.vel_x * direction

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
        if self.bullet_pattern_counter >= self.ref_time:
            if self.fire_cycles_counter >= self.fire_cycles[self.bullet_index][0]:
                if self.fire_cycles[self.bullet_index][1] >= self.bullet_type_qty:
                    if self.bullet_type_counter >= 20:
                        for bullet_type in self.bullet[self.bullet_index]:
                            BossBullet(self.rect.center, *BOSSES_BULLETS[f'b_bullet_{bullet_type}'], self.bullet_group)
                        self.bullet_type_counter = 0
                        self.bullet_type_qty += 1

                    else:
                        self.bullet_type_counter += 1
                else:
                    self.bullet_type_qty = 1
                    self.bullet_index += 1
            else:
                self.fire_cycles_counter += self.reload_speed
        # Reset Variables
        else:
            self.bullet_pattern_counter += self.reload_speed

        if self.bullet_index == len(self.fire_cycles):
            self.bullet_index = 0
            self.fire_cycles_counter = 0
            self.bullet_pattern_counter = 0

    def get_hit(self):
        self.hp -= 1

        if self.hp <= 0:
            self.destroy()

    def destroy(self):
        self.kill()
        self.effects_group.add(Explosion(self.rect.x, self.rect.y, self.explosion_scale))
        for num_particles in range(random.randrange(self.part_min, self.part_max)):
            Particle(self.rect.center, self.effects_group)

    def update(self):
        # Enter Level Animation
        if self.enter_animation:
            if self.rect.y <= self.y_enter:
                self.rect.y += self.vel_enter_y
            else:
                self.enter_animation = False

        else:
            if self.next_action:
                self.movement_action = secrets.choice(self.movement)
            if self.movement_action == 1:
                print(self.movement_action)
                self.next_action = False
                self.move_hor(1)
            elif self.movement_action == 2:
                self.next_action = False
                self.move_hor(-1)
            elif self.movement_action == 3:
                self.image, self.rect = self.move_hor_vert_sin()

            # Create Boss Bullet Object (fix later side of the bullet):
            self.spawn_bullet()

        # Reset Animation when leaving Screen
        if self.rect.top > HEIGHT or self.rect.left > WIDTH or self.rect.right < 0:
            self.enter_animation = True
            self.rect.center = [WIDTH/2, -1/4 * HEIGHT]


class BossBullet(pygame.sprite.Sprite):

    def __init__(self, pos, image, movement, vel, angle, sound, col_sound, group):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.image_copy = self.image
        self.rect = self.image.get_rect()
        self.rect.center = pos

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

