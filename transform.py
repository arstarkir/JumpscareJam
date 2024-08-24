import sys
import pygame
import numpy as np

class Transform:
  mouseX = 0
  mouseY = 0
  
  def __init__(self, x, y):
    self.x = x
    self.y = y
  
  def __getitem__(self, index):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
          
  def __iter__(self):
        yield self.x
        yield self.y
          
  def isMoveNeeded(self, newMX,newMY):
    if(not ((newMX  -  self.mouseX)**2 + (newMY - self.mouseY)**2)**0.5 <= 100):
      self.mouseX, self.mouseY = newMX,newMY
      return False
    return True
