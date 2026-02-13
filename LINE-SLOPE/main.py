from numpy import linspace
import matplotlib.pyplot as plt

def plotSlope(m: float, b: float) -> None:
    """PLOTTING y = mx + b"""
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
    plotSlope(m, b)

main(2, 3)