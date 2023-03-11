from queue import Queue

# Define the graph as a dictionary of lists
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Define the BFS function
def bfs(graph, start):
    visited = set()         # Set to keep track of visited nodes
    queue = Queue()         # Initialize a queue to store nodes to visit
    queue.put(start)        # Add start node to queue

    while not queue.empty():
        node = queue.get()  # Get the next node from the queue
        if node not in visited:
            print(node)     # Visit the node
            visited.add(node)
            for neighbor in graph[node]:  # Add unvisited neighbors to queue
                if neighbor not in visited:
                    queue.put(neighbor)

# Test the BFS function with graph starting at 'A'
bfs(graph, 'A')
