import sys
import time
import pygame
from math import sin, cos

## Graphics Initialization
SIZE = (WIDTH, HEIGHT) = (1280, 720)
# Get the Surface for the main window.
screen = pygame.display.set_mode(SIZE)
# You could make it fullscreen by exchanging for this line!
# screen = pygame.display.set_mode(SIZE, pygame.FULLSCREEN)
pygame.display.set_caption("Dingus")
pd = pygame.draw
drawmode = 'stick'
pygame.init()

def draw_frame(screen):
  ball_y_offset = int(100 * sin(time.time()))
  ball_position = (WIDTH/4, HEIGHT/4 + ball_y_offset)

  # Clear the screen with white
  # The color is an RGB tuple
  # Look here for more crazy things to do with the screen Surface
  # http://www.pygame.org/docs/ref/surface.html
  screen.fill((255, 255, 255))

  # Draw some shapes
  # Look here for some more shapes to draw
  # http://www.pygame.org/docs/ref/draw.html

  # line(Surface, color, start_pos, end_pos, width=1) -> Rect
  pd.line(screen, (0, 100, 255), (20, 20), (140, 400), 2)
  # circle(Surface, color, pos, radius, width=0) -> Rect
  pd.circle(screen, (255, 100, 100), ball_position, 30)

def handle_events(events):
  for event in events:
    if event.type == pygame.QUIT:
      exit()
    elif event.type == pygame.KEYDOWN:
      if event.key == pygame.K_ESCAPE or event.unicode == 'q':
        exit()

def exit():
  print "Goodbye."
  pygame.quit()
  sys.exit()

## Main Loop
while True:
  handle_events(pygame.event.get())
  draw_frame(screen)

  # Switch the framebuffers, basically show everything
  # that has been drawn this frame.
  pygame.display.flip()
