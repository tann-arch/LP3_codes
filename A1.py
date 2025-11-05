
# Recursive method
def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)

# Iterative method
def fibonacci_iterative(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# Main program
n = int(input("Enter number of terms: "))

# Print using Iterative
print("\nFibonacci Series (Iterative):")
print(fibonacci_iterative(n))

# Print using Recursive
print("\nFibonacci Series (Recursive):")
for i in range(n):
    print(fibonacci_recursive(i), end=" ")



















































































# ---

# ## 🧩 **Assignment Title**

# > **Write a Python program to generate the Fibonacci series using both iterative and recursive methods.**

# ---

# ## 🧠 **Theory Concepts**

# ### 🔹 What is the Fibonacci Series?

# The Fibonacci sequence is a series of numbers where each number is the **sum of the previous two numbers**.
# It starts with:

# ```
# 0, 1, 1, 2, 3, 5, 8, 13, ...
# ```

# Formally:
# [
# F(n) =
# \begin{cases}
# 0 & \text{if } n=0 \
# 1 & \text{if } n=1 \
# F(n-1) + F(n-2) & \text{if } n>1
# \end{cases}
# ]

# ---

# ### 🔹 Recursive Approach

# Recursion means a **function calls itself** to solve smaller instances of the same problem.

# For Fibonacci:

# ```python
# F(n) = F(n-1) + F(n-2)
# ```

# The recursion continues until reaching base cases (n=0 or n=1).

# **Advantages**

# * Easy to understand and implement.
#   **Disadvantages**
# * Inefficient for large n (repeats calculations).
# * High time complexity O(2ⁿ).

# ---

# ### 🔹 Iterative Approach

# Iteration uses **loops** instead of recursive function calls.

# We start with a = 0 and b = 1, then repeatedly add to generate the next term.

# **Advantages**

# * Efficient, faster, uses less memory.
#   **Disadvantages**
# * Slightly longer code but simple logic.

# **Time complexity:** O(n)

# ---

# ### 🔹 Comparison

# | Method    | Time Complexity | Space Complexity | Remarks                   |
# | --------- | --------------- | ---------------- | ------------------------- |
# | Recursive | O(2ⁿ)           | O(n)             | Slow for large inputs     |
# | Iterative | O(n)            | O(1)             | Fast and memory efficient |

# ---

# ## 💻 **Code Explanation (Line-by-Line)**

# ```python
# # Recursive method
# def fibonacci_recursive(n):
#     if n <= 1:
#         return n
#     else:
#         return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)
# ```

# 🧩 **Explanation:**

# * Function `fibonacci_recursive(n)` finds the nth Fibonacci number.
# * **Base case:** if n ≤ 1, return n directly.
# * **Recursive case:** sum of previous two Fibonacci numbers.
# * Calls itself twice → exponential time complexity.

# ---

# ```python
# # Iterative method
# def fibonacci_iterative(n):
#     a, b = 0, 1
#     series = []
#     for _ in range(n):
#         series.append(a)
#         a, b = b, a + b
#     return series
# ```

# 🧩 **Explanation:**

# * Starts with first two Fibonacci numbers (0, 1).
# * Uses a `for` loop to append each new term into a list `series`.
# * Returns the full list containing n terms.
# * Efficient (linear time).

# ---

# ```python
# # Main program
# n = int(input("Enter number of terms: "))
# ```

# Takes user input for how many terms of the Fibonacci series to print.

# ---

# ```python
# # Print using Iterative
# print("\nFibonacci Series (Iterative):")
# print(fibonacci_iterative(n))
# ```

# Prints complete series using the iterative method.

# ---

# ```python
# # Print using Recursive
# print("\nFibonacci Series (Recursive):")
# for i in range(n):
#     print(fibonacci_recursive(i), end=" ")
# ```

# Calls `fibonacci_recursive()` repeatedly for each term from 0 to n−1
# and prints them inline.

# ---

# ### ✅ **Sample Output**

# ```
# Enter number of terms: 7

# Fibonacci Series (Iterative):
# [0, 1, 1, 2, 3, 5, 8]

# Fibonacci Series (Recursive):
# 0 1 1 2 3 5 8
# ```

# ---

# ## ⚙️ **Algorithm Steps**

# ### **Iterative Algorithm**

# 1. Initialize a=0, b=1
# 2. Repeat n times:

#    * Print a
#    * Update: `next = a + b`
#    * `a = b`, `b = next`

# ### **Recursive Algorithm**

# 1. If n ≤ 1 → return n
# 2. Else → return `F(n-1) + F(n-2)`
# 3. Call recursively until base cases reached.

# ---

# ## 🧮 **Complexity Analysis**

# | Method        | Time Complexity | Space Complexity |
# | ------------- | --------------- | ---------------- |
# | **Recursive** | O(2ⁿ)           | O(n)             |
# | **Iterative** | O(n)            | O(1)             |

# ---

# ## 🧠 **Expected Viva Questions and Answers**

# | Question                                             | Short Answer                                              |
# | ---------------------------------------------------- | --------------------------------------------------------- |
# | What is the Fibonacci series?                        | Series where each number is the sum of previous two.      |
# | What is recursion?                                   | Function calling itself to solve smaller subproblems.     |
# | What is the base case in Fibonacci recursion?        | When n ≤ 1 (return n).                                    |
# | What is iteration?                                   | Repetition of steps using loops until a condition is met. |
# | Which is faster: recursive or iterative?             | Iterative is faster (O(n) vs O(2ⁿ)).                      |
# | Why is recursion slow?                               | Because it recomputes overlapping subproblems.            |
# | What is stack overflow?                              | Too many recursive calls cause memory overflow.           |
# | What is the space complexity of recursive Fibonacci? | O(n) due to function call stack.                          |
# | Why use recursion at all?                            | Code simplicity and clarity for small inputs.             |
# | What happens if we input a large number (like 50)?   | Recursive version becomes extremely slow.                 |

# ---

# ## 🔁 **Expected “Change Requests” During Practical and How to Do Them**

# | Change Requested                                         | What to Do                                      | Example Code                         |
# | -------------------------------------------------------- | ----------------------------------------------- | ------------------------------------ |
# | **“Print only nth Fibonacci number instead of series.”** | Just call once and print                        | `print(fibonacci_iterative(n)[-1])`  |
# | **“Start series from 1 instead of 0.”**                  | Change initial values                           | `a, b = 1, 1`                        |
# | **“Add total sum of Fibonacci numbers.”**                | Use `sum(series)`                               | `print(sum(fibonacci_iterative(n)))` |
# | **“Show recursive call count.”**                         | Add counter variable inside recursive function. |                                      |
# | **“Use while loop instead of for loop.”**                | Replace `for` loop with while.                  |                                      |
# | **“Use memoization to optimize recursion.”**             | Store computed values in dictionary.            |                                      |
# | **“Plot the Fibonacci sequence.”**                       | Use matplotlib to plot vs term number.          |                                      |

# ---

# ### Example: Optimized Recursive Version (for viva surprise)

# ```python
# memo = {}
# def fib_memo(n):
#     if n in memo:
#         return memo[n]
#     if n <= 1:
#         memo[n] = n
#     else:
#         memo[n] = fib_memo(n-1) + fib_memo(n-2)
#     return memo[n]
# ```

# ---

# ## 📈 **Graphical Add-On (optional, extra marks)**

# You can plot Fibonacci growth to visualize exponential pattern:

# ```python
# import matplotlib.pyplot as plt
# n = 10
# series = fibonacci_iterative(n)
# plt.plot(range(n), series, marker='o')
# plt.title("Fibonacci Sequence Growth")
# plt.xlabel("Term Number")
# plt.ylabel("Value")
# plt.show()
# ```

# ---

# ## 🧾 **Conclusion**

# > The program successfully generates the Fibonacci series using both **iterative** and **recursive** approaches.
# > The iterative method is more efficient in time and space, while recursion provides a clearer understanding of problem decomposition.

# ---

# ## 🗒️ **Quick Oral Summary (for Viva)**

# > “Fibonacci series is a sequence where each term is the sum of the previous two terms.
# > I implemented it using both iterative and recursive methods.
# > The iterative approach uses loops and is efficient (O(n)),
# > while the recursive approach calls itself and has exponential complexity (O(2ⁿ)).
# > For small inputs recursion is fine, but for large inputs iteration is preferred.” ✅

# ---

# Would you like me to add a **dry-run table** (step-by-step trace of variable values for n=5) — it’s often asked in practical viva to “trace the recursive calls”?
