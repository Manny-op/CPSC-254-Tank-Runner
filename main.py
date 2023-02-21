import pygame

#   set background color 
background_color = (156, 167, 184)
#   create a screen size and name the window
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Tank Runner")

#   fill the background with the background color
screen.fill(background_color)

pygame.init()

#   update the game using the flip function

pygame.display.flip()

#   variable to keep track of the game state being running

running = True
# game loop
while running:
    
# for loop through the event queue  
    for event in pygame.event.get():
      
        # Check for QUIT event      
        if event.type == pygame.QUIT:
            running = False