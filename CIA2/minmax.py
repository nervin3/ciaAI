def minimax_search(depth, node_index, is_max_player, node_values):
    if depth == 3:
        return node_values[node_index]

    if is_max_player:
        best_score = float('-inf')
        for child in range(2):
            score = minimax_search(depth + 1, node_index * 2 + child, False, node_values)
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float('inf')
        for child in range(2):
            score = minimax_search(depth + 1, node_index * 2 + child, True, node_values)
            best_score = min(best_score, score)
        return best_score


if __name__ == "__main__":
    node_values = [3, 5, 2, 8, 6, 1, 4, 7]  

    optimal_value = minimax_search(0, 0, True, node_values)
    print(f"Optimal value determined using Minimax: {optimal_value}")
