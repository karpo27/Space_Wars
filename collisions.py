# Scripts

# Modules
import pygame


# Find all sprites that collide between two groups: group_collide(group_1, group_2, do_kill_1, do_kill_2)
def check_collision(group_1, group_2, do_kill_1, do_kill_2):
    collision = pygame.sprite.groupcollide(group_1, group_2, do_kill_1, do_kill_2)
    for group1, group2 in collision.items():
        group2[0].get_hit()

