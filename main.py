# Scripts
import run_logic
from constants import *


# Modules
import pygame
from pygame import mixer

# Initialize Pygame
pygame.init()


class MainMenu:
    scroll = 0
    angle = 0
    Δy_init = 30
    base_color = (193, 225, 193)    # Pastel Green
    hover_color = (255, 255, 255)   # White
    Δfont_size = 4
    font_size_item = 48
    # Variable Text Parameters: (Text Color, Font Size)
    var_text_param = [
        (base_color, font_size_item),
        (base_color, font_size_item),
        (base_color, font_size_item),
        (base_color, font_size_item)
    ]

    def __init__(self):
        # Title and Icon
        pygame.display.set_caption("Main Menu")
        icon = pygame.image.load('Images/Screen/icon.png')
        pygame.display.set_icon(icon)

        # Background
        self.space_bg = pygame.image.load('Images/Main_Menu/main_menu_img.png')
        self.bg_height = self.space_bg.get_height()

        # Player Icon
        self.player_img = pygame.image.load('Images/Player/player_img.png')
        self.Δx = 40
        self.Δy = 30

        # Text
        self.font_size_title = 94
        self.title_font = pygame.font.Font('freesansbold.ttf', self.font_size_title)
        self.separation = 70

    def show(self):
        # Background Image
        SCREEN.blit(self.space_bg, (0, -self.bg_height + MainMenu.scroll))     # Position 2
        SCREEN.blit(self.space_bg, (0, MainMenu.scroll))     # Position 1

        # Scroll Movement Speed
        MainMenu.scroll += 0.45

        # Reset Scroll
        if MainMenu.scroll >= self.bg_height:
            MainMenu.scroll = 0

        # Main Menu Text
        mm_text = self.title_font.render("GAME PROJECT", True, (255, 255, 255))
        mm_text_rect = mm_text.get_rect()
        mm_text_position = (WIDTH/2 - mm_text_rect.width/2, 1/3 * HEIGHT - mm_text_rect.height/2)
        SCREEN.blit(mm_text, mm_text_position)

        # Play Button Text
        play_item_font = pygame.font.Font('freesansbold.ttf', MainMenu.var_text_param[0][1])
        play_text = play_item_font.render("PLAY", True, MainMenu.var_text_param[0][0])
        # For not moving while change font size
        fixed_text = pygame.font.Font('freesansbold.ttf', MainMenu.font_size_item)
        fixed_text_width, fixed_text_height = fixed_text.size("PLAY")
        play_text_position = (WIDTH/2 - fixed_text_width/2, 3/5 * HEIGHT - fixed_text_height/2)
        SCREEN.blit(play_text, play_text_position)

        # Load Button Text
        load_item_font = pygame.font.Font('freesansbold.ttf', MainMenu.var_text_param[1][1])
        load_text = load_item_font.render("LOAD", True, MainMenu.var_text_param[1][0])
        load_text_position = play_text_position[0], play_text_position[1] + self.separation
        SCREEN.blit(load_text, load_text_position)

        # Options Button Text
        opt_item_font = pygame.font.Font('freesansbold.ttf', MainMenu.var_text_param[2][1])
        opt_text = opt_item_font.render("OPTIONS", True, MainMenu.var_text_param[2][0])
        opt_text_position = play_text_position[0], play_text_position[1] + 2 * self.separation
        SCREEN.blit(opt_text, opt_text_position)

        # Quit Button Text
        quit_item_font = pygame.font.Font('freesansbold.ttf', MainMenu.var_text_param[3][1])
        quit_text = quit_item_font.render("QUIT", True, MainMenu.var_text_param[3][0])
        quit_text_position = play_text_position[0], play_text_position[1] + 3 * self.separation
        SCREEN.blit(quit_text, quit_text_position)

        # Player Icon
        rot_player_img = pygame.transform.rotate(self.player_img, self.angle)
        rot_player_img_rect = rot_player_img.get_rect()
        rot_player_img_position = (
            play_text_position[0] - self.Δx - rot_player_img_rect.width/2,
            play_text_position[1] + self.Δy - rot_player_img_rect.height/2
        )
        SCREEN.blit(rot_player_img, rot_player_img_position)
        pygame.display.flip()
        MainMenu.angle += 2.2

    def show_play(self):
        run = True
        while run:
            # Set screen FPS
            clock.tick(FPS)

            SCREEN.fill("white")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()

    def show_options(self):
        run = True
        while run:
            # Set screen FPS
            clock.tick(FPS)

            SCREEN.fill("white")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False

            pygame.display.update()


# Initialize Classes:
main_menu = MainMenu()

# Game Loop
run = True
while run:
    # Set screen FPS
    clock.tick(FPS)

    # Run Main Menu
    main_menu.show()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        # Press Keyboard
        if event.type == pygame.KEYDOWN:
            # Main Menu Selection Movement
            if event.key == pygame.K_DOWN:
                main_menu.Δy += main_menu.separation
            elif event.key == pygame.K_UP:
                main_menu.Δy -= main_menu.separation

            if event.key == pygame.K_RETURN:
                if main_menu.Δy == main_menu.Δy_init:   # Position: Play
                    run_logic.run_level_1()
                elif main_menu.Δy == main_menu.Δy_init + main_menu.separation:  # Position: Load
                    pass
                elif main_menu.Δy == main_menu.Δy_init + 2 * main_menu.separation:  # Position: Options
                    main_menu.show_options()
                elif main_menu.Δy == main_menu.Δy_init + 3 * main_menu.separation:  # Position: Quit
                    run = False

    # Player Icon Movement Boundaries
    if main_menu.Δy > 4 * main_menu.separation:
        main_menu.Δy = main_menu.Δy_init

    if main_menu.Δy < main_menu.Δy_init:
        main_menu.Δy = main_menu.Δy_init + 3 * main_menu.separation

    # Change text color when selected
    if main_menu.Δy == main_menu.Δy_init:
        MainMenu.var_text_param = [
            (MainMenu.hover_color, MainMenu.font_size_item + MainMenu.Δfont_size),
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.base_color, MainMenu.font_size_item)
        ]
    if main_menu.Δy == main_menu.Δy_init + main_menu.separation:
        MainMenu.var_text_param = [
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.hover_color, MainMenu.font_size_item + MainMenu.Δfont_size),
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.base_color, MainMenu.font_size_item)
        ]
    if main_menu.Δy == main_menu.Δy_init + 2 * main_menu.separation:
        MainMenu.var_text_param = [
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.hover_color, MainMenu.font_size_item + MainMenu.Δfont_size),
            (MainMenu.base_color, MainMenu.font_size_item)
        ]
    if main_menu.Δy == main_menu.Δy_init + 3 * main_menu.separation:
        MainMenu.var_text_param = [
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.base_color, MainMenu.font_size_item),
            (MainMenu.hover_color, MainMenu.font_size_item + MainMenu.Δfont_size)
        ]

    # Apply Changes
    pygame.display.update()
