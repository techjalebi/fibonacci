def is_prime(n):
    """
    Check if a number is prime.

    Args:
        n: The number to check (int)

    Returns:
        bool: True if the number is prime, False otherwise

    Raises:
        TypeError: If input is not an integer
        ValueError: If input is less than 0
    """
    if not isinstance(n, int):
        raise TypeError("Input must be an integer")
    if n < 0:
        raise ValueError("Input must be a non-negative integer")
    if n < 2:
        return False  # 0 and 1 are not prime numbers
    
    # Check for divisibility from 2 to square root of n
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Test data with various combinations
test_cases = [
    2,          # Smallest prime number
    3,          # Prime
    4,          # Not prime
    17,         # Prime
    25,         # Not prime
    97,         # Prime
    100,        # Not prime
    0,          # Not prime
    1,          # Not prime
    -5,         # Negative number (invalid)
    3.14,       # Float (invalid)
    "123",      # String (invalid)
]

for n in test_cases:
    try:
        result = is_prime(n)
        print(f"is_prime({n}) = {result}")
    except (TypeError, ValueError) as e:
        print(f"Error for input {n}: {e}")