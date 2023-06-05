# Scripts:
from constants import WIDTH, HEIGHT, SCREEN, BACKGROUNDS, SCENE_CHARS
from base_state import BaseState
from bg_creator import BGCreator
from scene_chars import SceneChar
from text_creator import TextCreator
from sound import scene_1_galaxy, level1_bg

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
        self.time_finish_render = self.time_start_render + 510  # 510 ms
        self.time_start_animation_scene_chars = self.time_finish_render + 30  # 30 ms
        self.time_start_dialogue = self.time_start_animation_scene_chars + 200  # 200 ms
        self.end_scene = False

        # Initialize Objects:
        self.operator = SceneChar(*SCENE_CHARS['operator'])
        self.commander = SceneChar(*SCENE_CHARS['commander'])
        self.dialogue_globe = SceneChar(*SCENE_CHARS['dialogue'])

        # Create Sprites Group:
        self.scene_chars_group = pygame.sprite.Group()

        # Add Player Sprites to group:
        self.scene_chars_group.add(self.operator, self.commander)

        # Screen Dialogue:
        self.pos = self.pos_x, self.pos_y = WIDTH/2 - 128, 4/5 * HEIGHT - 75
        self.dialogue = [
            ['OPERATOR:', '"Commander!', 'I\'m receiving a message...', '... Andromeda has been destroyed."'],
            ['COMMANDER:', '"It\'s the BUGS!!!', 'God damn it!...', 'General Bugfix will exterminate us."'],
            ['OPERATOR:', '"The fleet is on the other side of the', 'galaxy...', 'What should we do?"'],
            ['COMMANDER:', '"We\'re doomed...', 'by the time reinforcements reach', 'here, we\'ll be dust."'],
            ['OPERATOR:', '"...', 'We have an X-Wing pilot on it\'s way', 'back to planet Earth.', 'Should I call him?"'],
            ['COMMANDER:', '"DO IT!!!', 'Let\'s hope he can handle the whole', 'swarm army..."'],
            ['OPERATOR:', '"... Pilot!, Pilot!', 'Do you read me?', '... ... ...', '... ... ..."'],
        ]
        self.index_1 = 0
        self.index_2 = 0

        self.text = ""
        self.text_list = []
        self.text_list.append(self.text)
        self.text_ref_time = 5
        self.text_rate = 0

    def render_top_text(self):
        if self.index_2 < len(self.dialogue):
            if self.index_1 < len(self.dialogue[self.index_2]):
                i = len(self.dialogue[self.index_2][self.index_1]) - len(self.text)
                if i != 0:
                    if self.text_rate >= self.text_ref_time:
                        self.text += self.dialogue[self.index_2][self.index_1][-i]
                        self.text_list[self.index_1] = self.text
                        self.text_rate = 0
                    else:
                        self.text_rate += 1
                else:
                    self.index_1 += 1
                    self.text = ""
                    self.text_list.append(self.text)
                    self.text_rate = 0
                for index, text in enumerate(self.text_list):
                    TextCreator(index, text, self.font_type, 20, 20, self.base_color, self.base_color, self.pos,
                                self.dialogue[0][0], 32).render_text(index)
            else:
                self.index_2 += 1
                self.index_1 = 0
                self.text = ""
                self.text_list = []
                self.text_list.append(self.text)
                self.text_rate = 0
        else:
            for scene_char in self.scene_chars_group:
                scene_char.end_animation = True
            self.end_scene = True

    def render_image(self):
        if self.time_start_render < self.time <= self.time_finish_render:
            self.set_opacity()
            self.alpha += 0.5
        elif self.time_finish_render < self.time:
            SCREEN.blit(self.empty_surface, self.rect.center)
        if self.alpha == 210 and not self.end_scene:
            scene_1_galaxy.play_sound()
        self.time += 1

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True

    def draw(self, surface):
        # Draw Background:
        surface.fill(pygame.Color("black"))
        self.render_image()

        # End Scene Logic:
        if self.end_scene:
            self.alpha -= 0.7
            self.set_opacity()
            self.scene_chars_group.remove(self.dialogue_globe)
            if self.alpha <= 0:
                self.screen_done = True
                level1_bg.play_bg_music(-1)

        if self.time_start_animation_scene_chars <= self.time:
            # Update Sprites Group:
            self.scene_chars_group.update()
            # Draw Sprite Groups:
            self.scene_chars_group.draw(SCREEN)

        if not self.commander.start_animation:
            self.scene_chars_group.add(self.dialogue_globe)

        # Render Text 1 and Text 2:
        if self.time_start_dialogue <= self.time:
            self.render_top_text()
