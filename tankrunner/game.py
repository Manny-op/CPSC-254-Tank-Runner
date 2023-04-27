"""This file contains the TankRunner class which builds and runs the game."""

import pygame
from tankrunner.window import WindowTitle
from tankrunner.window import WindowGame


class TankRunner:
    """This class represents the Tank Runner game."""

    def __init__(self, window_width=800, window_height=600, window_title="Tank Runner"):
        """Initialization of TankRunner."""
        pygame.init()
        self._window_size = (window_width, window_height)
        self._clock = pygame.time.Clock()
        self._window = pygame.display.set_mode(self._window_size)
        self._title = window_title
        pygame.display.set_caption(self._title)
        self._game_over = False
        self._windows = [ 
                        WindowTitle("Tank Runner", self._window),
                        WindowGame(self._window),
                        WindowTitle("Tank Runner", self._window)]

    def run(self):
        """A loop that runs the game."""
        for scene in self._windows:
            while scene.valid:
                self._clock.tick(scene.frame_rate)
                for event in pygame.event.get():
                    scene.handle_event(event)
                scene.update()
                scene.draw()
                pygame.display.update()
        pygame.quit()
        return 0
