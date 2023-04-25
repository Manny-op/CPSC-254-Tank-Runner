"""This file contains the Obstacle class which represents the obstalces in TankRunner"""

import pygame


class Obstacle():
    """This class represents the Tank in TankRunner."""

    def __init__(self, surface):
        """Initialize the Obstacle."""
        self._surface = surface
        self._color = (255, 255, 255)
        self._obstacle = pygame.Rect(600, 495, 40, 8)
        self._obstacle_x_postion = self._obstacle.x
        self._obstacle_y_positon = self._obstacle.y

    def draw(self):
        """Draw the Tank."""
        pygame.draw.rect(self._surface, self._color, self._obstacle)

    def move(self):
        """Control the Obstacle movement."""
        self._obstacle.x -= 2

