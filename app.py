"""
This module provides a FastAPI application for calculating health metrics such as BMI and BMR.

Classes:
    Gender (Enum): An enumeration representing the gender of an individual.

Functions:
    get_bmi(height: float, weight: float) -> dict:
        Calculate Body Mass Index (BMI) based on height and weight.
        
    get_bmr(height: float, weight: float, age: int, gender: Gender) -> dict:
        Calculate Basal Metabolic Rate (BMR) based on height, weight, age, and gender.

Usage:
    Run this module to start the FastAPI server and expose endpoints for BMI and BMR calculations.
"""

from enum import Enum
from fastapi import FastAPI
import uvicorn
from health_utils import calculate_bmi, calculate_bmr

app = FastAPI()

class Gender(str, Enum):
    """
    Gender is an enumeration that represents the gender of an individual.

    Attributes:
        MALE (str): Represents the male gender.
        FEMALE (str): Represents the female gender.
    """
    MALE = "male"
    FEMALE = "female"


@app.post("/bmi",
          description="Calculate Body Mass Index (BMI)")
async def get_bmi(height: float, weight: float):
    """
    Asynchronously calculates the Body Mass Index (BMI) based on height and weight.

    Args:
        height (float): The height of the individual in meters.
        weight (float): The weight of the individual in kilograms.

    Returns:
        dict: A dictionary containing the calculated BMI rounded to two decimal places.
    """
    bmi = calculate_bmi(height, weight)
    return {"bmi": round(bmi, 2)}

@app.post("/bmr",
          description="Calculate Basal Metabolic Rate (BMR)")
async def get_bmr(height: float, weight: float, age: int, gender: Gender):
    """
    Calculate the Basal Metabolic Rate (BMR) based on height, weight, age, and gender.

    Args:
        height (float): The height of the individual in centimeters.
        weight (float): The weight of the individual in kilograms.
        age (int): The age of the individual in years.
        gender (Gender): The gender of the individual, should be an instance of the Gender enum.

    Returns:
        dict: A dictionary containing the calculated BMR rounded to two decimal places.
    """
    bmr = calculate_bmr(height, weight, age, gender.value)
    return {"bmr": round(bmr, 2)}


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
