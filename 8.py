import matplotlib.pyplot as plt
import numpy as np

def graph()

x = np.linspace(0, 10, 50)
y = x**2
plt.title("f(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.plot(x, y, 'r')
plt.show()