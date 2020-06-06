class Node:
    def __init__(self, id, activation):
        self.id = id
        self.activation = activation
        self.input_nodes = []
        self.weights = []
        self.output = 0
    
    def init_weights(self):
        for i in range(len(self.input_nodes)):
            self.weights.append(1) # TODO: rand

    def activate(self):
        # self.output = 0 TODO: check next iteration after bp
        for i in range(len(self.input_nodes)):
            self.output += (self.input_nodes[i].output * self.weights[i])
            self.output = self.activation(self.output)
        print('Node ' + self.id + " " + str(self.output))
