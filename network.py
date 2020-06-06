from layer import Layer
from node import Node
from activation import Activation

class Network:
    def __init__(self):
        self.layers = []

    # public
    def add_layer(self, num_of_nodes, activation, outputs = []):
        new_layer = self.__generate_layer(num_of_nodes, activation, outputs)
        self.layers.append(new_layer)

    def connect(self):
        self.__fully_connect(self.layers)

    def feed(self, inputs):
        self.add_layer(len(inputs), Activation.PassThrough, inputs)

    def activate(self):
        for layer in self.layers:
            self.__activate_layer(layer)

    # private
    def __generate_layer(self, num_of_nodes, activation, outputs = []):
        layer_num = len(self.layers)
        nodes = []
        for i in range(num_of_nodes):
            output = outputs[i] if len(outputs) > 0 else 0
            node = self.__generate_node(layer_num, i, activation, output)
            nodes.append(node)

        layer_id = 'L' + str(layer_num)
        new_layer = Layer(layer_id, nodes, activation)
        return new_layer

    # private static
    @staticmethod
    def __generate_node(layer_id, node_index, activation, output = None):
        node_id = 'L' + str(layer_id) +'_N' + str(node_index)
        node = Node(node_id, activation, output)
        return node

    @staticmethod
    def __fully_connect(layers):
        num_of_layers = len(layers)
        for i in range(num_of_layers - 1, 0, -1):
            if (i > 0):
                curr_layer = layers[i]
                prev_layer = layers[i - 1]
                for curr_node in curr_layer.nodes:
                    for prev_node in prev_layer.nodes:
                        curr_node.input_nodes.append(prev_node)   

    @staticmethod
    def __activate_layer(layer):
        for node in layer.nodes:
            node.activate()

