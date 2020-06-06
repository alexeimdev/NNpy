from network import Network
from activation import Activation

network = Network()
network.add_input_layer(2)
network.add_hidden_layer(2, Activation.ReLU)
network.add_output_layer(1)
network.connect()
network.feed([1,2,3])
network.init()

# network.layers[1].

network.activate()

for layer in network.layers:
    print("Layer " + layer.id + " " + str(layer.type))