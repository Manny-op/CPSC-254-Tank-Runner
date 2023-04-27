import pygame

color = (0, 0, 225)

class Obstacule:
    def __init__(self, x, y, width, height, screen):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen = screen

    def draw(self, screen):
        pygame.draw.rect(screen, color, (self.x, self.y, self.width, self.height))

    def update(self, velocity, deltaTime):
        self.x -= velocity * deltaTime
    
    def checkOver(self):
        if self.x < -self.width:
            return True
        else:
            return False