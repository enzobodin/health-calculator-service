"""
This module provides utility functions for health-related calculations.
"""
def calculate_bmi(height: float, weight: float) -> float:
    """
    Calculate the Body Mass Index (BMI) given height and weight.

    Args:
        height (float): The height of the individual in centimeters.
        weight (float): The weight of the individual in kilograms.

    Returns:
        float: The calculated BMI.
    """
    return weight / (height / 100) ** 2

def calculate_bmr(height: float, weight: float, age: int, gender: str) -> float:
    """
    Calculate the Basal Metabolic Rate (BMR) using the Harris-Benedict equation.

    Parameters:
    height (float): Height in centimeters.
    weight (float): Weight in kilograms.
    age (int): Age in years.
    gender (str): Gender of the person, either 'male' or 'female'.

    Returns:
    float: The calculated BMR.

    Raises:
    ValueError: If the gender is not 'male' or 'female'.
    """
    if gender == "male":
        return 88.362 + (13.397 * weight) + (4.799 * height) - (5.677 * age)
    elif gender == "female":
        return 447.593 + (9.247 * weight) + (3.098 * height) - (4.330 * age)
    else:
        raise ValueError("Invalid gender. Use 'male' or 'female'")
