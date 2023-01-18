# Scripts
from constants import *

# Enemies - Image Size: 64 x 64 / Bullet Size: 32 x 32
enemies = {
    'enemy_f': [
        'F',
        'Images/Enemies/enemy_F.png',
        [round(0.04 * dt), 1],
        1,
        100
    ],
    'enemy_e': [
        'E',
        'Images/Enemies/enemy_E.png',
        [0, 3],
        1,
        180
    ],
    'enemy_d': [
        'D'
        'Images/Enemies/enemy_D.png',
        [round(0.03 * dt), 1.8],
        1,
        100
    ]
}


'''
e_bullet_F = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_F.png',
    [0, 0.15 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)

e_bullet_E = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_E.png',
    [0, 0.22 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)

e_bullet_D = EnemyBullet(
    'Images/Enemies_Bullet/enemy_bullet_F.png',
    [0, 0.22 * dt],
    'Sounds/laser.wav',
    'Sounds/explosion.wav'
)'''