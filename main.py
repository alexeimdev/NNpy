import matplotlib.pyplot as plt
from activation import Activation

active = Activation()

min_range = -10
max_range = 10

y = []
x = []

for i in range(0, max_range):
    y.append(active.Sigmoid(i))
    x.append(i)
for i in range(max_range, 0, -1):
    y.append(active.Sigmoid(i))
    x.append(i)
for i in range(0, min_range, -1):
    y.append(active.Sigmoid(i))
    x.append(i)
for i in range(min_range, 0):
    y.append(active.Sigmoid(i))
    x.append(i)

plt.plot(x, y)
plt.show()
