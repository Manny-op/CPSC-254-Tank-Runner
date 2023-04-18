
import pygame

class Window:
    """"""

    def __init__(self, window):
        """Initialize the Window object."""
        self._window = window
        self._background = pygame.Surface(self._window.get_size())
        self._background_color = (156, 167, 184)
        self._background.fill(self._background_color)
        self._valid = True
        self._frame_rate = 60

    def update(self):
        pass

    def draw(self):
        self._window.blit(self._background, (0,0))

    @property
    def frame_rate(self):
        return self._frame_rate
    
    @property
    def valid(self):
        return self._valid
    
    def handle_event(self, event):
        """Trigger to move to next Window."""
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE :
            self._valid = False


class WindowTitle(Window):
    def __init__(self, title, window):
        super().__init__(window)
        self._game_title = title

    def draw(self):
        super().draw()
        (width, height) = self._window.get_size()
        font = pygame.font.get_default_font()
        window_font = pygame.font.Font(font, 70)
        render_window = window_font.render(self._game_title, True, (0,0,0))
        position = render_window.get_rect(center=(width/2, 100))
        self._window.blit(render_window, position)
    
