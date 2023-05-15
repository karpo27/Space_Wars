# Scripts
from constants import *
from game_effects import *

# Modules
import pygame
from pygame import mixer
import math


class Player(pygame.sprite.Sprite):
    def __init__(self, image, pos, vel, hp, lives, explosion_scale):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel = self.vel_x, self.vel_y = vel

        # State:
        self.state = "alive"
        self.hp = hp
        self.lives = lives

        # Initial Movement Animation:
        self.enter_animation = True
        self.y_enter = 5/6 * HEIGHT
        self.vel_enter_y = 0.2

        # Bullet:
        self.ref_time = 30
        self.fire_rate = 30
        self.reload_speed = 1

        # Explosion:
        self.explosion_scale = explosion_scale

        # HP Bar:
        self.hp_bar_pos = (1/43 * WIDTH, 16/17 * HEIGHT)
        self.hp_bar_size = (108, 30)
        self.hp_bar_border_color = (255, 255, 255)    # White
        self.hp_bar_low_color = (255, 49, 49)  # Neon Red
        self.hp_bar_med_color = (255, 165, 0)  # Orange
        self.hp_bar_full_color = (15, 255, 80)     # Neon Green
        self.line_width = 2
        self.border_radius = 4
        self.hp_animation = False
        self.hp_ref = 27.5
        self.Δhp = 0.5

        # Rotation:
        self.angle = 0

    def get_hit(self):
        self.hp_animation = True
        self.hp -= 1

        if self.hp <= 0:
            self.destroy()

    def destroy(self):

        self.kill()
        explosion = Explosion(self.rect.x, self.rect.y, self.explosion_scale)
        explosion_group.add(explosion)
        if self.lives > 0:
            self.lives -= 1
            self.hp = 3
        else:
            self.state = "dead"

    def draw_hp_bar(self):
        x_1, y_1 = (self.hp_bar_pos[0] + 1/3 * self.hp_bar_size[0], self.hp_bar_pos[1])
        x_2, y_2 = (x_1, y_1 + self.hp_bar_size[1] - 1)

        x_3, y_3 = (self.hp_bar_pos[0] + 2/3 * self.hp_bar_size[0], y_1)
        x_4, y_4 = (x_3, y_2)

        Δinner_pos = 4
        Δinner_size = 8.5
        inner_pos_1 = (self.hp_bar_pos[0] + 5, self.hp_bar_pos[1] + Δinner_pos)
        inner_pos_2 = (self.hp_bar_pos[0] + self.hp_bar_pos[0] + 1/6 * self.hp_bar_size[0], self.hp_bar_pos[1] + Δinner_pos)
        inner_pos_3 = (self.hp_bar_pos[0] + self.hp_bar_pos[0] + 1/2 * self.hp_bar_size[0], self.hp_bar_pos[1] + Δinner_pos)
        inner_size_1 = (1/3 * self.hp_bar_size[0] - Δinner_size + 1, self.hp_bar_size[1] - Δinner_size)
        inner_size_2 = (1/3 * self.hp_bar_size[0] - Δinner_size + 1, self.hp_bar_size[1] - Δinner_size)
        inner_size_3 = (1/3 * self.hp_bar_size[0] - Δinner_size, self.hp_bar_size[1] - Δinner_size)

        pygame.draw.line(SCREEN, self.hp_bar_border_color, (x_1, y_1), (x_2, y_2), self.line_width)
        pygame.draw.line(SCREEN, self.hp_bar_border_color, (x_3, y_3), (x_4, y_4), self.line_width)
        pygame.draw.rect(SCREEN, self.hp_bar_border_color, (*self.hp_bar_pos, *self.hp_bar_size), self.line_width, 4)

        if self.hp == 3:
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_1, *inner_size_1))
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_2, *inner_size_2))
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_3, *inner_size_3))
        elif self.hp == 2:
            if self.hp_animation:
                self.hp_ref -= self.Δhp
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_2, *inner_size_2))
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_3, self.hp_ref, inner_size_3[1]))
                if self.hp_ref == 0:
                    self.hp_animation = False
                    self.hp_ref = 27.5
            else:
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_2, *inner_size_2))

        elif self.hp == 1:
            if self.hp_animation:
                self.hp_ref -= self.Δhp
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_2, self.hp_ref, inner_size_2[1]))
                if self.hp_ref == 0:
                    self.hp_animation = False
                    self.hp_ref = 27.5
            else:
                pygame.draw.rect(SCREEN, self.hp_bar_low_color, (*inner_pos_1, *inner_size_1))

        elif self.hp == 0:
            if self.hp_animation:
                self.hp_ref -= self.Δhp
                pygame.draw.rect(SCREEN, self.hp_bar_low_color, (*inner_pos_1, self.hp_ref, inner_size_1[1]))
                if self.hp_ref == 0:
                    self.hp_animation = False
                    self.hp_ref = 27.5

    def update(self):
        # Enter Level Animation:
        if self.enter_animation:
            if self.rect.y > self.y_enter:
                self.rect.y -= self.vel_enter_y
            else:
                self.enter_animation = False

        # Press Keyboard
        else:
            key = pygame.key.get_pressed()
            # Player Keyboard Diagonal Movement - (UP-LEFT, DOWN-LEFT, UP-RIGHT, DOWN-RIGHT):
            if key[pygame.K_LEFT] and key[pygame.K_UP] and self.rect.left > 0 and self.rect.top > 0:
                self.rect.x -= math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y -= math.sqrt((self.vel_y ** 2) / 2)
            elif key[pygame.K_LEFT] and key[pygame.K_DOWN] and self.rect.left > 0 and self.rect.bottom < HEIGHT:
                self.rect.x -= math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y += math.sqrt((self.vel_y ** 2) / 2)
            elif key[pygame.K_RIGHT] and key[pygame.K_UP] and self.rect.right < WIDTH and self.rect.top > 0:
                self.rect.x += math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y -= math.sqrt((self.vel_y ** 2) / 2)
            elif key[pygame.K_RIGHT] and key[pygame.K_DOWN] and self.rect.right < WIDTH and self.rect.bottom < HEIGHT:
                self.rect.x += math.sqrt((self.vel_x ** 2) / 2)
                self.rect.y += math.sqrt((self.vel_y ** 2) / 2)

            # Player Keyboard Movement - (LEFT, RIGHT, UP, DOWN)
            elif key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.vel_x
            elif key[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.vel_x
            elif key[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.vel_y
            elif key[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.vel_y

            # Player Bullet Keyboard
            if key[pygame.K_SPACE]:
                # Create Player Bullet Object
                if self.fire_rate >= self.ref_time:
                    PlayerBullet(self.rect.center, *PLAYER_BULLETS['player_bullet_d'])
                    self.fire_rate = 0

        # Reset Variables
        if self.fire_rate < self.ref_time:
            self.fire_rate += self.reload_speed

        # Call HP Bar
        self.draw_hp_bar()


class PlayerBullet(pygame.sprite.Sprite):
    def __init__(self, pos, image, vel, sound, col_sound):
        super().__init__()
        self.image = pygame.image.load(image).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = pos

        # Movement:
        self.vel = self.vel_x, self.vel_y = vel

        # Sound:
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

        # Groups:
        PLAYER_BULLETS_GROUP.add(self)

    def update(self):
        # Player Bullet Movement:
        self.rect.y -= self.vel_y

        if self.rect.bottom < 0:
            self.kill()



