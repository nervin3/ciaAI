def alpha_beta_pruning(current_depth, position, is_max_player, score_values, alpha, beta):
    if current_depth == 3:
        return score_values[position]

    if is_max_player:
        best_value = float('-inf')
        for child in range(2):
            value = alpha_beta_pruning(current_depth + 1, position * 2 + child, False, score_values, alpha, beta)
            best_value = max(best_value, value)
            alpha = max(alpha, value)
            if beta <= alpha:
                break
        return best_value
    else:
        best_value = float('inf')
        for child in range(2):
            value = alpha_beta_pruning(current_depth + 1, position * 2 + child, True, score_values, alpha, beta)
            best_value = min(best_value, value)
            beta = min(beta, value)
            if beta <= alpha:
                break
        return best_value


if __name__ == "__main__":
    score_values = [3, 5, 2, 9, 6, 0, 1, 4]

    alpha = float('-inf')
    beta = float('inf')

    optimal_score = alpha_beta_pruning(0, 0, True, score_values, alpha, beta)

    print(f"Optimal score determined using Alpha-Beta Pruning: {optimal_score}")
