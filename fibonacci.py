def fibonacci(n):
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

numbers = [0, 1, 2, 3, -4, 5, 6,7,8,9]
for n in numbers:
    try:
        result = fibonacci(n)
        print(f"fibonacci({n}) = {result}")
    except ValueError as e:
        print(f"Error for n={n}: {e}")