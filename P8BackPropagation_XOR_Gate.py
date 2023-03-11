import numpy as np
X = np.array([[0, 0],
              [0, 1],
              [1, 0],
              [1, 1]])
y = np.array([[0],
              [1],
              [1],
              [0]])
input_layer_size = 2
hidden_layer_size = 2
output_layer_size = 1

# Initialize weights randomly
W1 = np.random.randn(input_layer_size, hidden_layer_size)
W2 = np.random.randn(hidden_layer_size, output_layer_size)

learning_rate = 0.1
num_iterations = 10000

for i in range(num_iterations):
    # Forward propagation
    hidden_layer = 1 / (1 + np.exp(-(np.dot(X, W1))))
    output_layer = 1 / (1 + np.exp(-(np.dot(hidden_layer, W2))))

    # Backward propagation
    output_layer_error = y - output_layer
    output_layer_delta = output_layer_error * output_layer * (1 - output_layer)

    hidden_layer_error = np.dot(output_layer_delta, W2.T)
    hidden_layer_delta = hidden_layer_error * hidden_layer * (1 - hidden_layer)

    # Update weights
    W2 += learning_rate * np.dot(hidden_layer.T, output_layer_delta)
    W1 += learning_rate * np.dot(X.T, hidden_layer_delta)
    
hidden_layer = 1 / (1 + np.exp(-(np.dot(X, W1))))
predicted_output = 1 / (1 + np.exp(-(np.dot(hidden_layer, W2))))
print(predicted_output.round())
