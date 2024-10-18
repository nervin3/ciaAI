import heapq

graph_structure = {
    'Start': {'NodeA': 1, 'NodeB': 2, 'NodeC': 5},
    'NodeA': {'NodeD': 3, 'Start': 1, 'NodeB': 1},
    'NodeB': {'NodeA': 1, 'Start': 2},
    'NodeC': {'NodeE': 4, 'Start': 5},
    'NodeD': {'NodeA': 3, 'NodeG': 2},
    'NodeE': {'NodeC': 4},
    'NodeG': {'NodeD': 2}
}

heuristic_values = {
    'Start': 6,
    'NodeA': 4,
    'NodeB': 3,
    'NodeC': 5,
    'NodeD': 1,
    'NodeE': 3,
    'NodeG': 0
}

def branch_and_bound_greedy_search(graph, initial_node, target_node, heuristics):
    priority_queue = [(heuristics[initial_node], 0, initial_node, [initial_node])]
    best_path = None
    minimum_cost = float('inf')

    while priority_queue:
        estimated_cost, actual_cost, current_node, current_path = heapq.heappop(priority_queue)

        if current_node == target_node:
            if actual_cost < minimum_cost:
                minimum_cost = actual_cost
                best_path = current_path
            continue

        for adjacent_node, travel_cost in graph[current_node].items():
            if adjacent_node not in current_path:
                total_cost = actual_cost + travel_cost
                estimated_total_cost = total_cost + heuristics[adjacent_node]
                heapq.heappush(priority_queue, (estimated_total_cost, total_cost, adjacent_node, current_path + [adjacent_node]))

    print(f"Branch and Bound Greedy Best Path: {best_path} with cost {minimum_cost}")
    return best_path

branch_and_bound_greedy_search(graph_structure, 'Start', 'NodeG', heuristic_values)
