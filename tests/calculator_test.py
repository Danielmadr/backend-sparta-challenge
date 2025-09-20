import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))
from app.calculator_numpy import calculate_management_fee_per_shareholder
from app.calculator_brute_force import (
    calculate_management_fee_per_shareholder as calculate_management_fee_per_shareholder_brute_force,
)

INPUT_DATA = {
    "taxa": 0.02,
    "cotas": [
        {"valor": 100.0, "quantidades": [10, 50, 25]},
        {"valor": 102.5, "quantidades": [10, 40, 30]},
        {"valor": 101.0, "quantidades": [0, 40, 30]},
    ],
}
EXPECTED_OUTPUT = {0.1607142857142857, 1.0428571428571427, 0.682936507936508}

def test_calculate_management_fee_per_shareholder_numpy():
    actual_output = calculate_management_fee_per_shareholder(INPUT_DATA)

    assert set(actual_output) == EXPECTED_OUTPUT, f"Expected {EXPECTED_OUTPUT}, but got {actual_output}"

def test_calculate_management_fee_per_shareholder_brute_force():
    actual_output = calculate_management_fee_per_shareholder_brute_force(INPUT_DATA)

    assert set(actual_output) == EXPECTED_OUTPUT, f"Expected {EXPECTED_OUTPUT}, but got {actual_output}"