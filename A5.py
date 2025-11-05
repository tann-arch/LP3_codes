def print_board(board, n):
    for i in range(n):
        for j in range(n):
            print(board[i][j], end=" ")
        print()
    print()

def is_safe(board, row, col, n):
    # Check column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    i, j = row, col
    while i >= 0 and j >= 0:
        if board[i][j] == 1:
            return False
        i -= 1
        j -= 1

    # Check upper right diagonal
    i, j = row, col
    while i >= 0 and j < n:
        if board[i][j] == 1:
            return False
        i -= 1
        j += 1
    return True

def solve_n_queens(board, row, n):
    if row >= n:
        print("\n>>Solution Found:\n")
        print_board(board, n)
        return True

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            print(f"Placing Queen at ({row}, {col})")
            if solve_n_queens(board, row + 1, n):
                return True
            print(f"Backtracking from ({row}, {col})")
            board[row][col] = 0  # Backtrack
    return False

def n_queens(n, first_queen_col):
    board = [[0 for _ in range(n)] for _ in range(n)]
    # Place first queen manually
    board[0][first_queen_col] = 1
    print(f"Initial Board with First Queen placed at (0, {first_queen_col}):")
    print_board(board, n)

    if not solve_n_queens(board, 1, n):
        print("No solution exists for this configuration.")

# Example usage
n = 4
first_queen_col = 1  # 0-indexed column position of first queen
print("=== N-Queens Problem using Backtracking ===")
print(f"Board Size: {n} x {n}")
print(f"First Queen placed at column {first_queen_col}\n")
n_queens(n, first_queen_col)








































































# ## 🧭 THEORETICAL OVERVIEW

# **The N-Queens problem:**
# Place N queens on an N×N chessboard so that **no two queens attack each other**.
# That means no two queens share the same **row, column, or diagonal**.

# ### Rules of attack:

# * A queen can attack any piece in its same row, column, or diagonal.
# * The task: place one queen per row such that none threaten each other.

# ### Nature of problem:

# * **Constraint Satisfaction Problem (CSP)** — we’re looking for a configuration satisfying constraints.
# * **Non-deterministic search problem** — there may be multiple valid solutions or none.
# * **Backtracking** is used to explore possible positions systematically.

# ---

# ## 🧠 DEEP THEORY CONCEPTS USED

# ### 1. **Backtracking Algorithm (Depth-First Search in disguise)**

# Backtracking is a **refined brute-force** method that incrementally builds candidates and abandons partial solutions as soon as it detects a violation of constraints (known as *pruning*).

# * **State space tree:** Each level represents one row.
#   Each node represents a partial placement of queens.
# * **Decision:** In each row, choose a column to place a queen.
# * **Constraint check:** For each placement, check if it’s safe.
# * **Backtrack:** If placing the next queen leads to a dead end, undo the last step (remove queen) and try the next position.

# **Algorithm type:**
# Systematic search, often represented as recursive DFS with constraint pruning.

# ---

# ### 2. **Constraint Satisfaction & Pruning**

# For each queen placement:

# * **Row constraint:** Only one queen per row — automatically satisfied since we place one per row.
# * **Column constraint:** Must check previous rows for same column.
# * **Diagonal constraints:** Must check both diagonals.

# This drastically cuts down the search space from ( N^N ) (all placements) to a manageable fraction.

# ---

# ### 3. **Recursive Tree Representation**

# At row `r`, the recursion explores all columns `c = 0 ... N-1`:

# * If safe → move to row `r+1`
# * If no column works → backtrack to `r-1`

# Each path in the recursion tree represents a possible configuration.
# Valid leaves correspond to solutions.

# **Depth of recursion:** N
# **Branching factor:** up to N (one queen per column per row)

# ---

# ### 4. **Complexity**

# * **Time complexity:** O(N!) in the worst case (since there are N! permutations for placing N queens).
# * **Space complexity:** O(N²) for the board representation (though only O(N) for column positions).

# Despite the exponential nature, backtracking prunes large portions of the tree quickly for small N (like 4 or 8).

# ---

# ### 5. **Mathematical Context**

# The N-Queens problem has been studied since 1848 (Max Bezzel).
# For N=1 → 1 solution
# For N=2,3 → no solution
# For N≥4 → at least one solution exists.
# The number of solutions grows rapidly (e.g., 92 for N=8).

# ---

# ### 6. **Alternative Theoretical Angles**

# * **Permutation approach:** Represent columns as permutation of [0..N-1] ensuring diagonal safety.
# * **Bitmask optimization:** Represent rows/columns/diagonals as bit patterns → O(1) safety check.
# * **Constraint Propagation (CSP theory):** Advanced form using domain reduction.

# ---

# ## 🧩 LINE-BY-LINE EXPLANATION

# ### Helper: print the board

# ```python
# def print_board(board, n):
#     for i in range(n):
#         for j in range(n):
#             print(board[i][j], end=" ")
#         print()
#     print()
# ```

# * Loops through each row/column and prints the board.
# * `1` means a queen is placed; `0` means empty.
# * Prints an extra newline for readability.

# ---

# ### Safety check

# ```python
# def is_safe(board, row, col, n):
# ```

# Checks if placing a queen at `(row, col)` is safe.

# #### Check same column

# ```python
#     for i in range(row):
#         if board[i][col] == 1:
#             return False
# ```

# If any queen is in the same column above current row → not safe.

# #### Check upper left diagonal

# ```python
#     i, j = row, col
#     while i >= 0 and j >= 0:
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j -= 1
# ```

# Moves diagonally up-left → if a queen found → unsafe.

# #### Check upper right diagonal

# ```python
#     i, j = row, col
#     while i >= 0 and j < n:
#         if board[i][j] == 1:
#             return False
#         i -= 1
#         j += 1
# ```

# Moves diagonally up-right → checks for conflicts.

# If all checks pass → safe.

# ```python
#     return True
# ```

# ---

# ### Recursive backtracking solver

# ```python
# def solve_n_queens(board, row, n):
#     if row >= n:
#         print("\n>>Solution Found:\n")
#         print_board(board, n)
#         return True
# ```

# Base case: if all rows filled, we found a valid configuration → print it.

# ---

# ```python
#     for col in range(n):
#         if is_safe(board, row, col, n):
#             board[row][col] = 1
#             print(f"Placing Queen at ({row}, {col})")
# ```

# Try placing a queen in each column of current row.
# If safe → mark queen (`1`) and recurse to next row.

# ---

# ```python
#             if solve_n_queens(board, row + 1, n):
#                 return True
# ```

# Recursive call — if a solution found deeper → propagate success.

# ---

# ```python
#             print(f"Backtracking from ({row}, {col})")
#             board[row][col] = 0
# ```

# If deeper call failed → remove queen (undo move) and try next column.
# Classic **backtracking** step.

# ---

# ```python
#     return False
# ```

# If no column works in current row → backtrack further up.

# ---

# ### Main controller function

# ```python
# def n_queens(n, first_queen_col):
#     board = [[0 for _ in range(n)] for _ in range(n)]
# ```

# Creates an empty N×N chessboard.

# ```python
#     board[0][first_queen_col] = 1
#     print(f"Initial Board with First Queen placed at (0, {first_queen_col}):")
#     print_board(board, n)
# ```

# Places first queen manually in given column of first row.

# ```python
#     if not solve_n_queens(board, 1, n):
#         print("No solution exists for this configuration.")
# ```

# Starts solving from second row (index 1).
# If recursion fails → no valid configuration found.

# ---

# ### Example run

# ```python
# n = 4
# first_queen_col = 1
# ```

# 4×4 board, first queen at (0,1).
# One valid configuration (queens at columns 1, 3, 0, 2).

# Output prints placements, backtracking steps, and final board.

# ---

# ## 🧮 DRY RUN EXAMPLE (N=4)

# 1. Place queen at (0,1)
# 2. Row 1:

#    * Try col 0 → safe → place (1,0)
#    * Row 2:

#      * col 0,1,2 conflict → backtrack (1,0)
#    * Try col 2 → safe → place (1,2)
#    * Row 2:

#      * place (2,0) → works
#    * Row 3:

#      * place (3,3) → solution found ✅

# Board (1s = queens):

# ```
# 0 1 0 0
# 0 0 1 0
# 1 0 0 0
# 0 0 0 1
# ```

# ---

# ## 🔁 EXPECTED CHANGES THEY MIGHT ASK

# 1. **Find all solutions (not just one)**

#    * Remove `return True` after printing a solution.
#    * Continue recursion to explore all configurations.

# 2. **Remove first queen constraint**

#    * Start recursion from row 0.

# 3. **Display total number of solutions**

#    * Keep a counter variable.

# 4. **Use a 1D array representation**
#    `board[row] = col_position`

# 5. **Add delay or visualization** (for UI-based viva).

# 6. **Explain diagonals mathematically:**
#    Two queens `(r1,c1)` and `(r2,c2)` are on same diagonal if
#    (|r1 - r2| = |c1 - c2|)

# ---

# ## 🎓 VIVA QUESTIONS

# **Q1. What is the N-Queens problem?**
# Placing N queens on an N×N board so that no two attack each other.

# **Q2. Why use backtracking?**
# Because it explores all configurations systematically and prunes invalid branches early, reducing unnecessary computation.

# **Q3. Time complexity?**
# O(N!) in worst case, but effectively much less due to pruning.

# **Q4. What are constraints checked?**
# Column and both diagonals — since each row has exactly one queen.

# **Q5. How is diagonal conflict detected?**
# If absolute row difference = absolute column difference.

# **Q6. Can we solve it iteratively?**
# Yes, but recursion naturally expresses the state space.

# **Q7. What’s difference between backtracking and brute force?**
# Backtracking prunes invalid states early; brute force explores all regardless of validity.

# ---

# ## ⚙️ RUN / TEST CHEATSHEET

# To execute:

# ```bash
# python3 n_queens.py
# ```

# Try:

# * `n=4`, `first_queen_col=0` → 2 possible solutions.
# * `n=3` → No solution.
# * `n=8` → Classic 8-Queens problem.

# ---

# ## 🧠 INSIGHT TO REMEMBER

# The **N-Queens** problem is a beautiful microcosm of **search algorithms** —
# it shows how recursion and backtracking emulate logical reasoning:
# “Try, verify, and retreat when wrong.”

# It’s also a building block for **constraint solvers, SAT problems, and AI planning systems** — one of the earliest demonstrations of computational search.

# ---

# Would you like me to make the **handwritten-style practical notes** for this one too (including the state space tree diagram and the diagonal safety condition formula)?

