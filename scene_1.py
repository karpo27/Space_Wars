# Scripts:
from constants import SCREEN, BACKGROUNDS, SCENE_CHARS
from base_state import BaseState
from bg_creator import BGCreator
from scene_chars import SceneChar
from sound import scene_1_galaxy

# Modules:
import pygame



# Initialize Pygame:
pygame.init()


class Scene1(BaseState):
    def __init__(self):
        super().__init__()
        # Next State:
        self.next_state = "LEVEL_1"

        # Background Image:
        self.background = BGCreator(*BACKGROUNDS['scene_1'])
        self.image = self.background.image
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]
        # Empty Surface:
        self.empty_surface = pygame.Surface(self.background.image.get_size(), pygame.SRCALPHA)
        self.alpha = 0
        # Time on Screen:
        self.time = 0
        self.time_start_render = 150  # 150 ms
        self.time_finish_render = self.time_start_render + 515  # 515 ms
        self.time_start_dialogue = self.time_finish_render + 30     # 30 ms

        # Initialize Objects:
        self.operator = SceneChar(*SCENE_CHARS['operator'])
        self.minister = SceneChar(*SCENE_CHARS['minister'])

        # Create Sprites Group:
        self.scene_chars_group = pygame.sprite.Group()

        # Add Player Sprites to group:
        self.scene_chars_group.add(self.operator, self.minister)

    def render_image(self):
        if self.time_start_render < self.time <= self.time_finish_render:
            self.set_opacity()
            self.alpha += 0.5
        elif self.time_finish_render < self.time:
            SCREEN.blit(self.empty_surface, self.rect.center)
        if self.alpha == 210:
            scene_1_galaxy.play_sound()
        self.time += 1

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))
        self.render_image()

        if self.time_start_dialogue <= self.time:
            # Update Sprites Group:
            self.scene_chars_group.update()

            # Draw Sprite Groups:
            self.scene_chars_group.draw(SCREEN)

        #level1_bg.play_bg_music(-1)

