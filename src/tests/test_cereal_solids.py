"""Example of how to unit-test Dagster solids."""
from solids.cereal_solids import (
    display_results,
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)

TEST_CEREALS = [
    {"name": "All-Bran", "calories": 70, "protein": 4},
    {"name": "Corn Flakes", "calories": 100, "protein": 2},
    {"name": "Special K", "calories": 110, "protein": 6},
]


def test_hello_cereal_solid():
    """Example of a unit-test of a simple solid."""
    res = hello_cereal()
    assert isinstance(res, list)
    assert len(res) == 77


def test_cereal_solid_download_cereal():
    """Example of a unit-test of a simple solid."""
    res = download_cereals()
    assert isinstance(res, list)
    assert len(res) == 77


def test_cereal_solid_find_highest_protein_cereal():
    """Example of a unit-test of a solid that takes both inputs and gices output."""
    assert find_highest_protein_cereal(cereals=TEST_CEREALS) == "Special K"


def test_cereal_solid_find_highest_calorie_cereal():
    """Example of a unit-test of a solid that takes both inputs and gices output."""
    assert find_highest_calorie_cereal(cereals=TEST_CEREALS) == "Special K"


def test_cereal_solid_display_result(caplog):
    """Example of a unit-test of a solid that gives no output."""
    display_results(most_calories="Special C", most_protein="Special P")
    assert "Special C" in caplog.text
    assert "Special P" in caplog.text
