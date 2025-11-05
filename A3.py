def fractional_knapsack(weights, values, capacity):
    n = len(values)
    print("Items (Value, Weight):")
    for i in range(n):
        print(f"Item {i+1}: Value = {values[i]}, Weight = {weights[i]}")

    # Calculate value/weight ratio for each item
    ratio = [(values[i] / weights[i], weights[i], values[i], i + 1) for i in range(n)]

    # Sort items by ratio in descending order
    ratio.sort(reverse=True)

    print("\nItems sorted by Value/Weight ratio (descending):")
    for r, w, v, idx in ratio:
        print(f"Item {idx}: Ratio = {r:.2f}, Value = {v}, Weight = {w}")

    total_value = 0.0  # Total value accumulated
    print("\nProcessing items:")
    for r, w, v, idx in ratio:
        if capacity == 0:
            break

        if capacity >= w:
            capacity -= w
            total_value += v
            print(f"-> Took entire Item {idx} (Weight {w}, Value {v})")
        else:
            fraction = capacity / w
            total_value += v * fraction
            print(
                f"-> Took {fraction*100:.1f}% of Item {idx} (Weight {capacity:.2f}, Value {v * fraction:.2f})"
            )
            capacity = 0

    print(f"\n>> Maximum value in Knapsack = {total_value:.2f}")
    return total_value


# Example input
values = [60, 100, 120]
weights = [10, 20, 30]
capacity = 50

print("=== Fractional Knapsack Problem ===")
print(f"Knapsack Capacity = {capacity}\n")

fractional_knapsack(weights, values, capacity)






















































# Fantastic, Shubham — this is the **Fractional Knapsack Problem**, a staple of greedy algorithms and a favorite of university examiners.
# Let’s unpack it **thoroughly**, with a new detailed section on the **Deep Theory Concepts Used** as you asked.

# ---

# # 🧭 THEORETICAL OVERVIEW

# The **Fractional Knapsack Problem** asks:

# > Given `n` items, each with a *value* and *weight*, determine the maximum total value you can carry in a knapsack of limited capacity — but you can take *fractions* of items.

# Unlike the **0/1 Knapsack Problem** (where items are indivisible), here we’re allowed to take parts — e.g., half an item.
# That changes the problem class from **NP-hard** (for 0/1) to **polynomial-time solvable** (for fractional).

# **Strategy:**

# * Compute each item’s *value-to-weight ratio*.
# * Sort items by this ratio, descending.
# * Greedily pick the item (or fraction) with the highest ratio until the capacity is full.

# This works because taking the “most value per unit weight” first always leads to the optimal solution — a hallmark of a *greedy algorithm*.

# ---

# # 🧩 DEEP THEORY CONCEPTS USED

# ### 1. **Greedy Algorithm Paradigm**

# A greedy algorithm makes a locally optimal choice at each step, hoping it leads to a globally optimal solution.
# For the Fractional Knapsack problem, the **greedy choice property** and **optimal substructure** are both satisfied:

# * **Greedy choice property:**
#   Choosing the item with the highest value/weight ratio first will never lead to a worse solution — because fractional items allow continuous division.

# * **Optimal substructure:**
#   The optimal solution to a problem of size `n` includes the optimal solution to its subproblem of size `n-1` (remaining capacity after taking an item).

# Together, they guarantee **global optimality** — something not true for 0/1 knapsack (where you must use dynamic programming).

# ---

# ### 2. **Mathematical Model**

# Let:

# * ( n ) = number of items
# * ( w_i ) = weight of item i
# * ( v_i ) = value of item i
# * ( x_i \in [0,1] ) = fraction of item i taken

# We want to **maximize total value**:
# [
# \text{Maximize } \sum_{i=1}^{n} v_i x_i
# ]

# Subject to the **capacity constraint**:
# [
# \sum_{i=1}^{n} w_i x_i \leq W
# ]

# This is a **Linear Programming (LP)** problem with continuous variables (x_i).
# Because the constraint is linear and the objective is linear, the solution lies at an **extreme point** of the feasible region — where all but one of the (x_i) are 0 or 1, and one may be fractional.
# That’s precisely what the greedy method constructs.

# ---

# ### 3. **Sorting and Computational Complexity**

# Sorting by ratio has time complexity (O(n \log n)).
# The rest (linear scan and accumulation) is (O(n)).
# So total = (O(n \log n)).

# Space complexity = (O(n)) for storing ratios.

# This is **much more efficient** than dynamic programming ((O(nW))) used for 0/1 knapsack.

# ---

# ### 4. **Correctness Proof (Sketch)**

# Let’s assume the greedy solution isn’t optimal.
# Then, there exists another solution with higher value — meaning it must have replaced a lower ratio item fraction with a higher ratio one, contradicting the sorting order.
# Therefore, the greedy approach gives the optimal result.

# This follows from **exchange argument**:
# Any non-greedy choice can be swapped for a greedy one without reducing total value.

# ---

# ### 5. **Comparison with 0/1 Knapsack**

# | Feature                | Fractional Knapsack          | 0/1 Knapsack               |
# | ---------------------- | ---------------------------- | -------------------------- |
# | Item divisibility      | Allowed                      | Not allowed                |
# | Algorithm type         | Greedy                       | Dynamic Programming        |
# | Complexity             | O(n log n)                   | O(nW)                      |
# | Optimal Substructure   | Yes                          | Yes                        |
# | Greedy Choice Property | True                         | False                      |
# | Nature of solution     | Deterministic and continuous | Combinatorial and discrete |

# ---

# # 🧮 LINE-BY-LINE EXPLANATION

# ```python
# def fractional_knapsack(weights, values, capacity):
#     n = len(values)
# ```

# Defines function and counts number of items.

# ---

# ```python
#     print("Items (Value, Weight):")
#     for i in range(n):
#         print(f"Item {i+1}: Value = {values[i]}, Weight = {weights[i]}")
# ```

# Displays initial data for clarity — useful for demonstration or viva.

# ---

# ```python
#     ratio = [(values[i] / weights[i], weights[i], values[i], i + 1) for i in range(n)]
# ```

# Computes **value-to-weight ratio** for each item and keeps extra info:

# * ratio
# * weight
# * value
# * index (for printing)

# Stored as tuple → easy to sort later.

# ---

# ```python
#     ratio.sort(reverse=True)
# ```

# Sorts the items **descending by ratio**, so the first item gives highest value per unit weight.

# ---

# ```python
#     print("\nItems sorted by Value/Weight ratio (descending):")
#     for r, w, v, idx in ratio:
#         print(f"Item {idx}: Ratio = {r:.2f}, Value = {v}, Weight = {w}")
# ```

# Prints sorted list to show decision order.

# ---

# ```python
#     total_value = 0.0  # Total value accumulated
#     print("\nProcessing items:")
#     for r, w, v, idx in ratio:
#         if capacity == 0:
#             break
# ```

# Iterates over sorted items; if the bag is full, stop.

# ---

# ```python
#         if capacity >= w:
#             capacity -= w
#             total_value += v
#             print(f"-> Took entire Item {idx} (Weight {w}, Value {v})")
# ```

# If there’s enough capacity for the whole item → take it entirely.

# ---

# ```python
#         else:
#             fraction = capacity / w
#             total_value += v * fraction
#             print(
#                 f"-> Took {fraction*100:.1f}% of Item {idx} (Weight {capacity:.2f}, Value {v * fraction:.2f})"
#             )
#             capacity = 0
# ```

# If not enough space, take fractional part:
# `fraction = remaining capacity / item weight`.
# Update total value accordingly.
# Then set capacity = 0 → knapsack full.

# ---

# ```python
#     print(f"\n>> Maximum value in Knapsack = {total_value:.2f}")
#     return total_value
# ```

# Prints final optimal value and returns it.

# ---

# ### Example Run

# ```
# Values  = [60, 100, 120]
# Weights = [10, 20, 30]
# Capacity = 50
# ```

# Sorted by ratio:

# | Item | Value | Weight | Ratio |
# | ---- | ----- | ------ | ----- |
# | 1    | 60    | 10     | 6.0   |
# | 2    | 100   | 20     | 5.0   |
# | 3    | 120   | 30     | 4.0   |

# Take:

# * Entire Item 1 (10 kg)
# * Entire Item 2 (20 kg)
# * 20/30 = 66.6% of Item 3

# Total value = 60 + 100 + 120×(20/30) = **240.0**

# ---

# # 🔁 EXPECTED CHANGES THEY MIGHT ASK

# 1. **User Input**

#    ```python
#    n = int(input("Enter number of items: "))
#    values = list(map(int, input("Enter values: ").split()))
#    weights = list(map(int, input("Enter weights: ").split()))
#    capacity = int(input("Enter capacity: "))
#    ```

# 2. **Print only final result (no debug info)**
#    → remove print statements.

# 3. **Return both total value and fraction list**
#    To show what fraction of each item was taken.

# 4. **Sort using a custom comparator**
#    Or demonstrate without built-in `.sort()` (e.g., using manual bubble sort).

# 5. **Change to 0/1 knapsack version**
#    Use dynamic programming array:

#    ```python
#    dp = [[0]*(capacity+1) for _ in range(n+1)]
#    ```

# 6. **Ask to derive formula for fractional part:**
#    ( \text{fraction value} = v_i \times \frac{remaining_capacity}{w_i} )

# ---

# # 🎓 POSSIBLE VIVA QUESTIONS

# **Q1. Define fractional knapsack problem.**
# It’s a problem of selecting items to maximize total value within weight capacity, allowing fractional parts of items.

# **Q2. Why can we use greedy method here but not in 0/1 knapsack?**
# Because fractional division makes the value function continuous and linear, satisfying greedy choice property.

# **Q3. What is time complexity?**
# (O(n \log n)) due to sorting by ratio.

# **Q4. When will we take a fractional item?**
# When the next item’s full weight doesn’t fit in the remaining capacity.

# **Q5. Is the solution unique?**
# Not necessarily if two items have the same ratio.

# **Q6. What is optimal substructure?**
# Optimal solution of the whole problem contains optimal solutions of its subproblems.

# ---

# # ⚙️ RUN/TEST CHEATSHEET

# To run:

# ```bash
# python3 fractional_knapsack.py
# ```

# To test edge case:

# * Empty items: should return 0.
# * Capacity 0: should return 0.
# * All same ratio: should take in order of input until full.

# ---

# # 🧠 INSIGHT TO REMEMBER

# The **Fractional Knapsack** is the *only variant* of knapsack solvable by a greedy method — a brilliant example where “short-term best” leads to global best.
# It’s also an elegant case study in the boundary between combinatorial and continuous optimization.

# ---

# Would you like me to now prepare a **handwritten-style practical notebook summary** (short and neat) for this same code — with formulae and key viva points condensed for memorization?

