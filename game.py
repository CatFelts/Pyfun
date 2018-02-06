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
FRAMERATE = 30

#screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

#start position
START_X = SCREEN_WIDTH/2
START_Y = SCREEN_HEIGHT/2

HEAD_SIZE = 10

clock = pygame.time.Clock()

#gameover screen
gameover_text = my_font.render("GAME OVER", False, RED)
restart_text = my_font.render("Would you like to start a new game?", False, RED)
yes_or_no_text = my_font.render("(Press Y for yes or N for n)", False, RED)

#game window
game_display = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("ssslitherrr")



def restart_game():
       global game_over
       global head_x
       global head_y
       global x_change
       global y_change
       game_over = False
       head_x = START_X
       x_change = 0
       head_y = START_Y
       y_change = 0

#game loop
restart_game()
game_over = False
game_exit = False
paused = False
while not game_over and not game_exit:
       #event handling
       for event in pygame.event.get():
              #quit
              if event.type == pygame.QUIT:
                     game_exit = True
              #keyboard input from user
              if event.type == pygame.KEYDOWN:
                     #arrow keys for movement
                     if not paused:
                            if event.key == pygame.K_LEFT:
                                   x_change = -HEAD_SIZE
                                   y_change = 0
                                   print("left arrow button pressed")
                            elif event.key == pygame.K_RIGHT:
                                   x_change = HEAD_SIZE
                                   y_change = 0
                                   print("right arrow button pressed")
                            elif event.key == pygame.K_UP:
                                   y_change = -HEAD_SIZE
                                   x_change = 0
                                   print("up arrow button pressed")
                            elif event.key == pygame.K_DOWN:
                                   y_change = HEAD_SIZE
                                   x_change = 0
                                   print("down arrow button pressed")
                     #other keys for game controls
                     #pause button is 'P'
                     if event.key == pygame.K_p:
                            paused = not paused
                            if paused == True: #if the user just paused the game, save the game state
                                   saved_x_change = x_change
                                   saved_y_change = y_change
                                   x_change = 0
                                   y_change = 0
                            if paused == False: #if the user just unpaused the game, restore game state
                                   x_change = saved_x_change
                                   y_change = saved_y_change
                     if event.key == pygame.K_ESCAPE:
                            game_exit = True
                            
                                   

       head_x = head_x + x_change
       head_y = head_y + y_change
       
       #if the head hits the edges, game over
       if head_x <=0 or head_x >= SCREEN_WIDTH or head_y <= 0 or head_y >= SCREEN_HEIGHT:
              game_over = True
       
       #draws
       game_display.fill(WHITE)
       pygame.draw.rect(game_display, GREEN, [head_x, head_y, HEAD_SIZE, HEAD_SIZE])
       pygame.display.update()
       clock.tick(FRAMERATE)

       
       while game_over and not game_exit:
              #debugging prints
              print("game over screen")
              print("head_x = %d" % (head_x))
              print("head_y = %d" % (head_y))
              print("x_change = %d" % (x_change))
              print("y_change = %d" % (y_change))
              #game over screen event handler
              for event in pygame.event.get():
                     if event.type == pygame.QUIT:
                            game_exit = True
                     #if 'Y' key pressed, restart game
                     if event.type == pygame.KEYDOWN:
                            if event.key == pygame.K_y:
                                   game_over = False
                                   restart_game()
                            if event.key == pygame.K_n:
                                   game_exit = True

              #draws
              game_display.fill(BLACK)
              game_display.blit(gameover_text, (300, 150))
              game_display.blit(restart_text, (150, 300))
              game_display.blit(yes_or_no_text, (200, 500))
              pygame.display.flip()
              clock.tick(FRAMERATE)

pygame.quit()
quit()
