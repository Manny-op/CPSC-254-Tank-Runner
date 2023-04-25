"""This file contains the Tank class which represents the tank the player will control."""

import pygame


class Tank():
    """This class represents the Tank in TankRunner."""

    def __init__(self, surface):
        """Initialize the Tank."""
        self._surface = surface
        self._color = (255, 255, 255)
        self._tank = pygame.Rect(100, 495, 40, 8)
        self._tank_x_postion = self._tank.x
        self._tank_y_positon = self._tank.y

    def draw(self):
        """Draw the Tank."""
        pygame.draw.rect(self._surface, self._color, self._tank)

    def move(self):
        """Control the Tank movement."""
        key = pygame.key.get_pressed()
        if key[pygame.K_SPACE]:
            self._tank.y -= 2
        elif self._tank.y != self._tank_y_positon:
            self._tank.y += 2
