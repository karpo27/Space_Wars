# Scripts
from game_objects import *
from enemies import *


# Modules
import pygame
from pygame import mixer

# Initialize Pygame
pygame.init()


def run_level_1():
    # Game Loop
    run = True
    while run:
        # Set screen FPS
        clock.tick(FPS)

        # Define Number of Enemies to spawn in Level 1: 10
        enemies_lvl_1 = [enemies['enemy_f'], enemies['enemy_e'], enemies['enemy_f']]

        # Draw Scrolling Background
        background.show()

        # Go to Game Over / Continue Screen
        if player.lives < 1:
            pass

        # Consume Life to Keep Playing
        if player.hp == 0:
            player.lives -= 1
            pass

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            # Press Mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse_pos = pygame.mouse.get_pos()
                if speakers.off_rect.collidepoint(mouse_pos):
                    if speakers.state == "off":
                        speakers.state = "on"
                    else:
                        speakers.state = "off"

            # Spawn Enemies According to Level
            if len(enemies_group) < len(enemies_lvl_1):
                if event.type == Enemy.spawn_enemy:
                    k = enemies_lvl_1[len(enemies_group)]
                    # Generate Enemies
                    new_enemy = Enemy(*k)
                    enemies_group.add(new_enemy)

        '''
        # Enemies:
        for i in range(len(Enemy.enemy_list)):
            # After Enemies Appear Generate Enemy Bullet every enemy_X.Δt_bullet cycles
            if len(Enemy.enemy_list) > 0:
                Enemy.Δt_bullet[i] += 1
                if Enemy.pos[i][1] >= 0 and Enemy.Δt_bullet[i] >= Enemy.enemy_list[i][0].Δt_bullet:
                    Enemy.Δt_bullet[i] = 0
                    Enemy.enemy_list[i][1].generate_bullet(i)

            # Collision Detection for Player with Enemy
            col_player_with_enemy = pygame.Rect.colliderect(
                player.image.get_rect(x=player.pos[0], y=player.pos[1]),
                Enemy.image[i].get_rect(x=Enemy.pos[i][0], y=Enemy.pos[i][1])
            )

            
            if col_player_with_enemy:
                # The collision will affect only if this:
                if Enemy.pos[i][1] + Enemy.image[i].get_rect().width >= 0:
                    player.hp -= 1
                    player.hp_animation = True
                    score.value += 1

            # Collision Detection for Player Bullet with Enemy
            for j in range(len(PlayerBullet.image)):
                col_p_bul_with_enemy = pygame.Rect.colliderect(
                    PlayerBullet.image[j].get_rect(x=PlayerBullet.pos[j][0], y=PlayerBullet.pos[j][1]),
                    Enemy.image[i].get_rect(x=Enemy.pos[i][0], y=Enemy.pos[i][1])
                )

                if col_p_bul_with_enemy:
                    # The collision will affect only if this:
                    if Enemy.pos[i][1] + Enemy.image[i].get_rect().width >= 0:
                        PlayerBullet.image.pop()    # fix removal for bullet not last (later)
                        PlayerBullet.pos.pop()
                        Enemy.hp[i] -= 1
                        score.value += 1
                        p_bullet.col_sound.play()

            if Enemy.hp[i] == 0:
                explosion_enemy = Explosion(*Enemy.pos[i])
                explosion_group.add(explosion_enemy)
                Enemy.enemy_list.pop(i)
                Enemy.image.pop(i)
                Enemy.pos.pop(i)
                Enemy.Δpos.pop(i)
                Enemy.hp.pop(i)
                Enemy.Δt_bullet.pop(i)
                break

            # Collision Detection for Enemy Bullet with Player
            col_e_bul_with_player = pygame.Rect.colliderect(
                player.image.get_rect(x=player.pos[0], y=player.pos[1]),
                EnemyBullet.image[i].get_rect(x=EnemyBullet.pos[i][0], y=EnemyBullet.pos[i][1])
            )

            if col_e_bul_with_player:
                # The collision will affect only if this:
                EnemyBullet.image.remove(EnemyBullet.image[i])
                EnemyBullet.pos.remove(EnemyBullet.pos[i])
                EnemyBullet.Δpos.remove(EnemyBullet.Δpos[i])
                player.hp -= 1
                player.hp_animation = True
                score.value += 1
                e_bullet_F.col_sound.play()
                break
                '''

        # Update Sprites
        player.update()

        # Update Sprites Group
        player_bullet_group.update()
        enemies_group.update()
        enemies_bullet_group.update()

        explosion_group.update()

        # Draw Sprite Groups
        enemies_bullet_group.draw(SCREEN)
        enemies_group.draw(SCREEN)

        player_bullet_group.draw(SCREEN)
        player_group.draw(SCREEN)

        explosion_group.draw(SCREEN)

        player.draw_hp_bar(player.hp, player.hp_animation)
        score.show(score.x, score.y)
        speakers.action(speakers.x, speakers.y, speakers.state)

        # Apply changes
        pygame.display.update()


run_level_1()
