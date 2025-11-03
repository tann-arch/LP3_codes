def knapsack_dynamic_programming(values, weights, capacity):
    n = len(values)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]
    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1
    selected_items.reverse()
    return dp[n][capacity], selected_items
 # Example usage
if __name__ == "__main__":
 values = [60, 100, 120]
 weights = [10, 20, 30]
 capacity = 50
 max_value, selected_items = knapsack_dynamic_programming(values, weights, 
capacity)
 print("Maximum value in the knapsack:", max_value)
 print("Selected items:", selected_items)