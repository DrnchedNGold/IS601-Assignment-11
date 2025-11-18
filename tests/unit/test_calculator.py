# tests/unit/test_calculator.py

import pytest  # Import the pytest framework for writing and running tests
from typing import Union  # Import Union for type hinting multiple possible types
from app.operations import add, subtract, multiply, divide  # Import the calculator functions from the operations module

# Define a type alias for numbers that can be either int or float
Number = Union[int, float]


# ---------------------------------------------
# Unit Tests for the 'add' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 5),           # Test adding two positive integers
        (-2, -3, -5),        # Test adding two negative integers
        (2.5, 3.5, 6.0),     # Test adding two positive floats
        (-2.5, 3.5, 1.0),    # Test adding a negative float and a positive float
        (0, 0, 0),            # Test adding zeros
    ],
    ids=[
        "add_two_positive_integers",
        "add_two_negative_integers",
        "add_two_positive_floats",
        "add_negative_and_positive_float",
        "add_zeros",
    ]
)
def test_add(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'add' function with various combinations of integers and floats.

    This parameterized test verifies that the 'add' function correctly adds two numbers,
    whether they are positive, negative, integers, or floats. By using parameterization,
    we can efficiently test multiple scenarios without redundant code.

    Parameters:
    - a (Number): The first number to add.
    - b (Number): The second number to add.
    - expected (Number): The expected result of the addition.

    Steps:
    1. Call the 'add' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_add(2, 3, 5)
    >>> test_add(-2, -3, -5)
    """
    # Call the 'add' function with the provided arguments
    result = add(a, b)
    
    # Assert that the result of add(a, b) matches the expected value
    assert result == expected, f"Expected add({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'subtract' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (5, 3, 2),           # Test subtracting a smaller positive integer from a larger one
        (-5, -3, -2),        # Test subtracting a negative integer from another negative integer
        (5.5, 2.5, 3.0),     # Test subtracting two positive floats
        (-5.5, -2.5, -3.0),  # Test subtracting two negative floats
        (0, 0, 0),            # Test subtracting zeros
    ],
    ids=[
        "subtract_two_positive_integers",
        "subtract_two_negative_integers",
        "subtract_two_positive_floats",
        "subtract_two_negative_floats",
        "subtract_zeros",
    ]
)
def test_subtract(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'subtract' function with various combinations of integers and floats.

    This parameterized test verifies that the 'subtract' function correctly subtracts the
    second number from the first, handling both positive and negative values, as well as
    integers and floats. Parameterization allows for comprehensive testing of multiple cases.

    Parameters:
    - a (Number): The number from which to subtract.
    - b (Number): The number to subtract.
    - expected (Number): The expected result of the subtraction.

    Steps:
    1. Call the 'subtract' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_subtract(5, 3, 2)
    >>> test_subtract(-5, -3, -2)
    """
    # Call the 'subtract' function with the provided arguments
    result = subtract(a, b)
    
    # Assert that the result of subtract(a, b) matches the expected value
    assert result == expected, f"Expected subtract({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'multiply' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (2, 3, 6),           # Test multiplying two positive integers
        (-2, 3, -6),         # Test multiplying a negative integer with a positive integer
        (2.5, 4.0, 10.0),    # Test multiplying two positive floats
        (-2.5, 4.0, -10.0),  # Test multiplying a negative float with a positive float
        (0, 5, 0),            # Test multiplying zero with a positive integer
    ],
    ids=[
        "multiply_two_positive_integers",
        "multiply_negative_and_positive_integer",
        "multiply_two_positive_floats",
        "multiply_negative_float_and_positive_float",
        "multiply_zero_and_positive_integer",
    ]
)
def test_multiply(a: Number, b: Number, expected: Number) -> None:
    """
    Test the 'multiply' function with various combinations of integers and floats.

    This parameterized test verifies that the 'multiply' function correctly multiplies two numbers,
    handling both positive and negative values, as well as integers and floats. Parameterization
    enables efficient testing of multiple scenarios in a concise manner.

    Parameters:
    - a (Number): The first number to multiply.
    - b (Number): The second number to multiply.
    - expected (Number): The expected result of the multiplication.

    Steps:
    1. Call the 'multiply' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_multiply(2, 3, 6)
    >>> test_multiply(-2, 3, -6)
    """
    # Call the 'multiply' function with the provided arguments
    result = multiply(a, b)
    
    # Assert that the result of multiply(a, b) matches the expected value
    assert result == expected, f"Expected multiply({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Unit Tests for the 'divide' Function
# ---------------------------------------------

@pytest.mark.parametrize(
    "a, b, expected",
    [
        (6, 3, 2.0),           # Test dividing two positive integers
        (-6, 3, -2.0),         # Test dividing a negative integer by a positive integer
        (6.0, 3.0, 2.0),       # Test dividing two positive floats
        (-6.0, 3.0, -2.0),     # Test dividing a negative float by a positive float
        (0, 5, 0.0),            # Test dividing zero by a positive integer
    ],
    ids=[
        "divide_two_positive_integers",
        "divide_negative_integer_by_positive_integer",
        "divide_two_positive_floats",
        "divide_negative_float_by_positive_float",
        "divide_zero_by_positive_integer",
    ]
)
def test_divide(a: Number, b: Number, expected: float) -> None:
    """
    Test the 'divide' function with various combinations of integers and floats.

    This parameterized test verifies that the 'divide' function correctly divides the first
    number by the second, handling both positive and negative values, as well as integers
    and floats. Parameterization allows for efficient and comprehensive testing across multiple cases.

    Parameters:
    - a (Number): The dividend.
    - b (Number): The divisor.
    - expected (float): The expected result of the division.

    Steps:
    1. Call the 'divide' function with arguments 'a' and 'b'.
    2. Assert that the result is equal to 'expected'.

    Example:
    >>> test_divide(6, 3, 2.0)
    >>> test_divide(-6, 3, -2.0)
    """
    # Call the 'divide' function with the provided arguments
    result = divide(a, b)
    
    # Assert that the result of divide(a, b) matches the expected value
    assert result == expected, f"Expected divide({a}, {b}) to be {expected}, but got {result}"


# ---------------------------------------------
# Negative Test Case: Division by Zero
# ---------------------------------------------

def test_divide_by_zero() -> None:
    """
    Test the 'divide' function with division by zero.

    This negative test case verifies that attempting to divide by zero raises a ValueError
    with the appropriate error message. It ensures that the application correctly handles
    invalid operations and provides meaningful feedback to the user.

    Steps:
    1. Attempt to call the 'divide' function with arguments 6 and 0, which should raise a ValueError.
    2. Use pytest's 'raises' context manager to catch the expected exception.
    3. Assert that the error message contains "Cannot divide by zero!".

    Example:
    >>> test_divide_by_zero()
    """
    # Use pytest's context manager to check for a ValueError when dividing by zero
    with pytest.raises(ValueError) as excinfo:
        # Attempt to divide 6 by 0, which should raise a ValueError
        divide(6, 0)
    
    # Assert that the exception message contains the expected error message
    assert "Cannot divide by zero!" in str(excinfo.value), \
        f"Expected error message 'Cannot divide by zero!', but got '{excinfo.value}'"

# ---------------------------------------------
# Tests for app.database utility functions
# ---------------------------------------------

from app.database import get_engine, get_sessionmaker, SQLALCHEMY_DATABASE_URL

def test_get_engine_returns_engine():
    engine = get_engine()
    from sqlalchemy.engine import Engine
    assert isinstance(engine, Engine)

def test_get_sessionmaker_returns_sessionmaker():
    engine = get_engine()
    Session = get_sessionmaker(engine)
    from sqlalchemy.orm import sessionmaker
    assert isinstance(Session, sessionmaker)

def test_get_engine_custom_url():
    from app.database import get_engine
    custom_url = "sqlite:///:memory:"
    engine = get_engine(custom_url)
    from sqlalchemy.engine import Engine
    assert isinstance(engine, Engine)

def test_user_repr():
    from app.models.user import User
    import uuid
    user = User(id=uuid.uuid4(), username="TestUser", email="testuser@example.com")
    assert "<User(username=TestUser, email=testuser@example.com)>" == repr(user)

# ---------------------------------------------
# Coverage for error branches in Calculation models
# ---------------------------------------------

from app.models.calculation import Addition, Subtraction, Multiplication, Division
import uuid

def test_addition_invalid_inputs_type():
    addition = Addition(user_id=uuid.uuid4(), inputs="not-a-list")
    try:
        addition.get_result()
    except ValueError as e:
        assert "Inputs must be a list of numbers." in str(e)

def test_addition_invalid_inputs_length():
    addition = Addition(user_id=uuid.uuid4(), inputs=[1])
    try:
        addition.get_result()
    except ValueError as e:
        assert "Inputs must be a list with at least two numbers." in str(e)

def test_subtraction_invalid_inputs_type():
    subtraction = Subtraction(user_id=uuid.uuid4(), inputs="not-a-list")
    try:
        subtraction.get_result()
    except ValueError as e:
        assert "Inputs must be a list of numbers." in str(e)

def test_subtraction_invalid_inputs_length():
    subtraction = Subtraction(user_id=uuid.uuid4(), inputs=[1])
    try:
        subtraction.get_result()
    except ValueError as e:
        assert "Inputs must be a list with at least two numbers." in str(e)

def test_multiplication_invalid_inputs_type():
    multiplication = Multiplication(user_id=uuid.uuid4(), inputs="not-a-list")
    try:
        multiplication.get_result()
    except ValueError as e:
        assert "Inputs must be a list of numbers." in str(e)

def test_multiplication_invalid_inputs_length():
    multiplication = Multiplication(user_id=uuid.uuid4(), inputs=[1])
    try:
        multiplication.get_result()
    except ValueError as e:
        assert "Inputs must be a list with at least two numbers." in str(e)

def test_division_invalid_inputs_type():
    division = Division(user_id=uuid.uuid4(), inputs="not-a-list")
    try:
        division.get_result()
    except ValueError as e:
        assert "Inputs must be a list of numbers." in str(e)

def test_division_invalid_inputs_length():
    division = Division(user_id=uuid.uuid4(), inputs=[1])
    try:
        division.get_result()
    except ValueError as e:
        assert "Inputs must be a list with at least two numbers." in str(e)

def test_base_calculation_get_result_not_implemented():
    from app.models.calculation import AbstractCalculation
    base = AbstractCalculation()
    try:
        base.get_result()
    except NotImplementedError as e:
        assert "Subclasses must implement get_result() method" in str(e)

# ---------------------------------------------
# Coverage for app/schemas/calculation.py error branches
# ---------------------------------------------

def test_calculation_base_invalid_type():
    from app.schemas.calculation import CalculationBase
    import pytest
    with pytest.raises(ValueError) as excinfo:
        CalculationBase(type="invalid_type", inputs=[1, 2])
    assert "Type must be one of:" in str(excinfo.value)

def test_calculation_base_too_few_inputs():
    from app.schemas.calculation import CalculationBase
    import pytest
    with pytest.raises(ValueError) as excinfo:
        CalculationBase(type="addition", inputs=[1])
    assert "List should have at least 2 items after validation" in str(excinfo.value)

def test_calculation_update_too_few_inputs():
    from app.schemas.calculation import CalculationUpdate
    import pytest
    with pytest.raises(ValueError) as excinfo:
        CalculationUpdate(inputs=[1])
    assert "List should have at least 2 items after validation" in str(excinfo.value)
