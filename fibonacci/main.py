import matplotlib.pyplot as plt

def generate_fib(n: int) -> list[int]:
    seq = [None] * n
    seq[0] = 0
    seq[1] = 1
 
    for i in range(2, n):
        seq[i] = seq[i-2] + seq[i-1]

    return seq

def plot_fib(seq: list[int]) -> None:
    x = [i for i in range(len(seq))]
    y = seq

    plt.plot(x, y)
    plt.title("FIBONACCI SEQUENCE")
    plt.xlabel("X-AXIS")
    plt.ylabel("Y-AXIS")
    plt.grid()
    plt.show()

def main(n: int) -> None:
    try:
        seq = generate_fib(n)
    except:
        print("AN ERROR OCCURED!")
    else:
        print("FIBONACCI SEQUENCE :")
        print(seq)
        plot_fib(seq)

main(20)