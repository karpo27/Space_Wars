# Scripts


# Modules
import pygame

# Initialize Pygame
pygame.init()

# Create the screen
size = width, height = (800, 800)
screen = pygame.display.set_mode(size)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()



if __name__ == '__main__':
    pass


