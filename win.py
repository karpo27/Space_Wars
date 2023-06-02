# Scripts:
from constants import *
from base_state import BaseState
from bg_creator import BGCreator
from text_creator import TextCreator
from pointer import Pointer
from game_effects import Particle
from sound import menu_bg, win_fireworks
from hud import score

# Modules:
import pygame
import random


class Win(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.pos = self.pos_x, self.pos_y = WIDTH/2, HEIGHT/10
        self.text_1 = ""
        self.text_1_ref_time = 24
        self.text_1_rate = 0
        self.text_2 = "You have saved our Galaxy!"

        # Back Text:
        self.back = TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color, (WIDTH / 2, 9 / 10 * HEIGHT), "", 50)
        self.back_ref_time = 950
        self.back_time = 0

        # Create Sprites Group:
        self.effects_group = pygame.sprite.Group()

        # Initialize Classes:
        self.background = BGCreator(*BACKGROUNDS['win'])
        self.pointer = Pointer()

        # Background Image:
        self.image = self.background.image
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]
        # Empty Surface:
        self.empty_surface = pygame.Surface(self.background.image.get_size(), pygame.SRCALPHA)
        self.alpha = 0
        # Time on Screen:
        self.time = 0
        self.time_start_render = 40  # 40 ms
        self.time_finish_render = self.time_start_render + 540  # 540 ms

        # Fireworks Effect:
        self.ref_time = 80
        self.fire_rate = 80

        # Score:
        self.score_pos = WIDTH/2, 3/4 * HEIGHT
        self.score_size = 48

    def update_text(self):
        ref_text = "CONGRATULATIONS"
        if len(self.text_1) < len(ref_text):
            for i in range(len(self.text_1), len(self.text_1) + 1):
                self.text_1 += ref_text[i]

    def handle_action(self):
        if self.back_time >= self.back_ref_time:
            self.next_state = "MENU"
            self.screen_done = True
            menu_bg.play_bg_music(-1)

    def create_fireworks(self):
        if self.fire_rate >= self.ref_time:
            self.fire_rate = 0
            pos = random.randrange(50, WIDTH - 50), random.randrange(50, HEIGHT - 50)
            for num_particles in range(random.randrange(65, 110)):
                Particle(pos, self.effects_group)
            win_fireworks.play_sound()
        # Reset Fire Bullet Variables:
        if self.fire_rate < self.ref_time:
            self.fire_rate += 1

    def render_top_text(self):
        if len(self.text_1) < 15:
            if self.text_1_rate >= self.text_1_ref_time:
                self.update_text()
                self.text_1_rate = 0
            else:
                self.text_1_rate += 1
        if self.back_time >= self.back_ref_time * 3/4:
            TextCreator(self.index + 2, self.text_2, self.font_type, 38, 38, self.base_color, None, [self.pos[0], self.pos[1] + 74], "", 74).render_text(self.index)
        TextCreator(self.index + 1, self.text_1, self.font_type, 78, 78, self.base_color, None, self.pos, "", 74).render_text(self.index)

    def render_back_text(self):
        if self.back_time >= self.back_ref_time:
            self.back.render_text(self.index)
            score.show_score(self.score_pos, self.score_size)
            self.pointer.draw_rotated(self.back.text_position, "CONGRATULATIONS")
        else:
            self.back_time += 1

    def render_image(self):
        if self.time_start_render < self.time <= self.time_finish_render:
            self.set_opacity()
            self.alpha += 0.5
        elif self.time_finish_render < self.time:
            SCREEN.blit(self.empty_surface, self.rect.center)
        self.time += 1

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))
        self.render_image()

        # Draw Fireworks:
        self.create_fireworks()

        # Render Text 1 and Text 2:
        self.render_top_text()
        # Render Back Text and Score:
        self.render_back_text()

        # Update Sprites Group:
        self.effects_group.update()

        # Draw Sprite Groups:
        self.effects_group.draw(SCREEN)
