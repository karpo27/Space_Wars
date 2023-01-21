# Scripts
from constants import *
from background import *
from player import *
from enemies import *

# Modules
import pygame
from pygame import mixer
import random
import math

# Initialize Pygame
pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self, image, pos, vel, hp, lives):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel = self.vel_x, self.vel_y = vel
        self.hp = hp
        self.lives = lives
        self.enter_animation = True
        self.y_enter = 5/6 * HEIGHT
        self.Δd = 0.2

        # Bullet
        self.ref_time = 30
        self.fire_rate = 30
        self.reload_speed = 1

        # HP Bar
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

    def update(self):
        # Enter Level Animation
        if self.enter_animation:
            if self.rect.y > self.y_enter:
                self.rect.y -= self.Δd
            else:
                self.enter_animation = False
                self.y_enter = 0
                self.Δd = 0

        # Press Keyboard
        else:
            key = pygame.key.get_pressed()
            # Player Keyboard Diagonal Movement - (UP-LEFT, DOWN-LEFT, UP-RIGHT, DOWN-RIGHT)
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
                if self.fire_rate >= 30:
                    player_bullet = PlayerBullet(
                        [self.rect.centerx, self.rect.top],
                        'Images/Player_Bullet/bullets.png',
                        [0, 0.8 * dt],
                        'Sounds/laser.wav',
                        'Sounds/explosion.wav'
                    )

                    player_bullet_group.add(player_bullet)
                    self.fire_rate = 0
                    player_bullet.sound.play()
                    player_bullet.sound.set_volume(speakers.initial_sound)

        # Reset Variables
        if self.fire_rate < self.ref_time:
            self.fire_rate += self.reload_speed

    def draw_hp_bar(self, hp, hp_animation):
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

        if hp == 3:
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_1, *inner_size_1))
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_2, *inner_size_2))
            pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_3, *inner_size_3))
        elif hp == 2:
            if hp_animation:
                player.hp_ref -= player.Δhp
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_2, *inner_size_2))
                pygame.draw.rect(SCREEN, self.hp_bar_full_color, (*inner_pos_3, player.hp_ref, inner_size_3[1]))
                if self.hp_ref == 0:
                    self.hp_animation = False
                    self.hp_ref = 27.5
            else:
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_2, *inner_size_2))

        elif hp == 1:
            if hp_animation:
                player.hp_ref -= player.Δhp
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_1, *inner_size_1))
                pygame.draw.rect(SCREEN, self.hp_bar_med_color, (*inner_pos_2, player.hp_ref, inner_size_2[1]))
                if self.hp_ref == 0:
                    self.hp_animation = False
                    self.hp_ref = 27.5
            else:
                pygame.draw.rect(SCREEN, self.hp_bar_low_color, (*inner_pos_1, *inner_size_1))

        elif hp == 0:
            if hp_animation:
                player.hp_ref -= player.Δhp
                pygame.draw.rect(SCREEN, self.hp_bar_low_color, (*inner_pos_1, player.hp_ref, inner_size_1[1]))
                if self.hp_ref == 0:
                    self.hp_animation = False
                    self.hp_ref = 27.5


class PlayerBullet(pygame.sprite.Sprite):

    def __init__(self, pos, image, vel, sound, col_sound):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.vel = self.vel_x, self.vel_y = vel
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

    def update(self):
        # Player Bullet Movement
        self.rect.y -= self.vel_y

        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    # Define time delay between enemies to spawn
    time_to_spawn = random.randint(2000, 5000)
    spawn_enemy = pygame.USEREVENT + 0
    pygame.time.set_timer(spawn_enemy, time_to_spawn)

    def __init__(self, cat, image, vel, hp, fire_rate):
        super().__init__()
        self.cat = cat
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = [random.randint(0, 3/4 * WIDTH), -80]
        self.vel = self.vel_x, self.vel_y = vel
        self.hp = hp

        # Bullet
        self.ref_time = fire_rate
        self.fire_rate = fire_rate
        self.reload_speed = 1

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        if self.rect.left <= -0.1 * WIDTH:
            self.rect.x += self.vel_x
        if self.rect.right >= 1.1 * WIDTH:
            self.rect.x -= self.vel_y

        if self.rect.top > HEIGHT:
            self.kill()

        # Enemy Bullet
        if self.rect.top > 0:
            # Create Enemy Bullet Object
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
        self.image = pygame.image.load(image)
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


class Speakers:
    def __init__(self):
        self.on_image = pygame.image.load('Images/Speakers/speakers_on_img.png')
        self.off_image = pygame.image.load('Images/Speakers/speakers_off_img.png')
        self.position = self.x, self.y = (13/14 * WIDTH, 1/75 * HEIGHT)
        self.on_rect = self.on_image.get_rect(x=self.x, y=self.y)
        self.off_rect = self.off_image.get_rect(x=self.x, y=self.y)
        self.state = "off"      # This means game will begin with Speakers-Off as default
        self.initial_sound = 0.0

    def action(self, x, y, state):
        if state == "off":
            SCREEN.blit(self.off_image, (x, y))
            mixer.music.set_volume(0.0)
            #player_bullet.sound.set_volume(self.initial_sound)
            #player_bullet.col_sound.set_volume(self.initial_sound)
            #e_bullet_F.col_sound.set_volume(self.initial_sound)
        elif state == "on":
            SCREEN.blit(self.on_image, (x, y))
            mixer.music.set_volume(0.08)
            #player_bullet.sound.set_volume(0.08)
            #player_bullet.col_sound.set_volume(0.08)
            #e_bullet_F.col_sound.set_volume(0.08)


class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font('freesansbold.ttf', 32)
        self.position = self.x, self.y = (10, 10)

    def show(self, x, y):
        score_screen = self.font.render("Score: " + str(self.value), True, (255, 255, 255))
        SCREEN.blit(score_screen, (x, y))


class Explosion(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.sprites = []
        for i in range(1, 6):
            images = pygame.image.load(f'Images/Explosion/explosion_{i}.png')
            self.sprites.append(images)

        self.index = 0
        self.image = self.sprites[self.index]
        self.rect = self.image.get_rect(x=x, y=y)
        self.counter = 0

    def update(self):
        explosion_delay = 8
        # Update Explosion Animation
        self.counter += 1

        if self.counter >= explosion_delay and self.index < len(self.sprites) - 1:
            self.counter = 0
            self.index += 1
            self.image = self.sprites[self.index]

        # If the Animation is Complete, Reset the Index
        if self.index >= len(self.sprites) - 1 and self.counter >= explosion_delay:
            self.kill()


# Initialize Classes:
# Player
player = Player(*player_atr)

speakers = Speakers()
score = Score()
explosion_group = pygame.sprite.Group()
background = Background()

# Create Sprites Group:
all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()
enemies_bullet_group = pygame.sprite.Group()

# Add Some Sprites to group
player_group.add(player)





if __name__ == '__main__':
    pass
