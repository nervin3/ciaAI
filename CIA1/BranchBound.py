import heapq

network = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}

def branch_bound_search(network, origin, destination):
    task_queue = [(0, origin, [origin])]
    optimal_route = None
    least_cost = float('inf')

    while task_queue:
        current_cost, current_node, journey = heapq.heappop(task_queue)

        if current_node == destination:
            if current_cost < least_cost:
                least_cost = current_cost
                optimal_route = journey
            continue

        for adj_node, travel_cost in network[current_node].items():
            if adj_node not in journey:
                updated_cost = current_cost + travel_cost
                heapq.heappush(task_queue, (updated_cost, adj_node, journey + [adj_node]))

    print(f"Optimal Path: {optimal_route} with total cost {least_cost}")
    return optimal_route

branch_bound_search(network, 'S', 'G')
