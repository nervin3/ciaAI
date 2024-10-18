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
    priority_list = [(heuristics[initial_node], 0, initial_node, [initial_node])]

    while priority_list:
        estimated_total_cost, actual_cost, current_node, current_path = heapq.heappop(priority_list)

        if current_node == target_node:
            print(f"Branch and Bound Greedy Search: Best Path: {current_path} with cost {actual_cost}")
            return current_path

        for adjacent_node, travel_cost in graph[current_node].items():
            if adjacent_node not in current_path:
                new_cost = actual_cost + travel_cost
                estimated_cost = new_cost + heuristics[adjacent_node]
                heapq.heappush(priority_list, (estimated_cost, new_cost, adjacent_node, current_path + [adjacent_node]))

branch_and_bound_greedy_search(graph_structure, 'Start', 'NodeG', heuristic_values)
