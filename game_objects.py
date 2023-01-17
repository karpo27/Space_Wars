# Scripts
from constants import *
from background import *

# Modules
import pygame
from pygame import mixer
import random
import math

# Initialize Pygame
pygame.init()


class Player(pygame.sprite.Sprite):

    def __init__(self, image, pos, Δpos, hp, lives):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.Δpos = Δpos
        self.hp = hp
        self.lives = lives
        self.init_d = 0.3 * dt
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
                self.rect.x -= math.sqrt((self.init_d ** 2) / 2)
                self.rect.y -= math.sqrt((self.init_d ** 2) / 2)
            elif key[pygame.K_LEFT] and key[pygame.K_DOWN] and self.rect.left > 0 and self.rect.bottom < HEIGHT:
                self.rect.x -= math.sqrt((self.init_d ** 2) / 2)
                self.rect.y += math.sqrt((self.init_d ** 2) / 2)
            elif key[pygame.K_RIGHT] and key[pygame.K_UP] and self.rect.right < WIDTH and self.rect.top > 0:
                self.rect.x += math.sqrt((self.init_d ** 2) / 2)
                self.rect.y -= math.sqrt((self.init_d ** 2) / 2)
            elif key[pygame.K_RIGHT] and key[pygame.K_DOWN] and self.rect.right < WIDTH and self.rect.bottom < HEIGHT:
                self.rect.x += math.sqrt((self.init_d ** 2) / 2)
                self.rect.y += math.sqrt((self.init_d ** 2) / 2)

            # Player Keyboard Movement - (LEFT, RIGHT, UP, DOWN)
            elif key[pygame.K_LEFT] and self.rect.left > 0:
                self.rect.x -= self.init_d
            elif key[pygame.K_RIGHT] and self.rect.right < WIDTH:
                self.rect.x += self.init_d
            elif key[pygame.K_UP] and self.rect.top > 0:
                self.rect.y -= self.init_d
            elif key[pygame.K_DOWN] and self.rect.bottom < HEIGHT:
                self.rect.y += self.init_d

            # Player Bullet Keyboard
            if key[pygame.K_SPACE]:
                # Create Player Bullet Object
                if self.fire_rate >= 30:
                    player_bullet = PlayerBullet(
                        'Images/Player_Bullet/bullets.png',
                        [self.rect.centerx, self.rect.top],
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
    image = []
    pos = []
    Δpos = []

    def __init__(self, image, pos, Δpos, sound, col_sound):
        super().__init__()
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.Δpos = Δpos
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

    def update(self):
        # Player Bullet Movement
        self.rect.y -= self.Δpos[1]

        if self.rect.bottom < 0:
            self.kill()


class Enemy(pygame.sprite.Sprite):
    enemy_list = []
    image = []
    pos = []
    Δpos = []
    Δt_bullet = []
    hp = []

    # Define time delay between enemies to spawn: 8.0 sec
    time_to_spawn = 2500
    spawn_enemy = pygame.USEREVENT + 0
    pygame.time.set_timer(spawn_enemy, time_to_spawn)

    def __init__(self, type, image, pos, Δpos, hp, Δt_bullet):
        super().__init__()
        self.type = type
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.center = pos
        self.Δpos = Δpos
        self.hp = hp
        self.Δt_bullet = Δt_bullet

    def update(self, enemy_type):
        if enemy_type == 'F':
            self.rect.x += self.Δpos[0]
            self.rect.y += self.Δpos[1]

            '''
            if Enemy.pos[i][0] <= - 0.2 * WIDTH:
                Enemy.Δpos[i][0] = self.Δpos[0]
            if Enemy.pos[i][0] >= 1.2 * WIDTH - Enemy.image[i].get_rect().width:
                Enemy.Δpos[i][0] = - self.Δpos[0]'''

        '''
        elif enemy_type == enemy_E:
            Enemy.pos[i][1] += Enemy.Δpos[i][1]

        elif enemy_type == enemy_D:
            Enemy.pos[i][0] += Enemy.Δpos[i][0]
            Enemy.pos[i][1] += Enemy.Δpos[i][1]
            if Enemy.pos[i][0] <= - 0.2 * WIDTH:
                Enemy.Δpos[i][0] = self.Δpos[0]
            if Enemy.pos[i][0] >= 1.2 * WIDTH - Enemy.image[i].get_rect().width:
                Enemy.Δpos[i][0] = - self.Δpos[0]'''


class EnemyBullet:
    # Define Bullet Variables
    image = []
    pos = []
    Δpos = []

    def __init__(self, image, Δpos, sound, col_sound):
        self.image = pygame.image.load(image)
        self.l_image = self.image.get_rect().width
        self.Δpos = Δpos
        self.sound = mixer.Sound(sound)
        self.col_sound = mixer.Sound(col_sound)

    def generate_bullet(self, i):
        EnemyBullet.image.append(self.image)
        EnemyBullet.pos.append([Enemy.pos[i][0], Enemy.pos[i][1]])
        EnemyBullet.Δpos.append((self.Δpos[0], self.Δpos[1]))


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
            e_bullet_F.col_sound.set_volume(self.initial_sound)
        elif state == "on":
            SCREEN.blit(self.on_image, (x, y))
            mixer.music.set_volume(0.08)
            #player_bullet.sound.set_volume(0.08)
            #player_bullet.col_sound.set_volume(0.08)
            e_bullet_F.col_sound.set_volume(0.08)


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
player = Player(
    'Images/Player/player_img.png',      # Image Size: 64 x 64
    [WIDTH/2 - C_64/2, 19/18 * HEIGHT],
    [0, 0],
    3,
    3
)

# Enemies
enemy_F = Enemy(
    'F',
    'Images/Enemies/enemy_F.png',      # Image Size: 64 x 64
    [random.randint(0, WIDTH - C_64), random.randint(-100, 0 - C_64)],
    [round(0.04 * dt), 1],
    1,
    100
)


e_bullet_F = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_F.png',   # Image Size: 32 x 32
    [0, 0.15 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)

enemy_E = Enemy(
    'E',
    'Images/Enemies/enemy_E.png',      # Image Size: 64 x 64
    [random.randint(0, WIDTH - C_64), random.randint(-100, 0 - C_64)],
    [0, 1.6],
    1,
    180
)


e_bullet_E = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_E.png',   # Image Size: 32 x 32
    [0, 0.22 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)


enemy_D = Enemy(
    'D',
    'Images/Enemies/enemy_D.png',      # Image Size: 64 x 64
    [random.randint(0, WIDTH - C_64), random.randint(-100, 0 - C_64)],
    [0.04 * dt, 1.8],
    1,
    100
)


e_bullet_D = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_F.png',   # Image Size: 32 x 32
    [0, 0.22 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)


speakers = Speakers()
score = Score()
explosion_group = pygame.sprite.Group()
background = Background()

# Create Sprites Group:
all_sprites = pygame.sprite.Group()

player_group = pygame.sprite.Group()
player_bullet_group = pygame.sprite.Group()
enemies_group = pygame.sprite.Group()

# Add Some Sprites to group
player_group.add(player)



if __name__ == '__main__':
    pass
