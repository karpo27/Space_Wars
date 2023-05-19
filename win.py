# Scripts:
from constants import *
from base_state import BaseState
from background_creator import BackgroundCreator
from text_creator import TextCreator
from pointer import Pointer
from game_effects import Particle

# Modules:
import pygame
import random


class Win(BaseState):
    def __init__(self):
        super().__init__()
        # Screen Text and Options:
        self.pos = self.pos_x, self.pos_y = WIDTH/2, HEIGHT/7
        self.text = ["CONGRATULATIONS"]
        self.win = []
        self.win.append(TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color,
                                    (WIDTH / 2, 5 / 6 * HEIGHT), "", 50))
        self.win.append(
            TextCreator(self.index + 1, self.text[0], self.font_type, 84, 84, self.base_color, self.hover_color, self.pos,
                        "", 40))

        # Create Sprites Group:
        self.effects_group = pygame.sprite.Group()

        # Initialize Classes:
        self.background = BackgroundCreator(*BACKGROUNDS['win'])
        self.pointer = Pointer()

        # Effects:
        self.ref_time = 70
        self.fire_rate = 70

    def handle_action(self):
        self.next_state = "MENU"
        self.screen_done = True

    def create_fireworks(self):
        if self.fire_rate >= self.ref_time:
            self.fire_rate = 0
            pos = random.randrange(50, WIDTH - 50), random.randrange(50, HEIGHT - 50)
            for num_particles in range(random.randrange(65, 95)):
                Particle(pos, self.effects_group)

        # Reset Fire Bullet Variables:
        if self.fire_rate < self.ref_time:
            self.fire_rate += 1

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_action()

    def draw(self, surface):
        # Draw Background:
        self.background.update()
        self.create_fireworks()

        # Render Win:
        for text in self.win:
            text.render_text(self.index)
        self.pointer.draw_rotated(self.win[self.index].text_position, "CONGRATULATIONS")

        # Update Sprites Group:
        self.effects_group.update()

        # Draw Sprite Groups:
        self.effects_group.draw(SCREEN)
