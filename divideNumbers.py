def divide_numbers(a, b):
    """
    Divide one number by another with error handling.

    Args:
        a: Numerator (int or float)
        b: Denominator (int or float)

    Returns:
        The result of a divided by b

    Raises:
        TypeError: If inputs are not numbers
        ZeroDivisionError: If denominator is zero
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    if b == 0:
        raise ZeroDivisionError("Denominator cannot be zero")
    return a / b

# Test data with various combinations
test_cases = [
    (6, 3),      # Regular positive numbers
    (-8, 2),     # Negative numerator
    (0, 5),      # Zero numerator
    (7, -1),     # Negative denominator
    (4.5, 1.5),  # Floating point numbers
    (5, 0),      # Division by zero
    ("a", 1),   # Invalid input - string
    (3, None),   # Invalid input - None
]

for a, b in test_cases:
    try:
        result = divide_numbers(a, b)
        print(f"divide_numbers({a}, {b}) = {result}")
    except (TypeError, ZeroDivisionError) as e:
        print(f"Error for inputs {a}, {b}: {e}")
