import sys
import pygame
import numpy as np
from transform import Transform

pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()

width, height = 500, 500
screen = pygame.display.set_mode((width, height))

def mirror_point(px, py, ax, ay, bx, by):
    # Line vector
    lx, ly = bx - ax, by - ay
    # Normalize line vector
    len_line = (lx**2 + ly**2)**0.5
    lx, ly = lx / len_line, ly / len_line
    # Point vector
    px, py = px - ax, py - ay
    # Project point vector onto line vector
    dot = px * lx + py * ly
    proj_x, proj_y = dot * lx, dot * ly
    # Reflection vector
    rx, ry = proj_x - px, proj_y - py
    return ax + proj_x + rx, ay + proj_y + ry

def mirror_joint(joint):
  mirror_start = (crabPos.x + 50, crabPos.y)
  mirror_end = (crabPos.x + 50, crabPos.y + 50)
  return Transform(*mirror_point(joint.x, joint.y, *mirror_start, *mirror_end))
  
crabColor = (202,0,0)
crabAJ1Color= (250,0,0)
crabAJ2Color= (220,0,0)

while True:
  screen.fill((236, 204, 162))
  
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      pygame.quit()
      sys.exit()
  
  mouseX, mouseY = pygame.mouse.get_pos() 
  crabPos = Transform(mouseX, mouseY)
  crabE1 = Transform(crabPos.x + 10,crabPos.y -35)
  crabEP1 = Transform(crabE1.x + 10, crabE1.y + 5)
  crabE2 = Transform(crabPos.x + 60,crabPos.y -35)
  crabEP2 = Transform(crabE2.x + 10, crabE2.y + 5)
  crabA1J1S = Transform(crabPos.x + 10,crabPos.y + 25)
  crabA1J1E = Transform(crabA1J1S.x -50,crabA1J1S.y + 20)
  crabA1J2S = crabA1J1E
  crabA1J2E = Transform(crabA1J2S.x -50,crabA1J2S.y-20)
  
  crabA2J1S = Transform(crabPos.x + 10,crabPos.y + 50)
  crabA2J1E = Transform(crabA2J1S.x -50,crabA2J1S.y + 20)
  crabA2J2S = crabA2J1E
  crabA2J2E = Transform(crabA2J2S.x -50,crabA2J2S.y-20)
  
  crabA3J1S = Transform(crabPos.x + 10,crabPos.y + 75)
  crabA3J1E = Transform(crabA3J1S.x -50,crabA3J1S.y + 20)
  crabA3J2S = crabA3J1E
  crabA3J2E = Transform(crabA3J2S.x -50,crabA3J2S.y-20)
  
  pygame.draw.rect(screen, crabColor, (*crabPos,100,100), width=5)
        
  pygame.draw.rect(screen, (180,0,6), (*crabPos ,95,95))
  
  pygame.draw.rect(screen, (255,255,255), (*crabE1,20,50))
  pygame.draw.rect(screen, (0,0,0), ( crabEP1.x,crabEP1.y,10,10))
  pygame.draw.rect(screen, (255,255,255), (crabE2.x,crabE2.y,20,50))
  pygame.draw.rect(screen, (0,0,0), (crabEP2.x,crabEP2.y,10,10))
  
  pygame.draw.line(screen, crabAJ1Color, (crabA1J1S.x,crabA1J1S.y),(crabA1J1E.x,crabA1J1E.y),width = 8)
  pygame.draw.line(screen, crabAJ2Color, (crabA1J2S.x,crabA1J2S.y),(crabA1J2E.x,crabA1J2E.y),width = 8)
  
  pygame.draw.line(screen, crabAJ1Color, (crabA2J1S.x,crabA2J1S.y),(crabA2J1E.x,crabA2J1E.y),width = 8)
  pygame.draw.line(screen, crabAJ2Color, (crabA2J2S.x,crabA2J2S.y),(crabA2J2E.x,crabA2J2E.y),width = 8)
  
  pygame.draw.line(screen, crabAJ1Color, (crabA3J1S.x,crabA3J1S.y),(crabA3J1E.x,crabA3J1E.y),width = 8)
  pygame.draw.line(screen, crabAJ2Color, (crabA3J2S.x,crabA3J2S.y),(crabA3J2E.x,crabA3J2E.y),width = 8)
  
  crabA1J1S_mirrored = mirror_joint(crabA1J1S)
  crabA1J1E_mirrored = mirror_joint(crabA1J1E)
  crabA1J2S_mirrored = mirror_joint(crabA1J2S)
  crabA1J2E_mirrored = mirror_joint(crabA1J2E)

  crabA2J1S_mirrored = mirror_joint(crabA2J1S)
  crabA2J1E_mirrored = mirror_joint(crabA2J1E)
  crabA2J2S_mirrored = mirror_joint(crabA2J2S)
  crabA2J2E_mirrored = mirror_joint(crabA2J2E)

  crabA3J1S_mirrored = mirror_joint(crabA3J1S)
  crabA3J1E_mirrored = mirror_joint(crabA3J1E)
  crabA3J2S_mirrored = mirror_joint(crabA3J2S)
  crabA3J2E_mirrored = mirror_joint(crabA3J2E)
  
  pygame.draw.line(screen, crabAJ1Color, (crabA1J1S_mirrored.x,crabA1J1S_mirrored.y),(crabA1J1E_mirrored.x,crabA1J1E_mirrored.y),width = 8)
  pygame.draw.line(screen, crabAJ2Color, (crabA1J2S_mirrored.x,crabA1J2S_mirrored.y),(crabA1J2E_mirrored.x,crabA1J2E_mirrored.y),width = 8)
  
  pygame.draw.line(screen, crabAJ1Color, (crabA2J1S_mirrored.x,crabA2J1S_mirrored.y),(crabA2J1E_mirrored.x,crabA2J1E_mirrored.y),width = 8)
  pygame.draw.line(screen, crabAJ2Color, (crabA2J2S_mirrored.x,crabA2J2S_mirrored.y),(crabA2J2E_mirrored.x,crabA2J2E_mirrored.y),width = 8)
  
  pygame.draw.line(screen, crabAJ1Color, (crabA3J1S_mirrored.x,crabA3J1S_mirrored.y),(crabA3J1E_mirrored.x,crabA3J1E_mirrored.y),width = 8)
  pygame.draw.line(screen, crabAJ2Color, (crabA3J2S_mirrored.x,crabA3J2S_mirrored.y),(crabA3J2E_mirrored.x,crabA3J2E_mirrored.y),width = 8)
  
  
  pygame.display.flip()
  fpsClock.tick(fps)
  

