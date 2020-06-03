
import math

class Activation
  
  def __init__(self):
    pass

  def Sigmoid (self, x)
    return 1 / 1 + math.exp(-x)

  def ReLU (x):
    return x if x > 0 else 0
