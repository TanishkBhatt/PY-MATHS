from numpy import linspace
import matplotlib.pyplot as plt

def plot_slope(m: float, b: float) -> None:
    x = linspace(-10, 10, 500)
    y = m*x + b

    plt.plot(x, y)
    plt.title("SLOPE OF LINE")
    plt.xlabel("X-AXIS")
    plt.ylabel("Y-AXIS")

    plt.grid()
    plt.show()

def main(m: float, b: float) -> None:
    print(f"EQUATION: y = {m}x + {b}")
    plot_slope(m, b)

main(2, 3)