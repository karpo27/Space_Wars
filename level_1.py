# Scripts
from game_objects import *


# Modules
import pygame
from pygame import mixer
import math

# Initialize Pygame
pygame.init()


def run_level_1():
    # Game Loop
    run = True
    while run:
        # Define Number of Enemies to spawn in Level 1: 10
        enemies_lvl_1 = [enemy_E, enemy_D]

        # Set screen FPS
        clock.tick(FPS)

        # Draw Scrolling Background
        background.show()

        explosion_group.draw(SCREEN)
        explosion_group.update()

        # Enter Level Animation + Show Player Image Screen
        if player.pos[1] < Player.y_enter - Player.Δd:
            pygame.event.set_blocked([pygame.KEYDOWN, pygame.KEYUP])
            player.show_image(player.pos[0], Player.y_enter - Player.Δd)
            Player.Δd += 1.9
        else:
            Player.y_enter = 0
            Player.Δd = 0
            pygame.event.set_allowed([pygame.KEYDOWN, pygame.KEYUP])
            player.show_image(player.pos[0], player.pos[1])

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

            # Press Keyboard
            if event.type == pygame.KEYDOWN:
                # Player Keyboard Movement - (LEFT, RIGHT, UP, DOWN)
                if event.key == pygame.K_LEFT:
                    player.Δpos[0] = -player.init_d
                if event.key == pygame.K_RIGHT:
                    player.Δpos[0] = player.init_d
                if event.key == pygame.K_UP:
                    player.Δpos[1] = -player.init_d
                if event.key == pygame.K_DOWN:
                    player.Δpos[1] = player.init_d
                # Player Keyboard Diagonal Movement - (UP-LEFT, DOWN-LEFT, UP-RIGHT, DOWN-RIGHT)
                if player.Δpos[0] < 0:
                    if player.Δpos[1] < 0:
                        player.Δpos[0] = - math.sqrt((player.init_d ** 2) / 2)
                        player.Δpos[1] = - math.sqrt((player.init_d ** 2) / 2)
                    if player.Δpos[1] > 0:
                        player.Δpos[0] = - math.sqrt((player.init_d ** 2) / 2)
                        player.Δpos[1] = math.sqrt((player.init_d ** 2) / 2)
                if player.Δpos[0] > 0:
                    if player.Δpos[1] < 0:
                        player.Δpos[0] = math.sqrt((player.init_d ** 2) / 2)
                        player.Δpos[1] = - math.sqrt((player.init_d ** 2) / 2)
                    if player.Δpos[1] > 0:
                        player.Δpos[0] = math.sqrt((player.init_d ** 2) / 2)
                        player.Δpos[1] = math.sqrt((player.init_d ** 2) / 2)

                # Player Bullet Keyboard
                if event.key == pygame.K_SPACE:
                    if p_bullet.Δt_p_bullet >= PlayerBullet.p_bullet_ref:
                        p_bullet.Δt_p_bullet = 0
                        p_bullet.sound.play()
                        p_bullet.sound.set_volume(speakers.initial_sound)
                        p_bullet.generate_bullet()

            # Release Keyboard
            if event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.Δpos[0] = 0
                elif event.key in (pygame.K_UP, pygame.K_DOWN):
                    player.Δpos[1] = 0

            # Press Mouse
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse_pos = pygame.mouse.get_pos()
                if speakers.off_rect.collidepoint(mouse_pos):
                    if speakers.state == "off":
                        speakers.state = "on"
                    else:
                        speakers.state = "off"

            # Spawn Enemies According to Level
            n_enemies = len(enemies_lvl_1)
            if len(Enemy.enemy_list) < n_enemies:
                if event.type == Enemy.spawn_enemy:
                    x = enemies_lvl_1[len(Enemy.enemy_list)]
                    # Generate Enemies
                    Enemy.enemy_list.append(x)      # Fix this later for infinite enemies as last enemy_list
                    Enemy.image.append(x.image)
                    Enemy.pos.append([random.randint(-0.1 * WIDTH, 1.1 * WIDTH - C_64), random.randint(-80, 0 - C_64)])
                    Enemy.Δpos.append([x.Δpos[0], x.Δpos[1]])
                    Enemy.hp.append(x.hp)
                    Enemy.Δt_bullet.append(0)

        # Player Movement Boundaries
        player.pos[0] += player.Δpos[0]
        player.pos[1] += player.Δpos[1]

        if player.pos[0] <= 0:
            player.pos[0] = 0
        if player.pos[1] <= 0:
            player.pos[1] = 0
        if player.pos[0] >= WIDTH - player.l_image:
            player.pos[0] = WIDTH - player.l_image
        if player.pos[1] >= HEIGHT - player.l_image:
            player.pos[1] = HEIGHT - player.l_image

        # Player Bullet Movement
        if p_bullet.Δt_p_bullet < PlayerBullet.p_bullet_ref:
            p_bullet.Δt_p_bullet += 1

        for bullet_pos in PlayerBullet.pos[:]:
            bullet_pos[1] -= p_bullet.Δpos[1]

            if bullet_pos[1] + p_bullet.l_image < 0:
                PlayerBullet.image.pop()
                PlayerBullet.pos.remove(bullet_pos)

        # Show Player Bullet on Screen
        for i in range(len(PlayerBullet.pos[:])):
            SCREEN.blit(PlayerBullet.image[i], (PlayerBullet.pos[i], PlayerBullet.pos[i]))

        # Enemies Movement
        for i in range(len(Enemy.enemy_list)):
            # Call Movement Function for Each Enemy
            Enemy.enemy_list[i].movement(Enemy.enemy_list[i], i)

            # Y Axis Movement Boundary for All Enemies
            if Enemy.pos[i][1] - Enemy.image[i].get_rect().width > HEIGHT:
                Enemy.enemy_list.pop(i)
                Enemy.image.pop(i)
                Enemy.pos.pop(i)
                Enemy.Δpos.pop(i)
                Enemy.hp.pop(i)
                Enemy.Δt_bullet.pop(i)
                break

            # After Enemies Appear Generate Enemy Bullet every enemy_X.Δt_bullet cycles
            if len(Enemy.enemy_list) > 0:
                Enemy.Δt_bullet[i] += 1
                if Enemy.pos[i][1] >= 0 and Enemy.Δt_bullet[i] >= Enemy.enemy_list[i].Δt_bullet:
                    Enemy.Δt_bullet[i] = 0
                    e_bullet_E.generate_bullet(i)

            # Collision Detection for Player with Enemy
            col_player_with_enemy = pygame.Rect.colliderect(
                player.image.get_rect(x=player.pos[0], y=player.pos[1]),
                Enemy.image[i].get_rect(x=Enemy.pos[i][0], y=Enemy.pos[i][1])
            )

            '''
            if col_player_with_enemy:
                # The collision will affect only if this:
                if Enemy.pos[i][1] + Enemy.image[i].get_rect().width >= 0:
                    player.hp -= 1
                    player.hp_animation = True
                    score.value += 1'''

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

            # Show Enemies on Screen
            SCREEN.blit(Enemy.image[i], (Enemy.pos[i][0], Enemy.pos[i][1]))

        # Enemy Bullet Movement (fix later according to enemy)
        for bullet_pos in EnemyBullet.pos:
            bullet_pos[1] += e_bullet_F.Δpos[1]

            if bullet_pos[1] > HEIGHT:
                EnemyBullet.image.pop()
                EnemyBullet.pos.remove(bullet_pos)
                EnemyBullet.Δpos.pop()

        # Collision Detection for Enemy Bullet with Player
        for i in range(len(EnemyBullet.image)):
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

        # Show Enemies Bullets on Screen
        for i in range(len(EnemyBullet.pos)):
            SCREEN.blit(EnemyBullet.image[i], EnemyBullet.pos[i])

        # Call other Functions
        player.draw_hp_bar(player.hp, player.hp_animation)
        score.show(score.x, score.y)
        speakers.action(speakers.x, speakers.y, speakers.state)

        # Apply changes
        pygame.display.update()


run_level_1()
