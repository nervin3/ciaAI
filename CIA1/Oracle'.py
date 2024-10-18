graph_data = {
    'M': {'N': 2, 'O': 3},
    'N': {'M': 2, 'P': 4},
    'O': {'M': 3, 'Q': 5},
    'P': {'N': 4},
    'Q': {'O': 5, 'R': 1},
    'R': {'Q': 1}
}

heuristic_data = {
    'M': 4,
    'N': 2,
    'O': 3,
    'P': 1,
    'Q': 0,
    'R': 1
}

def oracle_search(graph, start, goal):
    path = [start]
    current = start
    total_cost = 0
    visited = set()

    while current != goal:
        visited.add(current)
        neighbors = graph.get(current, {})

        if not neighbors:
            print(f"No valid neighbors for node {current}, cannot proceed further.")
            return None
        
        print(f"Current node: {current}, Neighbors: {neighbors}")
        
        unvisited_neighbors = {n: neighbors[n] for n in neighbors if n not in visited}
        
        if not unvisited_neighbors:
            print(f"No valid unvisited neighbors for node {current}. Backtracking.")
            path.pop()
            if not path:
                print("No path to the goal found.")
                return None
            current = path[-1] 
            continue

        best_neighbor = min(unvisited_neighbors, key=lambda x: heuristic_data[x])
        
        total_cost += neighbors[best_neighbor]
        path.append(best_neighbor)
        current = best_neighbor

    print(f"Oracle Search Best Path: {path} with cost {total_cost}")
    return path

oracle_search(graph_data, 'M', 'R')
