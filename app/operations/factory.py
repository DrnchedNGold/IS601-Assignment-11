"""
Calculation Factory

This module implements the Factory Pattern for creating calculation objects.
It centralizes the logic for instantiating the correct calculation subclass
(Addition, Subtraction, Multiplication, Division) based on the requested type.

Usage:
    from app.operations.factory import CalculationFactory
    calc = CalculationFactory.create(calculation_type, user_id, inputs)
"""

from typing import List
import uuid
from app.models.calculation import Addition, Subtraction, Multiplication, Division

class CalculationFactory:
    """
    Factory for creating calculation objects based on type.
    """
    calculation_classes = {
        'addition': Addition,
        'subtraction': Subtraction,
        'multiplication': Multiplication,
        'division': Division,
    }

    @classmethod
    def create(cls, calculation_type: str, user_id: uuid.UUID, inputs: List[float]):
        """
        Create the appropriate calculation subclass.

        Args:
            calculation_type: Type of calculation (e.g., 'addition')
            user_id: UUID of the user creating the calculation
            inputs: List of numbers to calculate

        Returns:
            An instance of the appropriate Calculation subclass

        Raises:
            ValueError: If calculation_type is not supported
        """
        calculation_class = cls.calculation_classes.get(calculation_type.lower())
        if not calculation_class:
            raise ValueError(
                f"Unsupported calculation type: {calculation_type}"
            )
        # Division by zero validation
        if calculation_type.lower() == "division" and any(x == 0 for x in inputs[1:]):
            raise ValueError("Cannot divide by zero.")
        return calculation_class(user_id=user_id, inputs=inputs)
