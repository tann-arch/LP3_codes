def knapsack_01(weights, values, capacity):
    n = len(values)

    print("Items (Value, Weight):")
    for i in range(n):
        print(f"Item {i+1}: Value = {values[i]}, Weight = {weights[i]}")

    # Initialize DP table (n+1) x (capacity+1)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    # Build DP table
    print("\nFilling DP Table:")
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
                )
            else:
                dp[i][w] = dp[i - 1][w]
        print(f"After including item {i}: {dp[i]}")

    max_value = dp[n][capacity]

    # Trace back selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i)
            w -= weights[i - 1]

    selected_items.reverse()

    print("\n>> DP Table:")
    for row in dp:
        print(row)

    print("\nSelected Items:")
    for item in selected_items:
        print(
            f"-> Item {item}: Value = {values[item - 1]}, Weight = {weights[item - 1]}"
        )

    print(f"\n>> Maximum value in Knapsack = {max_value}")
    return max_value


# Example input
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("=== 0–1 Knapsack Problem (Dynamic Programming) ===")
print(f"Knapsack Capacity = {capacity}\n")

knapsack_01(weights, values, capacity)

























































# ## 🧭 THEORETICAL OVERVIEW

# **Problem statement:**
# Given `n` items, each with a `value` and a `weight`, select items to maximize total value without exceeding a given weight capacity — but **each item can be taken only once (0 or 1)**.

# Unlike the **Fractional Knapsack**, you cannot take fractions here.
# That’s why this problem is **combinatorial and NP-hard**.
# Dynamic Programming (DP) gives a *pseudo-polynomial* solution by breaking it into overlapping subproblems.

# **Key idea:**
# Build a table where `dp[i][w]` represents the *maximum value attainable* using the first `i` items and total capacity `w`.

# ---

# ## 🧠 DEEP THEORY CONCEPTS USED

# ### 1. **Dynamic Programming (DP)**

# DP is an optimization technique that solves problems by breaking them into smaller **overlapping subproblems**, solving each once, and storing their results.

# Two main principles:

# * **Optimal Substructure:**
#   The optimal solution of the whole problem can be built from optimal solutions of its subproblems.

#   For knapsack:
#   If item `i` is included, the remaining capacity = `W - weight[i]`.
#   If excluded, the capacity remains `W`.
#   We take the maximum of both.

# * **Overlapping Subproblems:**
#   The same subproblems (like capacity = 10 with first 2 items) recur many times, so we memoize them.

# ### 2. **Recursive Definition (DP Relation)**

# Let:

# * `val[i]` = value of item `i`
# * `wt[i]` = weight of item `i`
# * `W` = total capacity

# Then:

# [
# dp[i][w] =
# \begin{cases}
# 0 & \text{if } i=0 \text{ or } w=0 \
# dp[i-1][w] & \text{if } wt[i-1] > w \
# \max(val[i-1] + dp[i-1][w - wt[i-1]],\ dp[i-1][w]) & \text{otherwise}
# \end{cases}
# ]

# ### 3. **Bottom-Up Tabulation**

# This program builds the DP table iteratively (not recursively).
# Each cell represents a state defined by `(i, w)` — number of items and remaining capacity.

# Time complexity: **O(n × W)**
# Space complexity: **O(n × W)**
# (optimized versions use O(W) space).

# ### 4. **Traceback**

# After filling the table, we can trace back which items were included by comparing `dp[i][w]` and `dp[i-1][w]`.

# If they differ → item `i` was included.

# ### 5. **Complexity Nature**

# * It’s *pseudo-polynomial* — meaning complexity depends on numeric capacity `W`, not on the number of bits to represent `W`.
# * It’s **NP-complete** in general, but DP gives efficient results for moderate `W`.

# ### 6. **Relation to Other Theories**

# * Equivalent to **subset-sum** problem (if values == weights).
# * Related to **binary decision trees** (include/exclude branches).
# * Solved optimally via **Dynamic Programming Bellman Principle of Optimality**.

# ---

# ## 🧩 LINE-BY-LINE EXPLANATION

# ```python
# def knapsack_01(weights, values, capacity):
#     n = len(values)
# ```

# Defines the function, computes total items.

# ---

# ```python
#     print("Items (Value, Weight):")
#     for i in range(n):
#         print(f"Item {i+1}: Value = {values[i]}, Weight = {weights[i]}")
# ```

# Displays input data — helps verify correctness.

# ---

# ```python
#     dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
# ```

# Creates a 2D DP table of size `(n+1) × (capacity+1)`.
# `dp[i][w]` = max value using first `i` items with capacity `w`.

# Initialized with zeros since base case (no items or 0 capacity) gives 0 value.

# ---

# ### Core DP logic

# ```python
#     print("\nFilling DP Table:")
#     for i in range(1, n + 1):
#         for w in range(1, capacity + 1):
#             if weights[i - 1] <= w:
#                 dp[i][w] = max(
#                     values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w]
#                 )
#             else:
#                 dp[i][w] = dp[i - 1][w]
#         print(f"After including item {i}: {dp[i]}")
# ```

# #### Breakdown:

# * Loops over all items and capacities.
# * If item fits (`weights[i-1] <= w`):

#   * Two possibilities:

#     1. **Include** item → `value + dp[i-1][remaining capacity]`
#     2. **Exclude** item → `dp[i-1][same capacity]`
#   * Take the max.
# * Else → can’t include → copy previous value.

# This iterative filling ensures all subproblems are solved bottom-up.

# ---

# ```python
#     max_value = dp[n][capacity]
# ```

# Bottom-right cell = final answer (max possible value).

# ---

# ### Traceback: finding which items were taken

# ```python
#     selected_items = []
#     w = capacity
#     for i in range(n, 0, -1):
#         if dp[i][w] != dp[i - 1][w]:
#             selected_items.append(i)
#             w -= weights[i - 1]
# ```

# Starts from bottom-right, moving upward:

# * If the value differs from the previous row → item was included.
# * Subtract its weight from capacity and continue.

# Reverse list at end to print in input order.

# ---

# ### Display and return

# ```python
#     print("\n>> DP Table:")
#     for row in dp:
#         print(row)
# ```

# Prints entire DP table (for understanding and exam visualization).

# ```python
#     print("\nSelected Items:")
#     for item in selected_items:
#         print(
#             f"-> Item {item}: Value = {values[item - 1]}, Weight = {weights[item - 1]}"
#         )
# ```

# Prints selected items.

# ```python
#     print(f"\n>> Maximum value in Knapsack = {max_value}")
#     return max_value
# ```

# Displays final result and returns.

# ---

# ## 🧮 DRY RUN EXAMPLE

# **Input:**

# ```
# Values = [60, 100, 120]
# Weights = [10, 20, 30]
# Capacity = 50
# ```

# ### Step 1: Build table

# After processing all items:

# | i\W | 0 | 10 | 20  | 30  | 40  | 50  |
# | --- | - | -- | --- | --- | --- | --- |
# | 0   | 0 | 0  | 0   | 0   | 0   | 0   |
# | 1   | 0 | 60 | 60  | 60  | 60  | 60  |
# | 2   | 0 | 60 | 100 | 160 | 160 | 160 |
# | 3   | 0 | 60 | 100 | 160 | 180 | 220 |

# Max value = 220.

# ### Step 2: Selected items → Item 2 and Item 3.

# ---

# ## 🔁 EXPECTED CHANGES THEY MIGHT ASK

# 1. **Implement recursion + memoization version**

#    ```python
#    def knapsack_recursive(i, w):
#        if i == 0 or w == 0:
#            return 0
#        if wt[i-1] > w:
#            return knapsack_recursive(i-1, w)
#        else:
#            return max(val[i-1] + knapsack_recursive(i-1, w-wt[i-1]),
#                       knapsack_recursive(i-1, w))
#    ```

# 2. **Optimize space**

#    * Use 1D array `dp[w]` updating backward.

# 3. **Print only maximum value** (remove trace).

# 4. **Add user input** for values, weights, and capacity.

# 5. **Modify to print total weight used.**

#    ```python
#    total_weight = sum(weights[i-1] for i in selected_items)
#    ```

# 6. **Ask to explain difference between DP and Greedy** — highlight non-divisibility.

# ---

# ## 🎓 VIVA QUESTIONS

# **Q1. Why can’t we solve 0/1 knapsack with a greedy method?**
# Because taking a high ratio item first may block combinations of smaller ones that yield higher total value — the greedy choice property fails.

# **Q2. Define dynamic programming.**
# An algorithmic technique to solve optimization problems by combining solutions to overlapping subproblems.

# **Q3. Time and space complexity?**
# Time = O(n × W)
# Space = O(n × W)

# **Q4. What is “optimal substructure”?**
# A property where an optimal solution to a problem contains optimal solutions to its subproblems.

# **Q5. What is the difference between 0/1 and fractional knapsack?**

# * 0/1 → items indivisible → DP
# * Fractional → divisible → Greedy

# **Q6. What is pseudo-polynomial time?**
# Runtime depends on numeric value of input (capacity `W`), not its number of digits.

# **Q7. How to reconstruct chosen items?**
# By backtracking in DP table: if dp[i][w] ≠ dp[i-1][w], item i is included.

# ---

# ## ⚙️ RUN/TEST CHEATSHEET

# Run with:

# ```bash
# python3 knapsack_01.py
# ```

# Try edge cases:

# * Capacity = 0 → answer = 0
# * Weights > capacity → answer = 0
# * Single item fits exactly → takes that item.

# ---

# ## 🧠 INSIGHT TO REMEMBER

# The **0/1 Knapsack** demonstrates how dynamic programming transforms an **exponential** (2ⁿ subsets) brute-force problem into a **polynomial-time** table-based solution.
# It’s not just a coding trick — it’s a cornerstone of **algorithmic optimization** and the bridge between **greedy** and **combinatorial** problem domains.

# ---

# Would you like me to make a **handwritten-style notebook summary** next (with formula, DP table diagram, and key viva pointers) for this 0/1 knapsack? It’ll look like how professors expect your practical writeup to read.


















































