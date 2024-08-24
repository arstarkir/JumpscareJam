import sys
import pygame
import numpy as np

class Transform:
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