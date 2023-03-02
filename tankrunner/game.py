"""File decleration"""

import pygame


class TankRunner:
    """This class represents the Tank Runner game."""

    def __init__(self, window_with=800, window_height=600, window_title="Tank Runner", background_color=(156, 167, 184)):
        """Initialization of the Tank Runner game."""
        pygame.init()
        self._window_size = (window_with, window_height)
        self._clock = pygame.time.Clock()
        self._screen = pygame.display.set_mode(self._window_size)
        self._screen.fill(background_color)
        self._title = window_title
        pygame.display.set_caption(self._title)

    def run(self):
        """A loop that will run the game."""
        running = True
        while running:
            for event in pygame.event.get():
                pygame.display.update()
                if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                    running = False
        pygame.quit()
        return 0
