import numpy as np

def pad_input(matrix, pad):
    if pad == 0:
        return matrix    
    return np.pad(matrix, ((pad, pad), (pad, pad)), mode='constant')

def convolve2d(input_matrix, kernel, stride=1, padding=0):
    kernel = np.flipud(np.fliplr(kernel))
    input_padded = pad_input(input_matrix, padding)
    kernel_ht, kernel_wd = kernel.shape
    input_ht, input_wd = input_padded.shape

    output_ht = (input_ht - kernel_ht) // stride + 1
    output_wd = (input_wd - kernel_wd) // stride + 1

    output = np.zeros((output_ht, output_wd))

    for y in range(output_ht):
        for x in range(output_wd):
            y_start = y * stride
            x_start = x * stride
            region = input_padded[y_start: y_start+kernel_ht, x_start: x_start+kernel_wd]
            output[y,x] = np.sum(region * kernel)

    return output

def max_pooling(input_matrix, pool_size=3, stride=1):
    input_ht, input_wd = input_matrix.shape
    out_ht = (input_ht - pool_size) // stride + 1
    out_wd = (input_wd - pool_size) // stride + 1

    pooled = np.zeros((out_ht, out_wd))

    for y in range(out_ht):
        for x in range(out_wd):
            y_start = y * stride
            x_start = x * stride
            region = input_matrix[y_start:y_start+pool_size, x_start:x_start+pool_size]
            pooled[y, x] = np.max(region)

    return pooled

# Example
input_matrix = np.array([
    [3, 1, 3, 13, 4],
    [2, 12, 3, 2, 12],
    [3, 9, 7, 12, 12],
    [2, 5, 11, 6, 3],
    [4, 12, 12, 9, 3]
])

kernel = np.array([
    [0, -1, 0],
    [-1, 3, -1],
    [0, -1, 0]
])

convolved_output = convolve2d(input_matrix, kernel, stride=1, padding=0)
print("Convolved Output:\n", convolved_output)

pooled_output = max_pooling(convolved_output, pool_size=3, stride=1)
print("\nPooled Output:\n", pooled_output)
