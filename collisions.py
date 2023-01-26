# Scripts


# Modules
import pygame


# Find all sprites that collide between two groups: group_collide(group1, group2, do_kill1, do_kill2)
def check_collision(group_1, group_2, do_kill_1, do_kill_2):
    collision = pygame.sprite.groupcollide(group_1, group_2, do_kill_1, do_kill_2)
    for i, j in collision.items():
        j[0].get_hit()

