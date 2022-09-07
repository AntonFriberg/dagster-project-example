"""Example of how to unit-test Dagster assets."""

from pathlib import Path

from dagster_example.assets.cereal import (
    CEREAL_URL,
    cereals,
    highest_calorie_cereal,
    highest_protein_cereal,
)

MOCKED_CEREAL_FILE = Path(__file__).parent / "misc/cereals.csv"

TEST_CEREALS = [
    {"name": "All-Bran", "calories": 70, "protein": 4},
    {"name": "Corn Flakes", "calories": 100, "protein": 2},
    {"name": "Special K", "calories": 110, "protein": 6},
]


def get_mocked_cereal_text():
    """Read data from csv file."""
    with open(MOCKED_CEREAL_FILE, "r", encoding="utf-8") as file:
        csv_text = file.read()
    return csv_text


def test_cereals_asset():
    """Example of a unit-test of an asset."""
    res = cereals()
    assert isinstance(res, list)
    assert len(res) == 77


def test_cereals_asset_mocked(requests_mock):
    """Example of a unit-test of an asset with mocked request."""
    dummy_cereal_text = get_mocked_cereal_text()
    requests_mock.get(CEREAL_URL, text=dummy_cereal_text)
    res = cereals()
    assert isinstance(res, list)
    assert len(res) == 77


def test_cereal_op_find_highest_protein_cereal():
    """Example of a unit-test of a down-stream asset."""
    assert highest_calorie_cereal(cereals=TEST_CEREALS) == "Special K"


def test_cereal_op_find_highest_calorie_cereal():
    """Example of a unit-test of a down-stream asset"""
    assert highest_protein_cereal(cereals=TEST_CEREALS) == "Special K"
