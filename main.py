# Scripts


# Modules
import pygame

# Initialize Pygame
pygame.init()

# Create the screen
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)

# Title and Icon
pygame.display.set_caption("Game_Project")
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

# Player
player_img = pygame.image.load('player_img.png')
player_x = 370
player_y = 480


def player():
    screen.blit(player_img, (player_x, player_y))


# Game Loop
running = True
while running:
    # Screen - RGB
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    player()

    pygame.display.update()



pygame.quit()

if __name__ == '__main__':
    pass


