# import matplotlib.pyplot as plt
from activation import Activation
from node import Node

# activate = Activation()

# min_range = -10
# max_range = 10

# y = []
# x = []

# for i in range(0, max_range):
#     y.append(activate.Sigmoid(i))
#     x.append(i)
# for i in range(max_range, 0, -1):
#     y.append(activate.Sigmoid(i))
#     x.append(i)
# for i in range(0, min_range, -1):
#     y.append(activate.Sigmoid(i))
#     x.append(i)
# for i in range(min_range, 0):
#     y.append(activate.Sigmoid(i))
#     x.append(i)

# plt.plot(x, y)
# plt.show()


# inputs
X_L1_N1 = [1]
X_L1_N2 = [1]

# Layer 1
n_L1_N1 = Node("L1N1", X_L1_N1, Activation.Sigmoid)
n_L1_N2 = Node("L1N2", X_L1_N2, Activation.Sigmoid)


# Layer 2
# n_L2_N1 = Neuron("L2N1", , Activation.Sigmoid)

