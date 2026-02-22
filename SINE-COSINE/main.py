import matplotlib.pyplot as plt
from numpy import linspace, sin, cos

x = linspace(-10, 10, 500)
y = sin(x)
z = cos(x)

plt.plot(x, y, label="SINE")
plt.plot(x, z, label="COSINE")
plt.title("SINE AND COSINE")

plt.xlabel("X-AXIS")
plt.ylabel("Y-AXIS")

plt.grid()
plt.legend()
plt.show()