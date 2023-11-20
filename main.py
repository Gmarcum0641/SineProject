import matplotlib.pyplot as plt
import numpy as np

def plotSine(freq = 1, time = 1, sampleRate = 1000):
    x = np.linspace(0, time, int(sampleRate * time), endpoint = False)
    y = np.sin(2 * np.pi * freq * x)
    plt.plot(x,y)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.title("Sine Wave")
    plt.show()

if __name__ == "__main__":
    plotSine()