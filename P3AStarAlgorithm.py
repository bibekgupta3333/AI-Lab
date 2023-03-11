inputGraph = {
 'A': [('B', 7, 6), ('D', 8, 5)],
 'B': [('A', 7, 9), ('C', 9, 3)],
 'C': [('D', 5, 5), ('B', 9, 4)],
 'D': [('A', 5, 11), ('C', 5, 3)],
}

goal = "D"

def astar(graph, start):
    # Set initial root-to-parent cost to 0 and add start node to the priority queue
    rootToParentCost = 0
    queue = [start + (rootToParentCost, )]
    
    visitedNodes = []
    
    while queue:
        # Sort the queue based on the combined cost of the current node and the heuristic value
        queue = sorted(queue, key=lambda x: x[1] + x[2] + x[3])
        
        # Pop the node with the lowest combined cost and update the root-to-parent cost
        node = queue.pop(0)
        rootToParentCost = node[1] + node[3]
        
        if node not in visitedNodes:
            visitedNodes.append(node)
            if node[0] == goal:
                break
            neighbours = graph[node[0]]
            for neighbour in neighbours:
                # Calculate the heuristic value for the neighbour
                heuristic = neighbour[2]
                # Add the neighbour to the queue with its combined cost and root-to-parent cost
                queue.append(neighbour + (rootToParentCost, ))
    
    return visitedNodes

visitedNodes = astar(inputGraph, ('A', 5, 10))

print(visitedNodes)
