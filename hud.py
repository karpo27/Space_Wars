# Scripts:
from base_state import BaseState
from text_creator import TextCreator

# Modules:


class Score(BaseState):
    def __init__(self):
        super().__init__()
        self.score = 0

    def update_score(self, value):
        self.score += value

    def show_score(self, pos, font_size):
        TextCreator(0, f'Score: {str(self.score)}', self.font_type, font_size, 40, self.base_color, None,
                    pos, "", 0).render_text(-1)


# Initialize Objects:
score = Score()
