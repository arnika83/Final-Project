import math

def convolution_1d(signal, kernel):
    signal_length = len(signal)
    kernel_length = len(kernel)
    
    output_length = signal_length - kernel_length + 1
    
    output = [0] * output_length
    
    for i in range(output_length):
        for j in range(kernel_length):
            if 0 <= i + j < signal_length:
                output[i] += signal[i + j] * kernel[j]
         
    return output

def write_array_to_file(arr, filename):
    with open(filename, 'w') as f:
        for value in arr:
            f.write(str(value) + '\n')

# تولید سیگنال سینوسی
signal = [math.sin(2 * math.pi * 0.1 * i / 100) + math.sin(2 * math.pi * 0.01 * i / 100) for i in range(1, 1001)]

# کرنل‌ها
kernel_low_freq = [1, 0, 1]
kernel_high_freq = [1, -1, 1]

# اعمال کانولوشن
low_frq = convolution_1d(signal, kernel_low_freq)    
high_frq = convolution_1d(signal, kernel_high_freq)

# نوشتن خروجی به فایل
write_array_to_file(low_frq, "low_frequency_signal.txt")
write_array_to_file(high_frq, "high_frequency_signal.txt")

print("Recovered Low Frequency Signal saved to low_frequency_signal.txt")
print("Recovered High Frequency Signal saved to high_frequency_signal.txt")
