# Scripts
from constants import *

# Modules
import pygame
from pygame import mixer


class MainMenu:
    def __init__(self):
        self.image = pygame.image.load('Images/Main_Menu/main_menu_img.png')
        self.font_size_title = 94
        self.font_size_item = 50
        self.title_font = pygame.font.Font('freesansbold.ttf', self.font_size_title)
        self.item_font = pygame.font.Font('freesansbold.ttf', self.font_size_item)

    def show(self):
        # Background Image
        SCREEN.blit(self.image, (0, 0))

        # Main Menu Text
        mm_text = self.title_font.render("GAME PROJECT", True, (255, 255, 255))
        mm_text_rect = mm_text.get_rect()
        mm_text_position = (WIDTH/2 - mm_text_rect.width/2, 1/3 * HEIGHT - mm_text_rect.height/2)
        SCREEN.blit(mm_text, mm_text_position)

        # Play Button Text
        play_text = self.item_font.render("PLAY", True, (255, 255, 255))
        play_text_rect = play_text.get_rect()
        play_text_position = (WIDTH/2 - play_text_rect.width/2, 3/5 * HEIGHT - play_text_rect. height/2)
        SCREEN.blit(play_text, play_text_position)

        # Load Button Text
        load_text = self.item_font.render("LOAD", True, (255, 255, 255))
        load_text_rect = load_text.get_rect()
        load_text_position = play_text_position[0], play_text_position[1] + 70
        SCREEN.blit(load_text, load_text_position)

        # Options Button Text
        opt_text = self.item_font.render("OPTIONS", True, (255, 255, 255))
        opt_text_rect = opt_text.get_rect()
        opt_text_position = play_text_position[0], play_text_position[1] + 140
        SCREEN.blit(opt_text, opt_text_position)

        # Quit Button Text
        quit_text = self.item_font.render("QUIT", True, (255, 255, 255))
        quit_text_rect = quit_text.get_rect()
        quit_text_position = play_text_position[0], play_text_position[1] + 210
        SCREEN.blit(quit_text, quit_text_position)

        '''
        MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                             text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                                text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                             text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    options()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()

        pygame.display.update()'''



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

            pygame.display.update()'''

    def options(self):
        pass
        '''
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

