from network import Network
from activation import Activation

network = Network()
network.add_input_layer(2)
network.add_hidden_layer(2, Activation.ReLU)
network.add_output_layer(1)
network.connect()
network.feed([1, 1])
network.init()

network.layers[1].nodes[0].weights[0] = -0.5
network.layers[1].nodes[0].weights[1] = 0.5
network.layers[1].nodes[1].weights[0] = -1
network.layers[1].nodes[1].weights[1] = -1

network.activate()

# for layer in network.layers:
#     print("Layer " + layer.id + " " + str(layer.type))