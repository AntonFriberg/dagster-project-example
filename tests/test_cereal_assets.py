"""Example of how to unit-test Dagster assets."""

from dagster_example.assets.cereal import cereals, highest_calorie_cereal, highest_protein_cereal

TEST_CEREALS = [
    {"name": "All-Bran", "calories": 70, "protein": 4},
    {"name": "Corn Flakes", "calories": 100, "protein": 2},
    {"name": "Special K", "calories": 110, "protein": 6},
]


def test_cereals_asset():
    """Example of a unit-test of an asset."""
    res = cereals()
    assert isinstance(res, list)
    assert len(res) == 77


def test_cereal_op_find_highest_protein_cereal():
    """Example of a unit-test of a down-stream asset."""
    assert highest_calorie_cereal(cereals=TEST_CEREALS) == "Special K"


def test_cereal_op_find_highest_calorie_cereal():
    """Example of a unit-test of a down-stream asset"""
    assert highest_protein_cereal(cereals=TEST_CEREALS) == "Special K"
