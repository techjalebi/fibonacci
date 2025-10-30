def add_numbers(a, b):
    """
    Add two numbers together.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        The sum of a and b
        
    Raises:
        TypeError: If inputs are not numbers
    """
    if not (isinstance(a, (int, float)) and isinstance(b, (int, float))):
        raise TypeError("Both inputs must be numbers")
    return a + b

# Test data with various combinations
test_cases = [
    (5, 3),      # Regular positive numbers
    (-2, 7),     # One negative, one positive
    (0, 0),      # Both zero
    (-4, -6),    # Both negative
    (1.5, 2.5),  # Floating point numbers
    ("a", 1),    # Invalid input - string
    (3, None),   # Invalid input - None
]

for a, b in test_cases:
    try:
        result = add_numbers(a, b)
        print(f"add_numbers({a}, {b}) = {result}")
    except TypeError as e:
        print(f"Error for inputs {a}, {b}: {e}")
