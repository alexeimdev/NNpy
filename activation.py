import math


class Activation:

    def __init__(self):
        pass

    def Sigmoid(self, x):
        # TODO: need to bound range
        return 1 / (1 + math.exp(-x))

    def ReLU(self, x):
        return x if x > 0 else 0
