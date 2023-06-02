# Scripts:
from constants import *
from base_state import BaseState
from sound import sounds_list, musics_list

# Modules:
from text_creator import TextCreator


class Options(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.text = ["AUDIO", "CONTROLS", "BACK"]
        self.options = []
        for index, text in enumerate(self.text):
            self.options.append(
                TextCreator(index, text, self.font_type, 48, 52, self.base_color, self.hover_color, self.pos,
                            self.text[0], 70))


class Controls(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.pos_left = self.left_x, self.left_y = WIDTH / 3 + 50, HEIGHT / 3 - 80
        self.pos_right = self.left_x + 300, self.left_y
        self.text_left = ["Move Forward", "Move Back", "Move Left", "Move Right", "Fire"]
        self.text_right = ["W / ARROW UP", "S / ARROW DOWN", "A / ARROW LEFT", "D / ARROW RIGHT", "SPACE"]
        self.controls = []
        self.controls.append(TextCreator(self.index, "BACK", self.font_type, 48, 52, self.base_color, self.hover_color,
                                         (WIDTH / 2, 5 / 6 * HEIGHT), "", 50))
        for index, text in enumerate(self.text_left):
            self.controls.append(
                TextCreator(index + 1, text, self.font_type, 30, 52, self.base_color, self.hover_color, self.pos_left,
                            self.text_left[0], 44))
        for index, text in enumerate(self.text_right):
            self.controls.append(
                TextCreator(index + 1, text, self.font_type, 30, 52, self.base_color, self.hover_color, self.pos_right,
                            self.text_right[0], 44))


class Credits(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.pos = self.pos_x, self.pos_y = WIDTH / 2, HEIGHT / 4
        self.text = ["May 2023", "SPACE WARS is a Python game developed by me: Julian Giudice (github.com/karpo27).",
                     "It's a Shoot 'em up inspired in Galaga game and has some elements from things I like.",
                     "Also my first game since I started learning Python 6 months ago.",
                     "I want to thank Pygame for allowing me to use this module,",
                     "and allow so many users to code their games.",
                     "I'll keep coding and trying myself harder everyday."]
        self.credits = []
        self.credits.append(TextCreator(self.index, "BACK", self.font_type, 48, 52, self.base_color, self.hover_color,
                                        (WIDTH / 2, 5 / 6 * HEIGHT), "", 50))
        for index, text in enumerate(self.text):
            self.credits.append(
                TextCreator(index + 1, text, self.font_type, 22, 52, self.base_color, self.hover_color, self.pos,
                            "", 40))


class Audio(BaseState):
    def __init__(self):
        # Screen Text and Options:
        super().__init__()
        self.pos = self.pos_x, self.pos_y = WIDTH / 2, HEIGHT / 3
        self.sound_volume = 5
        self.music_volume = 5
        self.audio = []
        self.update_text()

    def update_text(self):
        options = [f'SOUND VOLUME        «  {str(self.sound_volume)}  »',
                   f'MUSIC VOLUME        «  {str(self.music_volume)}  »']
        self.audio = []
        for index, text in enumerate(options):
            self.audio.append(
                TextCreator(index, text, self.font_type, 48, 52, self.base_color, self.hover_color, self.pos,
                            text, 70))
        self.audio.append(TextCreator(self.index + 2, "BACK", self.font_type, 48, 52, self.base_color, self.hover_color,
                                      (WIDTH / 2, 5 / 6 * HEIGHT), "", 0))

    def update_volume(self, value, category):
        # Update Volumes:
        if category == "sound":
            self.sound_volume += value
            for sound in sounds_list:
                sound.update_volume(self.sound_volume, "sound")
        else:
            self.music_volume += value
            for music in musics_list:
                music.update_volume(self.music_volume, "music")
        # Update Text:
        self.update_text()


# Initialize Object:
audio = Audio()
