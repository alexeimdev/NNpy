import math


class Activation:

    def __init__(self):
        pass

    @staticmethod
    def Sigmoid(x):
        # TODO: need to bound range
        return 1 / (1 + math.exp(-x))
        
    @staticmethod
    def ReLU(x):
        return x if x > 0 else 0
