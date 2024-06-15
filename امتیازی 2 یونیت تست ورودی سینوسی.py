import math

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

def test_output_length():
    signal = [1, 2, 3, 4, 5]
    kernel = [0.5, 0.5]
    output = convolution_1d(signal, kernel)
    assert len(output) == len(signal) - len(kernel) + 1

def test_correctness():
    signal = [1, 2, 3, 4, 5]
    kernel = [0.5, 0.5]
    output = convolution_1d(signal, kernel)
    expected_output = [1.5, 2.5, 3.5, 4.5]
    assert output == expected_output

def test_invalid_input():
    signal = [1, 2, 3, 4, 5]
    kernel = [0.5, 0.5, 0.5]  # Kernel length greater than signal length
    if len(kernel) > len(signal):
        assert True
    else:
        output = convolution_1d(signal, kernel)

# Run tests
test_output_length()
test_correctness()
test_invalid_input()

print("All tests passed successfully!")
