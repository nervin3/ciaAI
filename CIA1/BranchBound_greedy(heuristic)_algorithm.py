import heapq

network = {
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

def greedy_branch_and_bound(graph, initial, target, heuristics):
    priority_queue = [(heuristics[initial], 0, initial, [initial])]
    
    while priority_queue:
        est_cost, curr_cost, current_node, current_path = heapq.heappop(priority_queue)

        if current_node == target:
            print(f"Greedy Branch and Bound with Heuristic: Best Path: {current_path} with cost {curr_cost}")
            return current_path

        for adjacent, travel_cost in graph[current_node].items():
            if adjacent not in current_path:
                updated_cost = curr_cost + travel_cost
                estimated_total_cost = updated_cost + heuristics[adjacent]
                heapq.heappush(priority_queue, (estimated_total_cost, updated_cost, adjacent, current_path + [adjacent]))

greedy_branch_and_bound(network, 'Start', 'NodeG', heuristic_values)
