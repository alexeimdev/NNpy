from layer import Layer, LayerType
from node import Node
from activation import Activation

class Network:
    def __init__(self):
        self.layers = []

    # public
    def add_input_layer(self, num_of_nodes):
        input_layer = self.__generate_layer(LayerType.INPUT, num_of_nodes, Activation.PassThrough)
        self.layers.append(input_layer)

    def add_hidden_layer(self, num_of_nodes, activation):
        hidden_layer = self.__generate_layer(LayerType.HIDDEN, num_of_nodes, activation)
        self.layers.append(hidden_layer)

    def add_output_layer(self, num_of_nodes):
        output_layer = self.__generate_layer(LayerType.OUTPUT, num_of_nodes, Activation.PassThrough)
        self.layers.append(output_layer)

    def connect(self):
        self.__fully_connect(self.layers)

    def feed(self, inputs):
        input_layer = next((x for x in self.layers if x.type == LayerType.INPUT), None)
        if (len(input_layer.nodes) != len(inputs)):
            raise ValueError
        else:
            for i in range(len(input_layer.nodes)):
              input_layer.nodes[i].output = inputs[i]   

    def activate(self):
        for layer in self.layers:
            self.__activate_layer(layer)

    # private
    def __generate_layer(self, layer_type, num_of_nodes, activation):
        layer_num = len(self.layers)
        nodes = []
        output = 0
        for i in range(num_of_nodes):
            node = self.__generate_node(layer_num, i, activation)
            nodes.append(node)

        layer_id = 'L' + str(layer_num)
        new_layer = Layer(layer_type, layer_id, nodes, activation)
        return new_layer

    # private static
    @staticmethod
    def __generate_node(layer_id, node_index, activation):
        node_id = 'L' + str(layer_id) +'_N' + str(node_index)
        node = Node(node_id, activation)
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

