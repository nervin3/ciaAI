import itertools

graph_data = {
    'X': {'Y': 2, 'Z': 4},
    'Y': {'X': 2, 'A': 1},
    'Z': {'X': 4, 'B': 3},
    'A': {'Y': 1, 'C': 5},
    'B': {'Z': 3, 'C': 2},
    'C': {'A': 5, 'B': 2}
}

def alternative_search(graph, start, goal):
    all_routes = []

    def traverse(node, visited, route):
        if node == goal:
            all_routes.append(route + [node])
            return
        for neighbor in graph.get(node, {}):
            if neighbor not in visited:
                traverse(neighbor, visited + [neighbor], route + [node])

    traverse(start, [], [])

    optimal_route = None
    minimum_cost = float('inf')

    for route in all_routes:
        cost = sum(graph[route[i]][route[i + 1]] for i in range(len(route) - 1))
        if cost < minimum_cost:
            minimum_cost = cost
            optimal_route = route

    print(f"Optimal Path: {optimal_route} with cost {minimum_cost}")
    return optimal_route

alternative_search(graph_data, 'X', 'C')
