# things the player should be able to do
# move, aim, shoot
# other things that should be in this file
# render out the player 
import pygame
import math

class Player:
    color = [0, 155, 30]

    def movement():
        pass

    def aim():
        pass

    def fire():
        pass

    def display(self, surf):
        pygame.draw.rect(surf , self.color, width=2)


