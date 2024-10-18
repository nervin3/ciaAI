from collections import deque

graph_data = {
    'X': {'Y': 2, 'Z': 3},
    'Y': {'W': 4, 'X': 2},
    'Z': {'W': 1, 'X': 3, 'V': 5},
    'W': {'Y': 4, 'Z': 1, 'G': 2},
    'V': {'Z': 5, 'G': 3},
    'G': {'W': 2, 'V': 3}
}

def breadth_first_search(graph, start_node, target_node):
    node_queue = deque([(start_node, [start_node], 0)])
    optimal_path = None
    lowest_cost = float('inf')

    while node_queue:
        current_node, path_so_far, accumulated_cost = node_queue.popleft()

        if current_node == target_node:
            if accumulated_cost < lowest_cost:
                lowest_cost = accumulated_cost
                optimal_path = path_so_far
            continue

        for adjacent_node, edge_cost in graph[current_node].items():
            if adjacent_node not in path_so_far:
                new_path = path_so_far + [adjacent_node]
                total_cost = accumulated_cost + edge_cost
                node_queue.append((adjacent_node, new_path, total_cost))

    if optimal_path is not None:
        print(f"Optimal BFS Path: {optimal_path} with total cost {lowest_cost}")
    else:
        print("No path found.")

    return optimal_path

breadth_first_search(graph_data, 'X', 'G')