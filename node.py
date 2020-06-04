class Node:

    def __init__(self, id, input_nodes, activation):
        self.id = id
        self.input_nodes = input_nodes
        self.activation = activation
        self.bias = self.init_bias()
        self.weights = self.init_weights()
        self.output = 0

    def activate(self):
        sum = 0
        for i in range(len(self.input_nodes)):
            sum += self.input_nodes[i] * self.weights[i]
        result = sum + self.bias
        self.output = self.activation(result)

    def init_bias(self):
        return 0.1  # TODO: from rand

    def init_weights(self):
        initail_weights = []
        for i in range(len(self.input_nodes)):
            initail_weights.append(2)  # TODO: from rand
        return initail_weights
