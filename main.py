import sys
import pygame
import numpy as np

pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 500, 500
screen = pygame.display.set_mode((width, height))
 
while True:
  screen.fill((0, 0, 0))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  pygame.display.flip()
  fpsClock.tick(fps)