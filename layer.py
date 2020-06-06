from enum import Enum

class Layer:
    def __init__(self, type, id, nodes, activation):
        self.type = type
        self.id = id
        self.nodes = nodes
        self.activation = activation


class LayerType(Enum):
    INPUT = 1
    HIDDEN = 2
    OUTPUT = 3
