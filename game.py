import pygame

x = pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (72, 9, 150)
PINK = (239, 19, 221)
YELLOW = (250, 255, 0)
ORANGE = (255, 119, 0)

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ssslitherrr")

gameExit = False
while not gameExit:
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     gameExit = True
              

pygame.quit()
quit()
