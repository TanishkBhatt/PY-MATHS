from numpy import linspace
import matplotlib.pyplot as plt

def solution(a1: float, b1: float, c1: float, a2: float, b2: float, c2:float) -> tuple[float, float]:
    """SOLVING LINEAR EQN IN TWO VARIABLES"""
    D = (a1*b2) - (a2*b1)
    dx = ((c1*b2) - (c2*b1)) 
    dy = ((a1*c2) - (a2*c1)) 

    if D == 0:
        if dx == 0 and dy == 0:
            raise ValueError("DEPENDENT PAIR! INFINITE SOLUTIONS")
        else:
            raise ValueError("INCONSISTENT PAIR! NO SOLUTION")

    x = dx / D
    y = dy / D

    return x, y

def plotting(a1: float, b1: float, c1: float, a2: float, b2: float, c2:float) -> None:
    """PLOTTING LINEAR EQN"""
    x = linspace(-10, 10, 500)
    y1 = (c1 - (a1*x)) / b1
    y2 = (c2 - (a2*x)) / b2

    plt.plot(x, y1)
    plt.plot(x, y2)
    plt.title("LINEAR EQN IN TWO VARIABLES")
    plt.xlabel("X-AXIS")
    plt.ylabel("Y-AXIS")

    plt.grid()
    plt.show()

def main(a1: float, b1: float, c1: float, a2: float, b2: float, c2:float) -> None:
    try:
        res = solution(a1, b1, c1, a2, b2, c2)
    except Exception as e:
        print(e)
    else:
        print(f"EQN-I : {a1}x + {b1}y + {c1} = 0\nEQN-II : {a2}x + {b2}y + {c2} = 0")
        print(f"SOLUTIONS : {res[0]} AND {res[1]}")
        plotting(a1, b1, c1, a2, b2, c2)

main(2, 3, -13, 1, -1, -1)