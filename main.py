from network import Network
from activation import Activation

network = Network()
network.add_input_layer(3)
network.add_hidden_layer(3, Activation.ReLU)
network.add_hidden_layer(3, Activation.ReLU)
network.add_hidden_layer(3, Activation.ReLU)
network.add_output_layer(3)
network.connect()
network.feed([1,2,3])
network.activate()

for layer in network.layers:
    print("Layer " + layer.id + " " + str(layer.type))