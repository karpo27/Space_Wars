# Modules:
import pygame


class Game(object):
    def __init__(self, screen, states, initial_state):
        # Screen:
        self.screen = screen
        # Indicates if showing Screen is done or not:
        self.screen_done = False

        # Define Clock for Screen FPS:
        self.clock = pygame.time.Clock()
        self.fps = 60

        # States:
        self.states = states
        self.state_name = initial_state
        # Search for actual Game State in states dict:
        self.state = self.states[self.state_name]

    def loop_events(self):
        for event in pygame.event.get():
            # Brings every event from Current Game State:
            self.state.get_event(event)

    def flip_state(self):
        #current_state = self.state_name
        next_state = self.state.next_state
        self.state.screen_done = False
        self.state_name = next_state
        persistent = self.state.persist
        self.state = self.states[self.state_name]
        #self.state.startup(persistent)

    def update(self, dt):
        # Check State to Next Action:
        if self.state.quit:
            self.screen_done = True
        elif self.state.screen_done:
            self.flip_state()
        # Call Update Method for Current Game State:
        self.state.update(dt)

    def draw(self):
        self.state.draw(self.screen)

    def run(self):
        while not self.screen_done:
            dt = self.clock.tick(self.fps)
            self.loop_events()
            self.update(dt)
            self.draw()
            pygame.display.update()
