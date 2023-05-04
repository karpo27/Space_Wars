# Scripts:
from constants import *
from main_menu import *
from options import *
from game_objects import *
from background_creator import *

# Modules:
import pygame

# Initialize Pygame:
pygame.init()


def run_main_menu():
    # Game Loop:
    run = True
    while run:
        # Set screen FPS:
        clock.tick(FPS)

        # Draw Scrolling Background:
        background_main_menu.update()

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

        # Update Sprites Group:
        if main_menu.indicator == "main menu":
            main_menu_group.add(main_menu)
            main_menu_group.update()
        elif main_menu.indicator == "play":
            pass
        elif main_menu.indicator == "options":
            main_menu_group.add(options)
            main_menu_group.update()

        # Extras
        speakers.action(speakers.x, speakers.y, speakers.state)

        # Apply Changes:
        pygame.display.update()


# Run Main Menu:
run_main_menu()

