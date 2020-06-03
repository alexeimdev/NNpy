class Neuron:

    # def __init__(self, inputs, activation):
    def __init__(self, activation):
        self.inputs = [1, 2, 3, 4, 5]
        self.bias = 0.1
        self.weights = [2, 2, 2, 2, 2]
        self.activation = activation
        self.output = 0

    def activate(self):
        sum = 0
        for i in range(len(self.inputs)): 
            sum += self.inputs[i] * self.weights[i]
        result = sum + self.bias
        self.output = self.activation(result)