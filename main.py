# Scripts:
from constants import *
from main_menu import *
from options import *
from background_creator import *

# Modules:
import pygame
from pygame import mixer

# Initialize Pygame:
pygame.init()


def run_main_menu():
    # Game Loop:
    run = True
    while run:
        # Set screen FPS:
        clock.tick(FPS)

        # Draw Scrolling Background
        background_main_menu.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update Sprites Group:
        if main_menu.indicator == "menu":
            main_menu_group.update()
        elif main_menu.indicator == "options":
            run_options()

        # Apply Changes:
        pygame.display.update()


def run_options():
    # Game Loop:
    run = True
    while run:
        # Set screen FPS:
        clock.tick(FPS)

        # Draw Scrolling Background
        background_main_menu.show()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # Update Sprites Group:
        options_group.update()

        # Apply Changes:
        pygame.display.update()


# Run Main Menu:
run_main_menu()

