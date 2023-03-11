# Define the function to solve the water jug problem
def waterJugSolution(xCapacity, yCapacity, target, reverse=False):
    
    # Initialize the path to store the solution
    path = [[0, 0]]
    
    # Initialize the capacities of the jugs
    y = yCapacity
    x = 0
    
    # Add the initial state to the path
    path.append([x, y])
    
    # Initialize the number of steps
    steps = 1
    
    # Keep filling and emptying jugs until the target is reached
    while ((y != target) and (x != target)):
        
        # Calculate the amount to transfer
        temp = min(y, xCapacity - x)
        
        # Transfer the water
        x = x + temp
        y = y - temp
        
        # Add the new state to the path
        path.append([x, y])
        
        # Increment the step counter
        steps = steps + 1
        
        # Check if the target is reached
        if ((y == target) or (x == target)):
            break
        
        # If jug 2 is empty, fill it
        if y == 0:
            y = yCapacity
            path.append([x, y])
            steps = steps + 1
        
        # If jug 1 is full, empty it
        if x == xCapacity:
            x = 0
            path.append([x, y])
            steps = steps + 1
    
    # Reverse the path if required
    if reverse:
        path = [[y, x] for x, y in path]
    
    # Return the path and number of steps taken
    return [path, steps]
    
# Take input from user for jug capacities and target volume
xCapacity = int(input("Jug 1= "))
yCapacity = int(input("Jug 2= "))
target = int(input("Target vol = "))

# Define a function to calculate the GCD of two numbers
def solveGCD(a, b):
    if b == 0:
        return a
    return solveGCD(b, a % b)

# Check if the target volume is reachable
if target % solveGCD(xCapacity, yCapacity) == 0:
    
    # Calculate the solution using both jugs
    path1, step1 = waterJugSolution(xCapacity, yCapacity, target, reverse=False)
    
    # Calculate the solution using the jugs in reverse order
    path2, step2 = waterJugSolution(yCapacity, xCapacity, target, reverse=True)
    
    # Compare the number of steps taken and print the solution with minimum steps
    if step1 <= step2:
        print("The path is:", path1)
        print("The steps are:", step1)
    else:
        print("The path is:", path2)
        print("The steps are:", step2)
        
else:
    print("Solution failed")
