import math

class Activation:
    def __init__(self):
        pass

    @staticmethod
    def PassThrough(x):
        return x

    @staticmethod
    def Step(x):
        return 1 if x > 0 else 0 # TODO: change 1 value
        
    @staticmethod
    def ReLU(x):
        return x if x > 0 else 0

    @staticmethod
    def Sigmoid(x):
        return 1 / (1 + math.exp(-x)) # TODO: need to bound range

