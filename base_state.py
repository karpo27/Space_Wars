# Scripts:
from constants import WIDTH, HEIGHT, SCREEN
from pointer import Pointer
from text_creator import TextCreator
from sound import menu_movement

# Modules:
import pygame




class BaseState(object):
    def __init__(self):
        # Game State:
        self.screen_done = False
        self.quit = False
        self.next_state = None
        self.persist = {}

        # Screen:
        self.screen = None
        self.options_qty = 0

        # Text Properties:
        self.index = 0
        self.pos = self.pos_x, self.pos_y = WIDTH/2, 3/5 * HEIGHT
        self.font_type = 'freesansbold.ttf'
        self.base_color = "white"
        self.hover_color = "#f1d666"

        # Empty Surface:
        self.image = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        self.rect = self.image.get_rect()
        self.rect.center = [0, 0]
        self.empty_surface = None
        self.alpha = 0

        # Initialize Objects:
        self.background = None
        self.pointer = Pointer()

        # Back Text:
        self.back = TextCreator(self.index, "BACK", self.font_type, 48, 48, self.base_color, self.hover_color,
                                (WIDTH / 2, 9 / 10 * HEIGHT), "", 50)
        self.back_ref_time = 950
        self.back_time = 0

        # Score:
        self.score_pos = WIDTH / 2, 3 / 4 * HEIGHT
        self.score_size = 48

        # Others:
        self.next_screen_rate = 0
        self.next_screen_ref_time = 1

    def handle_movement(self, movement):
        self.index += movement
        if self.options_qty >= 1:
            menu_movement.play_sound()

    def handle_left_audio(self, audio_object):
        if self.index == 0:
            if audio_object.sound_volume > 0:
                audio_object.update_volume(-1, "sound")
        elif self.index == 1:
            if audio_object.music_volume > 0:
                audio_object.update_volume(-1, "music")

    def handle_right_audio(self, audio_object):
        if self.index == 0:
            if audio_object.sound_volume < 10:
                audio_object.update_volume(1, "sound")
        elif self.index == 1:
            if audio_object.music_volume < 10:
                audio_object.update_volume(1, "music")

    def set_opacity(self):
        self.empty_surface.set_alpha(self.alpha)
        self.empty_surface.blit(self.image, (0, 0))
        SCREEN.blit(self.empty_surface, self.rect.center)

    def render_image(self):
        pass

    def render_options(self, options_object):
        for text in options_object:
            text.render_text(self.index)
        self.pointer.draw_rotated(options_object[self.index].text_position, self.screen)

    def render_back_text(self, score_object):
        if self.back_time >= self.back_ref_time:
            self.back.render_text(self.index)
            score_object.show_score(self.score_pos, self.score_size)
            self.pointer.draw_rotated(self.back.text_position, "CONGRATULATIONS")
        else:
            self.back_time += 1

    def startup(self, persistent):
        self.persist = persistent

    def handle_action(self):
        pass

    def get_event(self, event):
        pass

    def update(self, dt):
        pass

    def draw(self, surface):
        pass
