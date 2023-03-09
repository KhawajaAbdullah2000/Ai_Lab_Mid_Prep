def DLS(graph, start_node, goal_node, max_depth):
    stack = [(start_node, 0)] #tuple represent node and its depth
    
    while stack:
        current_node, current_depth = stack.pop()
        
        if current_node == goal_node:
            return True
        
        if current_depth < max_depth:
            for neighbor in graph[current_node]:
                stack.append((neighbor, current_depth + 1))
                print(stack)
    
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

result = DLS(graph, start_node, goal_node, max_depth)

if result:
    print(f"{goal_node} found!")
else:
    print(f"{goal_node} not found within depth limit of {max_depth}.")