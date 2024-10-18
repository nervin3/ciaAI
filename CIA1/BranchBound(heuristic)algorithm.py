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

heuristic_data = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}

def heuristic_branch_bound(data, start_node, end_node, heuristics):
    open_set = [(heuristics[start_node], 0, start_node, [start_node])]
    best_route = None
    least_cost = float('inf')

    while open_set:
        est_total_cost, actual_cost, current, route = heapq.heappop(open_set)

        if current == end_node:
            if actual_cost < least_cost:
                least_cost = actual_cost
                best_route = route
            continue

        for neighbor, travel_cost in data[current].items():
            if neighbor not in route:
                new_cost = actual_cost + travel_cost
                estimated_cost = new_cost + heuristics[neighbor]
                heapq.heappush(open_set, (estimated_cost, new_cost, neighbor, route + [neighbor]))

    print(f"Best Route Found: {best_route} with total cost {least_cost}")
    return best_route

heuristic_branch_bound(graph_data, 'S', 'G', heuristic_data)
    