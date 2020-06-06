from network import Network
from activation import Activation

network = Network()
network.feed([1,2,3])
network.add_layer(3, Activation.ReLU)
network.add_layer(3, Activation.ReLU)
network.add_layer(3, Activation.ReLU)
network.connect()
network.activate()