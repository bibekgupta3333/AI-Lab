# Define the graph as an adjacency list
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Define the DFS function
def dfs(graph, start, visited=None):
    # Initialize visited if it is None
    if visited is None:
        visited = set()
    # Mark the starting node as visited
    visited.add(start)
    print(start, end=' ')

    # For each adjacent node that has not been visited, call DFS recursively
    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Call the DFS function with the starting node
dfs(graph, 'A')
