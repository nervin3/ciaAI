graph_structure = {
    'S': {'A': 1, 'B': 2, 'C': 5},
    'A': {'D': 3, 'S': 1, 'B': 1},
    'B': {'A': 1, 'S': 2},
    'C': {'E': 4, 'S': 5},
    'D': {'A': 3, 'G': 2},
    'E': {'C': 4},
    'G': {'D': 2}
}

heuristic_values = {
    'S': 6,
    'A': 4,
    'B': 3,
    'C': 5,
    'D': 1,
    'E': 3,
    'G': 0
}

def beam_search_algorithm(graph, initial_node, target_node, heuristics, beam_width=2):
    current_level = [(initial_node, [initial_node], 0)]
    best_path = None
    minimum_cost = float('inf')

    while current_level:
        next_candidates = []
        for current, path, cost in current_level:
            if current == target_node:
                if cost < minimum_cost:
                    minimum_cost = cost
                    best_path = path
                continue

            for neighbor, travel_cost in graph[current].items():
                if neighbor not in path: 
                    next_candidates.append((neighbor, path + [neighbor], cost + travel_cost))

        next_candidates = sorted(next_candidates, key=lambda x: heuristics[x[0]])[:beam_width]
        if not next_candidates:  
            break

        current_level = next_candidates

    print(f"Beam Search Best Path: {best_path} with cost {minimum_cost}")
    return best_path

beam_search_algorithm(graph_structure, 'S', 'G', heuristic_values)
