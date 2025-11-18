import pytest
import uuid
import math
from app.operations.factory import CalculationFactory
from app.models.calculation import Addition, Subtraction, Multiplication, Division
from app.schemas.calculation import CalculationCreate, CalculationType

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([2, 3], 5),
        ([0, 0], 0),
        ([-1, -1], -2),
        ([1.5, 2.5], 4.0),
        ([1000000, 2000000], 3000000),
        ([0, 5], 5),
        ([5, 0], 5),
        ([-5, 5], 0),
        ([1, -1], 0),
        ([1.1, 2.2], 3.3),
        ([999999999, 1], 1000000000),
        ([0.1, 0.2], 0.3),
        ([1e10, 1e10], 2e10),
        ([1e-10, 1e-10], 2e-10),
        ([123456789, 987654321], 1111111110),
        ([float("inf"), 1], float("inf")),
        ([float("-inf"), 1], float("-inf")),
        ([float("nan"), 1], float("nan")),
    ]
)
def test_factory_addition_param(inputs, expected):
    calc = CalculationFactory.create("addition", uuid.uuid4(), inputs)
    result = calc.get_result()
    if isinstance(expected, float) and str(expected) == "nan":
        assert str(result) == "nan"
    elif isinstance(expected, float):
        assert math.isclose(result, expected, rel_tol=1e-9)
    else:
        assert result == expected

def dummy_user_id():
    return uuid.uuid4()

def test_factory_addition():
    inputs = [2, 3]
    calc = CalculationFactory.create("addition", dummy_user_id(), inputs)
    assert isinstance(calc, Addition)
    assert calc.get_result() == 5

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([5, 2], 3),
        ([0, 0], 0),
        ([-1, -1], 0),
        ([1.5, 2.5], -1.0),
        ([1000000, 2000000], -1000000),
        ([0, 5], -5),
        ([5, 0], 5),
        ([-5, 5], -10),
        ([1, -1], 2),
        ([1.1, 2.2], -1.1),
        ([999999999, 1], 999999998),
        ([0.1, 0.2], -0.1),
        ([1e10, 1e10], 0),
        ([1e-10, 1e-10], 0),
        ([123456789, 987654321], -864197532),
        ([float("inf"), 1], float("inf")),
        ([float("-inf"), 1], float("-inf")),
        ([float("nan"), 1], float("nan")),
    ]
)
def test_factory_subtraction_param(inputs, expected):
    calc = CalculationFactory.create("subtraction", uuid.uuid4(), inputs)
    result = calc.get_result()
    if isinstance(expected, float) and str(expected) == "nan":
        assert str(result) == "nan"
    elif isinstance(expected, float):
        assert math.isclose(result, expected, rel_tol=1e-9)
    else:
        assert result == expected

def test_factory_subtraction():
    inputs = [5, 2]
    calc = CalculationFactory.create("subtraction", dummy_user_id(), inputs)
    assert isinstance(calc, Subtraction)
    assert calc.get_result() == 3

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([2, 4], 8),
        ([0, 0], 0),
        ([-1, -1], 1),
        ([1.5, 2.5], 3.75),
        ([1000000, 2000000], 2000000000000),
        ([0, 5], 0),
        ([5, 0], 0),
        ([-5, 5], -25),
        ([1, -1], -1),
        ([1.1, 2.2], 2.42),
        ([999999999, 1], 999999999),
        ([0.1, 0.2], 0.02),
        ([1e10, 1e10], 1e20),
        ([1e-10, 1e-10], 1e-20),
        ([123456789, 987654321], 121932631112635269),
        ([float("inf"), 1], float("inf")),
        ([float("-inf"), 1], float("-inf")),
        ([float("nan"), 1], float("nan")),
    ]
)
def test_factory_multiplication_param(inputs, expected):
    calc = CalculationFactory.create("multiplication", uuid.uuid4(), inputs)
    result = calc.get_result()
    if isinstance(expected, float) and str(expected) == "nan":
        assert str(result) == "nan"
    elif isinstance(expected, float):
        assert math.isclose(result, expected, rel_tol=1e-9)
    else:
        assert result == expected

def test_factory_multiplication():
    inputs = [2, 4]
    calc = CalculationFactory.create("multiplication", dummy_user_id(), inputs)
    assert isinstance(calc, Multiplication)
    assert calc.get_result() == 8

@pytest.mark.parametrize(
    "inputs,expected",
    [
        ([10, 2], 5),
        ([0, 1], 0),
        ([-4, -2], 2),
        ([1.5, 0.5], 3.0),
        ([1000000, 2], 500000),
        ([5, 0.5], 10),
        ([-10, 2], -5),
        ([1, -1], -1),
        ([1.1, 2.2], 0.5),
        ([999999999, 1], 999999999),
        ([0.1, 0.2], 0.5),
        ([1e10, 1e5], 1e5),
        ([1e-10, 1e-5], 1e-5),
        ([123456789, 987654321], 0.125),
        ([float("inf"), 1], float("inf")),
        ([float("-inf"), 1], float("-inf")),
        ([float("nan"), 1], float("nan")),
    ]
)
def test_factory_division_param(inputs, expected):
    calc = CalculationFactory.create("division", uuid.uuid4(), inputs)
    result = calc.get_result()
    if isinstance(expected, float) and str(expected) == "nan":
        assert str(result) == "nan"
    elif isinstance(expected, float):
        assert math.isclose(result, expected, rel_tol=1e-6)
    else:
        assert result == expected

def test_factory_division():
    inputs = [10, 2]
    calc = CalculationFactory.create("division", dummy_user_id(), inputs)
    assert isinstance(calc, Division)
    assert calc.get_result() == 5

def test_factory_invalid_type():
    with pytest.raises(ValueError):
        CalculationFactory.create("modulus", dummy_user_id(), [10, 2])

def test_factory_division_by_zero():
    with pytest.raises(ValueError):
        CalculationFactory.create("division", dummy_user_id(), [10, 0])

@pytest.mark.parametrize(
    "type_,inputs,user_id,should_raise",
    [
        (CalculationType.ADDITION, [1, 2], uuid.uuid4(), False),
        (CalculationType.SUBTRACTION, [5, 3], uuid.uuid4(), False),
        (CalculationType.MULTIPLICATION, [2, 2], uuid.uuid4(), False),
        (CalculationType.DIVISION, [10, 2], uuid.uuid4(), False),
        ("modulus", [1, 2], uuid.uuid4(), True),
        (CalculationType.DIVISION, [10, 0], uuid.uuid4(), True),
        (CalculationType.ADDITION, [], uuid.uuid4(), True),
        (CalculationType.ADDITION, [1], uuid.uuid4(), True),
        (CalculationType.ADDITION, [1, "a"], uuid.uuid4(), True),
        (CalculationType.ADDITION, [None, 2], uuid.uuid4(), True),
        (CalculationType.ADDITION, [[1, 2], 3], uuid.uuid4(), True),
        (CalculationType.ADDITION, [1, 2], None, True),
        (CalculationType.ADDITION, [1, 2], "not-a-uuid", True),
    ]
)
def test_calculation_create_schema_param(type_, inputs, user_id, should_raise):
    if should_raise:
        with pytest.raises(Exception):
            CalculationCreate(
                type=type_,
                inputs=inputs,
                user_id=user_id
            )
    else:
        schema = CalculationCreate(
            type=type_,
            inputs=inputs,
            user_id=user_id
        )
        assert schema.type == type_
        assert schema.inputs == inputs

def test_calculation_create_schema_valid():
    schema = CalculationCreate(
        type=CalculationType.ADDITION,
        inputs=[1, 2],
        user_id=dummy_user_id()
    )
    assert schema.type == CalculationType.ADDITION
    assert schema.inputs == [1, 2]

def test_calculation_create_schema_invalid_type():
    with pytest.raises(ValueError):
        CalculationCreate(
            type="modulus",
            inputs=[1, 2],
            user_id=dummy_user_id()
        )

def test_calculation_create_schema_division_by_zero():
    with pytest.raises(ValueError):
        CalculationCreate(
            type=CalculationType.DIVISION,
            inputs=[10, 0],
            user_id=dummy_user_id()
        )
