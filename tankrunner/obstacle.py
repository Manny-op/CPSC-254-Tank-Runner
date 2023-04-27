"""This file contains the Obstacle class which represents the obstalces in TankRunner"""

import pygame


class Obstacle():
    """This class represents the Tank in TankRunner."""

    def __init__(self, surface):
        """Initialize the Obstacle."""
        self._surface = surface
        self._color = (255, 255, 255)
        self._obstacle = pygame.Rect(800, 495, 40, 8)
        self._obstacle_copy = pygame.Rect(800, 495, 40, 8)
        self._list = []

    def draw(self):
        """Draw the Tank."""
        pygame.draw.rect(self._surface, self._color, self._obstacle)
        if self._obstacle.x < 0:
            pygame.draw.rect(self._surface, self._color, self._obstacle_copy)
            self._obstacle = pygame.Rect(800, 495, 40, 8)
        if self._obstacle_copy.x < 0:
            pygame.draw.rect(self._surface, self._color, self._obstacle)
            self._obstacle_copy = pygame.Rect(800, 495, 40, 8)

    def move(self):
        """Control the Obstacle movement."""
        self._obstacle.x -= 4
        if self._obstacle.x < 0:
            self._obstacle_copy.x -= 4
        if self._obstacle_copy.x < 0:
            self._obstacle.x -= 4

    def does_collide(self, player_pos):
        """Check if the obstacle collides with a player."""
        if self._obstacle.colliderect(player_pos) or self._obstacle_copy.colliderect(player_pos):
            return True
