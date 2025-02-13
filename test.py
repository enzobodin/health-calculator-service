"""
This module contains the unit tests for the health_utils module and the FastAPI endpoints.

The tests are written using the pytest framework and the FastAPI TestClient.

The following tests are implemented:
- test_calculate_bmi: Tests the calculate_bmi function.
- test_calculate_bmr: Tests the calculate_bmr function.
- test_bmi_endpoint: Tests the /bmi endpoint.
- test_bmr_endpoint: Tests the /bmr endpoint.
"""
import pytest
from fastapi.testclient import TestClient
from app import app
from health_utils import calculate_bmi, calculate_bmr

client = TestClient(app)

def test_calculate_bmi():
    """
    Test the calculate_bmi function.

    This test checks if the calculate_bmi function correctly calculates the Body Mass Index (BMI)
    for a given height and weight. The expected result is compared using pytest.approx to allow
    for a small margin of error.

    Assertions:
        - The BMI calculated for a height of 175 centimeters and a weight of 70 kilograms should be approximately 22.86.
    """
    assert calculate_bmi(175, 70) == pytest.approx(22.86, 0.01)

def test_calculate_bmr():
    """
    Tests the calculate_bmr function.

    This function tests the Basal Metabolic Rate (BMR) calculation for both male and female inputs.

    Test cases:
    - Male: height=175 cm, weight=70 kg, age=30 years, gender="male"
        Expected result: approximately 1667.105 (with a tolerance of 0.01)
    - Female: height=165 cm, weight=60 kg, age=25 years, gender="female"
        Expected result: approximately 1385.785 (with a tolerance of 0.01)
    """
    # Test male
    assert calculate_bmr(175, 70, 30, "male") == pytest.approx(1695.667, 0.01)
    # Test female
    assert calculate_bmr(165, 60, 25, "female") == pytest.approx(1405.333, 0.01)

def test_bmi_endpoint():
    """
    Test the /bmi endpoint.

    This test sends a POST request to the /bmi endpoint with a JSON payload containing the height and weight.
    The expected result is compared to the response JSON.

    Assertions:
        - The response status code should be 200.
        - The response JSON should contain the calculated BMI, which should be approximately 22.86 for a height of 175 centimeters and a weight of 70 kilograms.
    """
    response = client.post("/bmi", params={"height": 175, "weight": 70})
    assert response.status_code == 200
    assert response.json() == {"bmi": 22.86}

def test_bmr_endpoint():
    """
    Test the /bmr endpoint.

    This test sends a POST request to the /bmr endpoint with a JSON payload containing the height, weight, age, and
    gender. The expected result is compared to the response JSON.

    Assertions:
        - The response status code should be 200.
        - The response JSON should contain the calculated BMR, which should be approximately 1667.11 for a height of 175 cm, weight of 70 kg, age of 30 years, and
    """
    response = client.post("/bmr", params={
        "height": 175,
        "weight": 70,
        "age": 30,
        "gender": "male"
    })
    assert response.status_code == 200
    assert response.json()["bmr"] == pytest.approx(1695.667, 0.01)
