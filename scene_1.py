# Scripts:
from constants import WIDTH, HEIGHT, SCREEN, BACKGROUNDS, SCENE_CHARS
from base_state import BaseState
from bg_creator import BGCreator
from scene_chars import SceneChar
from text_creator import TextCreator
from sound import channel, scene_1_galaxy_laser, scene_1_galaxy_explosion, scene_1_dialogue_globe, scene_1_dialogue_letter, level_1_bg

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
        self.text_ref_time = 4
        self.text_rate = 0
        self.added_dialogue_globe = False

    def render_top_text(self):
        if self.index_2 < len(self.dialogue):
            if self.index_1 < len(self.dialogue[self.index_2]):
                i = len(self.dialogue[self.index_2][self.index_1]) - len(self.text)
                if i != 0:
                    if self.text_rate >= self.text_ref_time:
                        self.text += self.dialogue[self.index_2][self.index_1][-i]
                        scene_1_dialogue_letter.play_sound()
                        self.text_list[self.index_1] = self.text
                        self.text_rate = 0
                    else:
                        self.text_rate += 1
                else:
                    self.index_1 += 1
                    self.text = ""
                    self.text_list.append(self.text)
                    self.text_rate = 0
                self.render_dialogue()
            else:
                if self.text_rate >= 10 * self.text_ref_time:
                    self.index_2 += 1
                    self.index_1 = 0
                    self.text = ""
                    self.text_list = []
                    self.text_list.append(self.text)
                    self.text_rate = 0
                else:
                    self.render_dialogue()
                    self.text_rate += 1
        else:
            for scene_char in self.scene_chars_group:
                scene_char.end_animation = True
            self.end_scene = True

    def render_dialogue(self):
        for index, text in enumerate(self.text_list):
            TextCreator(index, text, self.font_type, 20, 20, self.base_color, self.base_color, self.pos,
                        self.dialogue[0][0], 32).render_text(index)

    def render_image(self):
        if self.time_start_render < self.time <= self.time_finish_render:
            self.set_opacity()
            self.alpha += 0.5
        elif self.time_finish_render < self.time:
            SCREEN.blit(self.empty_surface, self.rect.center)
        if self.alpha == 70 and not self.end_scene:
            scene_1_galaxy_laser.play_sound(True)
            scene_1_galaxy_explosion.play_sound(True)
        self.time += 1
        if not self.end_scene:
            self.render_skip_text()

    def finish_scene(self):
        if self.end_scene:
            self.alpha -= 0.5
            self.set_opacity()
            self.scene_chars_group.remove(self.dialogue_globe)
            if self.alpha <= 140:
                pygame.mixer.music.fadeout(6000)
            if self.alpha <= 0:
                self.screen_done = True
                level_1_bg.play_bg_music(-1)

    def update_scene_chars(self):
        # Draw and Update Sprites:
        if self.time_start_animation_scene_chars <= self.time:
            # Update Sprites Group:
            self.scene_chars_group.update()
            # Draw Sprite Groups:
            self.scene_chars_group.draw(SCREEN)
        if not self.commander.start_animation and not self.added_dialogue_globe:
            self.scene_chars_group.add(self.dialogue_globe)
            scene_1_dialogue_globe.play_sound()
            self.added_dialogue_globe = True

        # Dialogue Logic:
        if self.time_start_dialogue <= self.time and not self.end_scene:
            self.render_top_text()

    def render_skip_text(self):
        # Skip Text:
        TextCreator(self.index, "Press ENTER to Skip", self.font_type, 14, 14, self.base_color, self.base_color,
                    (7/8 * WIDTH, 1/40 * HEIGHT), "", 50).render_text(self.index)

    def handle_ending(self):
        for scene_char in self.scene_chars_group:
            scene_char.end_animation = True
        self.end_scene = True

    def get_event(self, event):
        if event.type == pygame.QUIT:
            self.quit = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                self.handle_ending()

    def draw(self, surface):
        # Draw Black Background:
        surface.fill(pygame.Color("black"))
        # Draw Background Image:
        self.render_image()
        # Finish Scene:
        self.finish_scene()
        # Draw Scene Chars:
        self.update_scene_chars()
