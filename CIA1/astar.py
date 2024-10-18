import heapq

graph_data = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}

heuristics = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}

def a_star_search(graph, start, goal, heuristics):
    priority_queue = [(0 + heuristics[start], 0, start, [start])]
    best_path = None
    min_cost = float('inf')
    visited = set()

    while priority_queue:
        estimated_cost, current_cost, current_node, path = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        if current_node == goal:
            if current_cost < min_cost:
                min_cost = current_cost
                best_path = path
            continue

        for neighbor, cost in graph[current_node].items():
            new_cost = current_cost + cost
            heapq.heappush(priority_queue, (new_cost + heuristics[neighbor], new_cost, neighbor, path + [neighbor]))

    print(f"A* Best Path: {best_path} with cost {min_cost}")
    return best_path

a_star_search(graph_data, 'S', 'G', heuristics)
