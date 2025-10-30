# Python Functions Examples

This project contains example implementations of common functions with error handling and test cases.

## Functions

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

## Error Handling

Both functions include error handling for invalid inputs:
- Fibonacci function checks for negative numbers
- Addition function validates numeric types

## Test Cases

Each function comes with built-in test cases that demonstrate:
- Normal operation
- Edge cases
- Error conditions

## Running the Code

To run either example:

```bash
python fibonacci.py    # Run Fibonacci examples
python addNUmber.py   # Run Addition examples
```

## Requirements

- Python 3.x
- No additional dependencies required


<!-- CHANGELOG:START -->
What changed
	- Add function to add two numbers with input validation and error handling.
	- Document test cases for addition, including invalid input scenarios.
	- Update usage instructions to include the new addition function.
	- Clarify requirements and error handling for both functions.
<!-- CHANGELOG:END -->