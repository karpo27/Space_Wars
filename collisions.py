# Scripts
from enemies import *
from game_objects import *

# Modules
import pygame


# Find all sprites that collide between two groups: group_collide(group1, group2, do_kill1, do_kill2)
def check_collision(group_1, group_2, do_kill_1, do_kill_2):
    pass

# Check Collisions Player Bullets vs Enemies
def check_collision_1(player_bullet, enemy):
    collision = pygame.sprite.groupcollide(player_bullet, enemy, True, False)
    for i, j in collision.items():
        j[0].get_hit()


# Check Collisions Enemy Bullet vs Player
def check_collision_2(enemy_bullet, player):
    collision = pygame.sprite.groupcollide(enemy_bullet, player, True, False)
    for i, j in collision.items():
        j[0].get_hit()


# Check Collisions Player vs Enemy
def check_collision_3(player, enemy):
    collision = pygame.sprite.groupcollide(player, enemy, False, False)
    for i, j in collision.items():
        j[0].get_hit()


# Check Collisions Enemy vs Player
def check_collision_4(enemy, player):
    collision = pygame.sprite.groupcollide(enemy, player, False, False)
    for i, j in collision.items():
        j[0].get_hit()


# Check Collisions Player Bullet vs Boss
def check_collision_5(player_bullet, boss):
    collision = pygame.sprite.groupcollide(player_bullet, boss, True, False)
    for i, j in collision.items():
        j[0].get_hit()


# Check Collisions Boss Bullet vs Player
def check_collision_6(boss_bullet, player):
    collision = pygame.sprite.groupcollide(boss_bullet, player, True, False)
    for i, j in collision.items():
        j[0].get_hit()
