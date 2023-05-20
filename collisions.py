# Scripts

# Modules:
import pygame


# Find all sprites that collide between two groups: group_collide(group_1, group_2, do_kill_1, do_kill_2)
def check_collision(group_1, group_2, do_kill_1, do_kill_2, col_type):
    collision = pygame.sprite.groupcollide(group_1, group_2, do_kill_1, do_kill_2)
    for sprite_1, sprites_2 in collision.items():
        for sprite_2 in sprites_2:
            sprite_2.get_hit(sprite_1.rect.center, col_type)

