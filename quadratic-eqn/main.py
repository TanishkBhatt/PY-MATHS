from numpy import linspace
import matplotlib.pyplot as plt

def solve_quad(a: float, b: float, c: float) -> tuple[float, float]:
    D = (b*b) - (4*a*c)

    if a == 0:
        raise Exception("NOT A QUADRATUC EQUATION!")
    if D < 0:
        raise Exception("NO REAL ROOTS EXISTS!")
    
    D = D**0.5
    return (-b + D) / (2*a), (-b - D) / (2*a)

def plot_quad(a: float, b: float, c: float) -> None:
    x = linspace(-10, 10, 500)
    y = a*(x**2) + (b*x) + c

    plt.plot(x, y)
    plt.title("QUADRATIC EQUATIONS")
    plt.xlabel("X-AXIS")
    plt.ylabel("Y-AXIS")

    plt.grid()
    plt.show()

def main(a: float, b: float, c: float) -> None:
    try:
        res = solve_quad(a, b, c)
    except Exception as e:
        print(e)
    else:
        print(f"EQUATION: {a}x**2 + {b}x + {c} = 0")
        print(f"SOLUTIONS: {res[0]} & {res[1]}")
        plot_quad(a, b, c)

main(2, 5, 2)