def root_number(a, n=2):
    """
    Calculate the n-th root of a number with error handling.

    Args:
        a: The number to find the root of (int or float)
        n: The degree of the root (int, default is 2 for square root)

    Returns:
        The n-th root of a

    Raises:
        TypeError: If inputs are not numbers
        ValueError: If n is zero or a negative root of a negative number
    """
    if not (isinstance(a, (int, float)) and isinstance(n, int)):
        raise TypeError("Input must be a number and root degree must be an integer")
    if n == 0:
        raise ValueError("Root degree cannot be zero")
    if a < 0 and n % 2 == 0:
        raise ValueError("Cannot take even root of a negative number")
    return a ** (1 / n)

# Test data with various combinations
test_cases = [
    (9, 2),      # Square root
    (27, 3),     # Cube root
    (16, 4),     # Fourth root
    (1, 5),      # Any root of 1
    (0, 2),      # Root of zero
    (-8, 3),     # Odd root of negative number
    (-16, 2),    # Even root of negative number (should error)
    (25, 0),     # Root degree zero (should error)
    ("a", 2),   # Invalid input - string
]

for a, n in test_cases:
    try:
        result = root_number(a, n)
        print(f"root_number({a}, {n}) = {result}")
    except (TypeError, ValueError) as e:
        print(f"Error for inputs {a}, {n}: {e}")
