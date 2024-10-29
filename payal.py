# Cleanroom Software Engineering Example: Simple Calculator

# Step 1: Specification - We define the requirements for our calculator.
# The calculator should perform basic operations: add, subtract, multiply, and divide.

def add(x, y):
    """Function to add two numbers"""
    return x + y

def subtract(x, y):
    """Function to subtract one number from another"""
    return x - y

def multiply(x, y):
    """Function to multiply two numbers"""
    return x * y

def divide(x, y):
    """Function to divide one number by another, handling division by zero"""
    if y == 0:
        return "Cannot divide by zero"
    return x / y

# Step 2: Design Verification - Verify each function meets its requirements.
# We create simple tests to verify that the functions work as expected.

def test_calculator():
    # Verify addition
    assert add(3, 4) == 7, "Addition test failed"
    # Verify subtraction
    assert subtract(10, 5) == 5, "Subtraction test failed"
    # Verify multiplication
    assert multiply(6, 3) == 18, "Multiplication test failed"
    # Verify division
    assert divide(9, 3) == 3, "Division test failed"
    # Test division by zero
    assert divide(9, 0) == "Cannot divide by zero", "Division by zero test failed"

    print("All tests passed!")

# Step 3: Statistical Testing - We test under different conditions to ensure reliability.
# In a full Cleanroom process, this would involve statistical methods, but here we use simple cases.

# Run the tests to verify the calculator functions
test_calculator()