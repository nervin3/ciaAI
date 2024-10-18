import random

graph_data = {
    'A': {'B': 2, 'C': 3},
    'B': {'A': 2, 'D': 4, 'E': 1},
    'C': {'A': 3, 'F': 5},
    'D': {'B': 4},
    'E': {'B': 1, 'F': 2},
    'F': {'C': 5, 'E': 2}
}

heuristic_data = {
    'A': 5,
    'B': 3,
    'C': 4,
    'D': 2,
    'E': 1,
    'F': 0
}

def find_best_neighbor(node, graph, heuristic):
    best_neighbor = None
    best_score = float('inf')
    
    for neighbor, cost in graph[node].items():
        score = cost + heuristic[neighbor]
        if score < best_score:
            best_score = score
            best_neighbor = neighbor
            
    return best_neighbor

def hill_climbing(graph, start, goal, heuristic):
    current = start
    path = [current]
    total_cost = 0
    
    while current != goal:
        next_node = find_best_neighbor(current, graph, heuristic)
        if next_node is None:
            break
        path.append(next_node)
        total_cost += graph[current][next_node]
        current = next_node
    
    print(f"Hill Climbing Best Path: {path} with cost {total_cost}")
    return path

hill_climbing(graph_data, 'A', 'F', heuristic_data)
