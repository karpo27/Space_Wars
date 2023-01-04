# Scripts
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
    base_color = (236, 255, 220)
    hover_color = (255, 255, 255)
    text_color = [
        base_color,
        base_color,
        base_color,
        base_color
    ]

    def __init__(self):
        # Background
        self.space_bg = pygame.image.load('Images/Main_Menu/main_menu_img.png')
        self.bg_height = self.space_bg.get_height()

        # Player Icon
        self.player_img = pygame.image.load('Images/Player/player_img.png')
        self.Δx = 40
        self.Δy = 30

        # Text
        self.font_size_title = 94
        self.font_size_item = 64
        self.title_font = pygame.font.Font('freesansbold.ttf', self.font_size_title)
        self.item_font = pygame.font.Font('freesansbold.ttf', self.font_size_item)
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
        play_text = self.item_font.render("PLAY", True, MainMenu.text_color[0])
        play_text_rect = play_text.get_rect()
        play_text_position = (WIDTH/2 - play_text_rect.width/2, 3/5 * HEIGHT - play_text_rect. height/2)
        SCREEN.blit(play_text, play_text_position)

        # Load Button Text
        load_text = self.item_font.render("LOAD", True, MainMenu.text_color[1])
        load_text_rect = load_text.get_rect()
        load_text_position = play_text_position[0], play_text_position[1] + self.separation
        SCREEN.blit(load_text, load_text_position)

        # Options Button Text
        opt_text = self.item_font.render("OPTIONS", True, MainMenu.text_color[2])
        opt_text_rect = opt_text.get_rect()
        opt_text_position = play_text_position[0], play_text_position[1] + 2 * self.separation
        SCREEN.blit(opt_text, opt_text_position)

        # Quit Button Text
        quit_text = self.item_font.render("QUIT", True, MainMenu.text_color[3])
        quit_text_rect = quit_text.get_rect()
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


def play(self):
        pass
        '''
        while True:
            PLAY_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("black")

            PLAY_TEXT = get_font(45).render("This is the PLAY screen.", True, "White")
            PLAY_RECT = PLAY_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(PLAY_TEXT, PLAY_RECT)

            PLAY_BACK = Button(image=None, pos=(640, 460),
                               text_input="BACK", font=get_font(75), base_color="White", hovering_color="Green")

            PLAY_BACK.changeColor(PLAY_MOUSE_POS)
            PLAY_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if PLAY_BACK.checkForInput(PLAY_MOUSE_POS):
                        main_menu()

            pygame.display.update()

    def options(self):
        pass
        
        while True:
            OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

            SCREEN.fill("white")

            OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
            OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
            SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

            OPTIONS_BACK = Button(image=None, pos=(640, 460),
                                  text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")

            OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
            OPTIONS_BACK.update(SCREEN)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                        main_menu()

            pygame.display.update()'''


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
                    pass
                elif main_menu.Δy == main_menu.Δy_init + main_menu.separation:  # Position: Load
                    print("load")
                elif main_menu.Δy == main_menu.Δy_init + 2 * main_menu.separation:  # Position: Options
                    print("opt")
                elif main_menu.Δy == main_menu.Δy_init + 3 * main_menu.separation:  # Position: Quit
                    run = False

    # Player Icon Movement Boundaries
    if main_menu.Δy > 4 * main_menu.separation:
        main_menu.Δy = main_menu.Δy_init

    if main_menu.Δy < main_menu.Δy_init:
        main_menu.Δy = main_menu.Δy_init + 3 * main_menu.separation

    # Change text color when selected
    if main_menu.Δy == main_menu.Δy_init:
        MainMenu.text_color = [
            MainMenu.hover_color,
            MainMenu.base_color,
            MainMenu.base_color,
            MainMenu.base_color
        ]
    if main_menu.Δy == main_menu.Δy_init + main_menu.separation:
        MainMenu.text_color = [
            MainMenu.base_color,
            MainMenu.hover_color,
            MainMenu.base_color,
            MainMenu.base_color
        ]
    if main_menu.Δy == main_menu.Δy_init + 2 * main_menu.separation:
        MainMenu.text_color = [
            MainMenu.base_color,
            MainMenu.base_color,
            MainMenu.hover_color,
            MainMenu.base_color
        ]
    if main_menu.Δy == main_menu.Δy_init + 3 * main_menu.separation:
        MainMenu.text_color = [
            MainMenu.base_color,
            MainMenu.base_color,
            MainMenu.base_color,
            MainMenu.hover_color
        ]

    # Apply Changes
    pygame.display.update()
