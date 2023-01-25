# Scripts
from enemies import *
from game_objects import *

# Modules
import pygame


# Find all sprites that collide between two groups: group_collide(group1, group2, do_kill1, do_kill2)

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
