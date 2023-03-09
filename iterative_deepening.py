def IDS(graph, start_node, goal_node, max_depth):
    for depth in range(max_depth):
        visited = set()
        stack = [(start_node, 0)]
        
        while stack:
            current_node, current_depth = stack.pop()
            
            if current_node == goal_node:
                return True
            
            if current_depth < depth:
                if current_node not in visited:
                    visited.add(current_node)
                    for neighbor in graph[current_node]:
                        stack.append((neighbor, current_depth + 1))
                    
    return False

graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

start_node = 'A'
goal_node = 'F'
max_depth = 3

result = IDS(graph, start_node, goal_node, max_depth)

if result:
    print(f"{goal_node} found!")
else:
    print(f"{goal_node} not found within depth limit of {max_depth}.")
