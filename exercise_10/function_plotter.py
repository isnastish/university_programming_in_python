import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0.001, 5, 1000)
y = 5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

plt.figure(figsize=(10, 6))
plt.plot(
    x,
    y,
    linewidth=2.5,
    color="blue",
    label="Y(x) = 5*cos(10*x)*sin(3*x)/√x",
    linestyle="-",
)

plt.xlabel("x", fontsize=12)
plt.ylabel("Y(x)", fontsize=12)
plt.title("Graph of Y(x) = 5*cos(10*x)*sin(3*x)/√x", fontsize=14, fontweight="bold")
plt.grid(True, alpha=0.3)
plt.legend(loc="best", fontsize=10)

plt.xlim(0, 5)
plt.tight_layout()
plt.show()
