import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-10, 10, 400)

F = 3 * np.cos(2 * x + 1)
G = np.log(np.abs(np.cos(2 * x + 1)))
H = np.exp(np.cos(2 * x + 1))

plt.figure(figsize=(10, 6))

plt.plot(x, F, label='F(x) = 3cos(2x+1)', color='blue')
plt.plot(x, G, label='G(x) = ln(cos(2x+1))', color='green')
plt.plot(x, H, label='H(x) = exp(cos(2x+1))', color='red')

plt.title('Tracé des fonctions F(x), G(x) et H(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.grid(True)

plt.show()