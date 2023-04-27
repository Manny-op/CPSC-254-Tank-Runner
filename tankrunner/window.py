"""This file contains the Window class and its subclasses.These classes build the Windows of the game."""

import pygame
from tankrunner.tank import Tank
from tankrunner.obstacle import Obstacle


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
            event.key == pygame.K_ESCAPE:
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


class WindowGame(Window):
    """A subclass of Window that represents the game Window of TankRunner."""

    def __init__(self, window):
        """Intialize WindowGame."""
        super().__init__(window)
        self._score = 0
        self._game_over = False
        self._tank = Tank(self._window)
        self._obstacle = Obstacle(self._window)

    def draw(self):
        """Draw the game Window."""
        super().draw()
        font = pygame.font.get_default_font()
        score_font = pygame.font.Font(font, 20)
        render_score = score_font.render(str(self._score), True, (0, 0, 0))
        positon = (750, 25)
        self._window.blit(render_score, positon)
        floor = pygame.draw.line(self._window, (0, 0, 0), [0, 500], [800, 500], width=5)

        self._tank.draw()
        self._obstacle.draw()
        

    def change_score(self):
        """Update the scoreboard."""
        self._score += 1
        font = pygame.font.get_default_font()
        score_font = pygame.font.Font(font, 20)
        render_score = score_font.render(str(self._score), True, (0, 0, 0))
        positon = (750, 25)
        self._window.blit(render_score, positon)

    def update(self):
        """Update the game Window."""
        self._tank.move()
        self._obstacle.move()
        if self._obstacle.does_collide(self._tank._tank):
            self._game_over = True
            # Display the game over
            pygame.time.delay(4000)
            self._valid = False
        if self._game_over != True:
            self.change_score()
