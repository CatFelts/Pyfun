import pygame

x = pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 30)

#color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
PURPLE = (72, 9, 150)
PINK = (239, 19, 221)
YELLOW = (250, 255, 0)
ORANGE = (255, 119, 0)

#FPS
FRAMERATE = 120

clock = pygame.time.Clock()

gameover_text = my_font.render("GAME OVER", False, RED)

game_display = pygame.display.set_mode((800, 600))
pygame.display.set_caption("ssslitherrr")

head_x = 300
x_change = 0
head_y = 200
y_change = 0

#game loop
game_over = False
game_exit = False
while not game_over and not game_exit:
       #event handling
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     game_exit = True
              if event.type == pygame.KEYDOWN:
                     if event.key == pygame.K_LEFT:
                            x_change = -3
                            y_change = 0
                            print("left arrow button pressed")
                     if event.key == pygame.K_RIGHT:
                            x_change = 3
                            y_change = 0
                            print("right arrow button pressed")
                     if event.key == pygame.K_UP:
                            y_change = -3
                            x_change = 0
                            print("up arrow button pressed")
                     if event.key == pygame.K_DOWN:
                            y_change = 3
                            x_change = 0
                            print("down arrow button pressed")

       head_x = head_x + x_change
       head_y = head_y + y_change

       if head_x <=0 or head_x >= 800:
              game_over = True
       if head_y <=0 or head_y >= 600:
              game_over = True
       
       #draws
       game_display.fill(WHITE)
       pygame.draw.rect(game_display, GREEN, [head_x, head_y, 10, 10])
       pygame.display.flip()
       clock.tick(FRAMERATE)

       
while not game_exit:              
       for event in pygame.event.get():
              if event.type == pygame.QUIT:
                     game_exit = True
       game_display.fill(BLACK)
       game_display.blit(gameover_text, (300, 300))
       pygame.display.flip()
       clock.tick(FRAMERATE)

pygame.quit()
quit()
