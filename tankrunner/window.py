"""This file contains the Window class and its subclasses.These classes build the Windows of the game."""

import pygame


class Window:
    """This class represents a TankRuner game Window."""

    def __init__(self, window):
        """Initialize the Window object."""
        self._window = window
        self._background = pygame.Surface(self._window.get_size())
        self._background_color = (156, 167, 184)
        self._background.fill(self._background_color)
        self._valid = True
        self._frame_rate = 60

    def update(self):
        """Update the Window."""
        pass

    def draw(self):
        """Draw the window."""
        self._window.blit(self._background, (0, 0))

    @property
    def frame_rate(self):
        """Return the frame rate."""
        return self._frame_rate

    @property
    def valid(self):
        """Return weather a Window is valid."""
        return self._valid

    def handle_event(self, event):
        """Trigger to move to next Window."""
        if event.type == pygame.QUIT:
            self._valid = False
        elif event.type == pygame.KEYDOWN and \
            event.key == pygame.K_SPACE:
            self._valid = False


class WindowTitle(Window):
    """A sublcass of Window that represents the Window title of TankRunner."""

    def __init__(self, title, window):
        """Initialize WindowTitle."""
        super().__init__(window)
        self._game_title = title

    def draw(self):
        """Draw the WindowTitle."""
        super().draw()
        (width, height) = self._window.get_size()
        font = pygame.font.get_default_font()
        window_font = pygame.font.Font(font, 70)
        render_window = window_font.render(self._game_title, True, (0, 0, 0))
        position = render_window.get_rect(center=(width/2, 100))
        self._window.blit(render_window, position)
