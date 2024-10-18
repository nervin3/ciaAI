graph_data = {
    'P': ['Q', 'R'],
    'Q': ['P', 'S'],
    'R': ['P', 'T'],
    'S': ['Q'],
    'T': ['R', 'U'],
    'U': ['T']
}

def depth_first_search(graph, start_node, target_node):
    stack = [(start_node, [start_node])]
    
    while stack:
        current_node, path = stack.pop()

        if current_node == target_node:
            return path

        for neighbor in graph[current_node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))

    return None

print("DFS Path:", depth_first_search(graph_data, 'P', 'U'))
