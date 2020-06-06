class Node:
    def __init__(self, id, activation, output = 0):
        self.id = id
        self.activation = activation
        self.input_nodes = []
        self.output = output
    
    def activate(self):
        # self.output = 0 TODO: check next iteration after bp
        for input_node in self.input_nodes:
            self.output += input_node.output
        self.output = self.activation(self.output)
        print('Node ' + self.id + " " + str(self.output))
