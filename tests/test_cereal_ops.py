"""Example of how to unit-test Dagster ops."""
from dagster_example.ops.cereal import (
    display_results,
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)

from . import MOCKED_CEREAL_LEN

TEST_CEREALS = [
    {"name": "All-Bran", "calories": 70, "protein": 4},
    {"name": "Corn Flakes", "calories": 100, "protein": 2},
    {"name": "Special K", "calories": 110, "protein": 6},
]


def test_hello_cereal_op():
    """Example of a unit-test of a simple op."""
    res = hello_cereal()
    assert isinstance(res, list)
    assert len(res) == MOCKED_CEREAL_LEN


def test_cereal_op_download_cereal():
    """Example of a unit-test of a simple op."""
    res = download_cereals()
    assert isinstance(res, list)
    assert len(res) == MOCKED_CEREAL_LEN


def test_cereal_op_find_highest_protein_cereal():
    """Example of a unit-test of a op that takes both inputs and gices output."""
    assert find_highest_protein_cereal(cereals=TEST_CEREALS) == "Special K"


def test_cereal_op_find_highest_calorie_cereal():
    """Example of a unit-test of a op that takes both inputs and gices output."""
    assert find_highest_calorie_cereal(cereals=TEST_CEREALS) == "Special K"


def test_cereal_op_display_result(caplog):
    """Example of a unit-test of a op that gives no output."""
    display_results(most_calories="Special C", most_protein="Special P")
    assert "Special C" in caplog.text
    assert "Special P" in caplog.text
