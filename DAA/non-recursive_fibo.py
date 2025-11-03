def calculate_fibonacci_series(n):
    a, b = 0, 1
    step_count = 0
    fibonacci_series = []
    for i in range(n):
        step_count += 1
        fibonacci_series.append(a)
        a, b = b, a+b
    return fibonacci_series
if __name__ == "__main__":
    # Input from the user
    n = int(input("Enter the number of terms in the Fibonacci series: "))
    # Calculate the Fibonacci series and step count
    fibonacci_series= calculate_fibonacci_series(n)
    print(f"Fibonacci Series for the first {n} terms: {fibonacci_series}")