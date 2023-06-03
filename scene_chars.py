# Scripts:
from constants import WIDTH, HEIGHT, SCREEN, SCENE_CHARS
from character import Character

# Modules:


class SceneChar(Character):
    def __init__(self, category, img_path, scale, start_pos, vel, final_pos, hp, state):
        super().__init__(category, img_path, scale, vel, hp)
        # Image:
        self.start_pos = start_pos
        self.rect.center = self.start_pos

        # Start Movement Animation:
        self.start_animation = True
        self.start_pos_x = self.start_pos[0]
        # End Movement Animation:
        self.final_pos = final_pos

    def animate_start(self):
        if self.start_pos_x < self.final_pos:
            if self.rect.x < self.final_pos:
                self.rect.x += self.vel_x
            else:
                self.start_animation = False
        else:
            if self.rect.x > self.final_pos:
                self.rect.x += self.vel_x
            else:
                self.start_animation = False

    def animate_end(self):
        if self.rect.x != self.start_pos_x:
            self.rect.x -= self.vel_x
        else:
            self.end_animation = False
