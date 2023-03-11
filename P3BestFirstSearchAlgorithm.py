# Define the input graph and the goal node
inputGraph = {
 'A': [('B', 4), ('D', 12)],
 'B': [('A', 9), ('C', 4)],
 'C': [('D', 4), ('B', 7)],
 'D': [('A', 9), ('C', 5)]
}
goal = "C"

# Define the function for Best First Search algorithm
def gbfs(graph, start):
    # Create a queue with the start node and a list to store visited nodes
    queue = [start]
    visitedNode = []
    
    # Loop through the queue while it's not empty
    while queue:
        # Sort the queue based on the heuristic function
        queue = sorted(queue, key=lambda x: x[1])
        
        # Pop the first node from the queue
        node = queue.pop(0)
        
        # Check if the node has not already been visited
        if node not in visitedNode:
            visitedNode.append(node)
            
            # Check if the current node is the goal node
            if node[0] == goal:
                break
                
        # Get the neighbours of the current node and add them to the queue
        neighbours = graph[node[0]]
        for neighbour in neighbours:
            queue.append(neighbour)

    # Return the list of visited nodes
    return visitedNode

# Call the function with the input graph and the start node
print(gbfs(inputGraph, ("A", 13)))
