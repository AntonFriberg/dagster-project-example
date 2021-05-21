"""Example of how to unit-test Dagster solids."""
from typing import OrderedDict

from dagster import execute_solid

from solids.cereal_solids import (
    display_results,
    download_cereals,
    find_highest_calorie_cereal,
    find_highest_protein_cereal,
    hello_cereal,
)

TEST_CEREALS = [
    OrderedDict([("name", "All-Bran"), ("calories", 70), ("protein", 4)]),
    OrderedDict([("name", "Corn Flakes"), ("calories", 100), ("protein", 2)]),
    OrderedDict([("name", "Special K"), ("calories", 110), ("protein", 6)]),
]


def test_hello_cereal_solid():
    """Example of a unit-test of a simple solid."""
    res = execute_solid(hello_cereal)
    assert res.success
    assert len(res.output_value()) == 77


def test_cereal_solid_download_cereal():
    """Example of a unit-test of a simple solid."""
    res = execute_solid(download_cereals)
    assert res.success
    assert len(res.output_value()) == 77


def test_cereal_solid_find_highest_protein_cereal():
    """Example of a unit-test of a solid that takes both inputs and gices output."""
    res = execute_solid(find_highest_protein_cereal, input_values={"cereals": TEST_CEREALS})
    assert res.success
    assert res.output_value() == "Special K"


def test_cereal_solid_find_highest_calorie_cereal():
    """Example of a unit-test of a solid that takes both inputs and gices output."""
    res = execute_solid(find_highest_calorie_cereal, input_values={"cereals": TEST_CEREALS})
    assert res.success
    assert res.output_value() == "Special K"


def test_cereal_solid_display_result():
    """Example of a unit-test of a solid that gives no output."""
    test_inputs = {
        "most_calories": "Special K",
        "most_protein": "Special K",
    }
    res = execute_solid(display_results, input_values=test_inputs)
    assert res.success
