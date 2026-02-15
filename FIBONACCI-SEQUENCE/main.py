import matplotlib.pyplot as plt

def generateFib(n: int) -> list[int]:
    seq = [None] * n
    seq[0] = 0
    seq[1] = 1
 
    for i in range(2, n):
        seq[i] = seq[i-2] + seq[i-1]

    return seq

def plotFib(seq: list[int]) -> None:
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
        seq = generateFib(n)
    except:
        print("AN ERROR OCCURED!")
    else:
        print("FIBONACCI SEQUENCE :")
        print(seq)
        plotFib(seq)

main(20)