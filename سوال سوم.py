from PIL import Image
import matplotlib.pyplot as pl
def read_image(image_path):
    # Read the image using PIL and convert to grayscale
    image = Image.open(image_path).convert('L')
    # Convert image to a 2D list
    image_array = list(image.getdata())
    width, height = image.size
    image_array = [image_array[i * width:(i + 1) * width] for i in range(height)]
    return image_array

def convolution(image, kernel):
    # Get dimensions of the image and the kernel
    image_height, image_width = len(image), len(image[0])
    kernel_height, kernel_width = len(kernel), len(kernel[0])
    
    # Calculate the output size
    output_height = image_height - kernel_height + 1
    output_width = image_width - kernel_width + 1
    
    # Initialize the output image
    output_image = [[0] * output_width for _ in range(output_height)]
    
    # Perform convolution
    for i in range(output_height):
        for j in range(output_width):
            # Initialize the sum for the current position
            sum_val = 0
            for di in range(kernel_height):
                for dj in range(kernel_width):
                    # Multiply and accumulate the values
                    sum_val += image[i + di][j + dj] * kernel[di][dj]
            output_image[i][j] = sum_val
    
    return output_image

def write_array_to_file(arr, filename):
    with open(filename, 'w') as f:
        for row in arr:
            f.write(' '.join(map(str, row)) + '\n')

# Define the edge detection filter
edge_filter = [
    [1, 0, -1],
    [0, 0, 0],
    [-1, 0, 1]
]

# Provide the path to your image file
image_path = "C:/Users/Arnika/Desktop/logo.jpg"  
image = read_image(image_path)

# Perform convolution
convolved_image = convolution(image, edge_filter)

# Write the result to a file
write_array_to_file(image, "original_image_array.txt")
write_array_to_file(convolved_image, "edge_detected_image_array.txt")

pl.subplot(1, 2, 1)
pl.title("original image")
pl.imshow(image, cmap='gray')
pl.axis('off')
pl.subplot(1, 2, 2)
pl.title("edge detected image")
pl.imshow(convolved_image, cmap='gray')
pl.axis('off')
pl.show()