import math
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def convolution_1d(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    output_length = signal_length - kernel_length + 1
    output = [0] * output_length
    for i in range(output_length):
        for j in range(kernel_length):
            if 0 <= i - j < signal_length:
                output[i] += signal[i + j] * kernel[j]
    return output

def plot_signals():
    signal = []
    for i in range(1, 1001):
        signal.append(math.sin(2 * math.pi * 0.1 * i / 100) + math.sin(2 * math.pi * 0.01 * i / 100))

    kernel_low_freq = [1, 0, 1]
    kernel_high_freq = [1, -1, 1]

    low_freq = convolution_1d(signal, kernel_low_freq)
    high_freq = convolution_1d(signal, kernel_high_freq)

    fig, (ax1, ax2, ax3) = plt.subplots(3, 1)

    ax1.plot(signal)
    ax1.set_title('Original Signal')

    ax2.plot(low_freq)
    ax2.set_title('Recovered Low Frequency Signal')

    ax3.plot(high_freq)
    ax3.set_title('Recovered High Frequency Signal')

    canvas = FigureCanvasTkAgg(fig, master=window)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

window = tk.Tk()
window.title("Signal Processing GUI")

plot_button = ttk.Button(window, text="Plot Signals", command=plot_signals)
plot_button.pack()

window.mainloop()
