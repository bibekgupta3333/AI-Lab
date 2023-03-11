from math import exp

# Define a function to calculate the output of the AND gate
def ANDGateCalculation(x1, x2):
    # Create a string to display the input and output of the AND gate
    stringLiteral = f"{x1} AND {x2} = "
    
    # Define the weights for the neural network
    weights = [-2, 1, 1]
    
    # Calculate the weighted sum of the inputs
    Z = weights[0] + x1 * weights[1] + x2 * weights[2]
    
    # Apply the sigmoid activation function to the weighted sum
    sigmoid_val = 1 / (1 + exp(-Z))
    
    # Print the result of the AND gate
    if sigmoid_val >= 0.5: 
        print(stringLiteral + "1")
    else: 
        print(stringLiteral + "0")
        
# Define a function to calculate the output of the OR gate
def ORGateCalculation(x1, x2):
    # Create a string to display the input and output of the OR gate
    stringLiteral = f"{x1} OR {x2} = "
    
    # Define the weights for the neural network
    weights = [-1, 2, 2]
    
    # Calculate the weighted sum of the inputs
    Z = weights[0] + x1 * weights[1] + x2 * weights[2]
    
    # Apply the sigmoid activation function to the weighted sum
    sigmoid_val = 1 / (1 + exp(-Z))
    
    # Print the result of the OR gate
    if sigmoid_val >= 0.5: 
        print(stringLiteral + "1")
    else: 
        print(stringLiteral + "0")

# Loop through all possible input combinations for the AND and OR gates
for x1 in range(2):
    for x2 in range(2):
        ORGateCalculation(x1,x2)
        ANDGateCalculation(x1,x2)
