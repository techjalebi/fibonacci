# Python Functions Examples

This project contains example implementations of common functions with error handling and test cases.

## Functions
### 5. Number Root (`rootNumber.py`)

The `root_number(a, n=2)` function calculates the n-th root of a number with comprehensive error handling.

```python
root_number(a, n)  # Returns the n-th root of a
```

**Features:**
- Support for integers and floating-point numbers
- Type checking for inputs
- Handles invalid root degrees and negative roots
- Comprehensive error handling
- Test cases covering various scenarios

**Example Usage:**
```python
result = root_number(9, 2)  # Returns 3.0
result = root_number(27, 3) # Returns 3.0
```



### 1. Fibonacci Number Calculator (`fibonacci.py`)

The `fib(n)` function calculates the nth number in the Fibonacci sequence.

```python
fib(n)  # Returns the nth Fibonacci number
```

**Features:**
- Input validation for non-negative integers
- Error handling with descriptive messages
- Test cases covering various scenarios

**Example Usage:**
```python
result = fib(5)  # Returns 5 (0,1,1,2,3,5)
```

### 2. Number Addition (`addNUmber.py`)

The `add_numbers(a, b)` function adds two numbers together with comprehensive error handling.

```python
add_numbers(a, b)  # Returns the sum of a and b
```

**Features:**
- Support for integers and floating-point numbers
- Type checking for inputs
- Comprehensive error handling
- Test cases covering various scenarios

**Example Usage:**
```python
result = add_numbers(5, 3)  # Returns 8
```

### 3. Number Multiplication (`multiplyNumbers.py`)

The `multiply_numbers(a, b)` function multiplies two numbers together with comprehensive error handling.

```python
multiply_numbers(a, b)  # Returns the product of a and b
```

**Features:**
- Support for integers and floating-point numbers
- Type checking for inputs
- Comprehensive error handling
- Test cases covering various scenarios

**Example Usage:**
```python
result = multiply_numbers(5, 3)  # Returns 15
```

### 4. Number Division (`divideNumbers.py`)

The `divide_numbers(a, b)` function divides one number by another with comprehensive error handling.

```python
divide_numbers(a, b)  # Returns the result of a divided by b
```

**Features:**
- Support for integers and floating-point numbers
- Type checking for inputs
- Handles division by zero
- Comprehensive error handling
- Test cases covering various scenarios

**Example Usage:**
```python
result = divide_numbers(6, 3)  # Returns 2.0
```

## Error Handling
- Division function also checks for division by zero
+- Root function checks for invalid root degrees and negative roots

All functions include error handling for invalid inputs:
- Fibonacci function checks for negative numbers
- Addition, multiplication, and division functions validate numeric types
- Division function also checks for division by zero

## Test Cases

Each function comes with built-in test cases that demonstrate:
- Normal operation
- Edge cases
- Error conditions

## Running the Code
python rootNumber.py         # Run Root examples

To run any example:

```bash
python fibonacci.py        # Run Fibonacci examples
python addNUmber.py        # Run Addition examples
python multiplyNumbers.py  # Run Multiplication examples
python divideNumbers.py    # Run Division examples
```

## Requirements

- Python 3.x
- No additional dependencies required


<!-- CHANGELOG:START -->
What changed on 31-October-2025 at 01:30 PM UTC
  - Add function to calculate n-th root of a number with input validation and error handling.
  - Document test cases for root calculation, including invalid root degrees and negative roots.
  - Update usage instructions and error handling notes for all math functions.

What changed on 31-October-2025 at 01:23 PM UTC
  - Add function to divide two numbers with input validation and error handling.
  - Document test cases for division, including division by zero and invalid input scenarios.
  - Clarify error handling and usage for all arithmetic functions.
<!-- CHANGELOG:END -->